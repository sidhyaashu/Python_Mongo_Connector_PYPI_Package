from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPEN_E_DOT]

    return requirements

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Python_Mongo_Connector_PYPI_Package"
PKG_NAME = "Mongo_connect_pkg"
AUTHOR_USER_NAME = "sidhyaashu"
AUTHOR_EMAIL = "ashutoshsidhya69@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with MongoDB database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("./requirements_dev.txt"),
)
