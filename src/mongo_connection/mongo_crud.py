from typing import Any, Optional, Union
import os
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
import json
import logging
from ensure import ensure_annotations

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@ensure_annotations
class MongoOperation:
    _client: Optional[MongoClient] = None  # Singleton MongoDB client
    _collection = None  # Private variable for MongoDB collection
    _database = None  # Private variable for MongoDB database

    def __init__(self, client_url: str, database_name: str, collection_name: Optional[str] = None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    def create_mongo_client(self) -> MongoClient:
        if not MongoOperation._client:
            try:
                MongoOperation._client = MongoClient(self.client_url)
                logger.info("MongoDB client created successfully.")
            except ConnectionFailure as e:
                logger.error(f"Failed to connect to MongoDB: {e}")
                raise
        return MongoOperation._client

    def create_database(self) -> Any:
        if not MongoOperation._database:
            client = self.create_mongo_client()
            MongoOperation._database = client[self.database_name]
            logger.info(f"Database '{self.database_name}' created/connected successfully.")
        return MongoOperation._database

    def create_collection(self, collection_name: Optional[str] = None) -> Any:
        collection_name = collection_name or self.collection_name
        if not MongoOperation._collection or MongoOperation._collection.name != collection_name:
            database = self.create_database()
            MongoOperation._collection = database[collection_name]
            logger.info(f"Collection '{collection_name}' created/connected successfully.")
        return MongoOperation._collection

    def insert_record(self, record: Union[dict, list], collection_name: str) -> Any:
        try:
            collection = self.create_collection(collection_name)
            if isinstance(record, list):
                if not all(isinstance(data, dict) for data in record):
                    raise TypeError("All records in the list must be dictionaries.")
                collection.insert_many(record)
                logger.info(f"{len(record)} records inserted successfully into '{collection_name}'.")
            elif isinstance(record, dict):
                collection.insert_one(record)
                logger.info(f"1 record inserted successfully into '{collection_name}'.")
            else:
                raise TypeError("Record must be a dictionary or a list of dictionaries.")
        except PyMongoError as e:
            logger.error(f"Failed to insert record(s) into MongoDB: {e}")
            raise

    def bulk_insert(self, datafile: str, collection_name: Optional[str] = None) -> None:
        try:
            if datafile.endswith('.csv'):
                dataframe = pd.read_csv(datafile, encoding='utf-8')
            elif datafile.endswith(".xlsx"):
                dataframe = pd.read_excel(datafile, encoding='utf-8')
            else:
                raise ValueError("Unsupported file format. Only .csv and .xlsx are supported.")

            datajson = json.loads(dataframe.to_json(orient='records'))
            collection = self.create_collection(collection_name)
            collection.insert_many(datajson)
            logger.info(f"Bulk insert of {len(datajson)} records into '{collection_name}' successful.")
        except (FileNotFoundError, ValueError) as e:
            logger.error(f"Error in reading the file: {e}")
            raise
        except PyMongoError as e:
            logger.error(f"Failed to insert records into MongoDB: {e}")
            raise

    def update_record(self, filter_query: dict, update_data: dict, collection_name: Optional[str] = None) -> None:
        try:
            collection = self.create_collection(collection_name)
            result = collection.update_many(filter_query, {'$set': update_data})
            logger.info(f"{result.modified_count} record(s) updated in '{collection_name}'.")
        except PyMongoError as e:
            logger.error(f"Failed to update records: {e}")
            raise

    def delete_record(self, filter_query: dict, collection_name: Optional[str] = None) -> None:
        try:
            collection = self.create_collection(collection_name)
            result = collection.delete_many(filter_query)
            logger.info(f"{result.deleted_count} record(s) deleted from '{collection_name}'.")
        except PyMongoError as e:
            logger.error(f"Failed to delete records: {e}")
            raise

    def close_connection(self) -> None:
        if MongoOperation._client:
            MongoOperation._client.close()
            logger.info("MongoDB connection closed.")
            MongoOperation._client = None
