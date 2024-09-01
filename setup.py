from setuptools import setup, find_packages

# Read the contents of the README file for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Define package version
__version__ = "0.0.1"

# Define package details
REPO_NAME = "Python_Mongo_Connector_PYPI_Package"
PKG_NAME = "PyMongodbConnector"
AUTHOR_USER_NAME = "sidhyaashu"
AUTHOR_EMAIL = "ashutoshsidhya69@gmail.com"

# Setup the package
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with MongoDB database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
