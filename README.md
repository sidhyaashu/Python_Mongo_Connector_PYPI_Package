# Python_Mongo_Connector_PYPI_Package
This is a custom python package for connect mongodb


# Development and Testing Setup
Overview of Dependency Files
    1. requirements.txt: This file lists the dependencies required to run the production version of the Python project. It ensures that all necessary packages for deployment are available.

    2. requirements_dev.txt: This file contains dependencies needed specifically for development and testing. Keeping these separate from requirements.txt helps in managing dependencies more efficiently and avoids installing unnecessary packages in the production environment.

# Tox for Python Package Testing
    1. tox.ini: This file is used to configure Tox, a tool that automates testing of Python packages across multiple Python versions. Tox creates isolated environments (.tox) to install dependencies, run tests, and execute commands. It acts as a combination of virtualenvwrapper and Makefile for managing virtual environments and task automation.
    Project Configuration Files

    2. pyproject.toml: A modern configuration file for Python projects, used as an alternative to setup.cfg. It defines the build system (like the build tool used, package name, version, author, license, and dependencies).

    3. setup.cfg: A configuration file utilized by setuptools to manage the packaging and installation process of the Python project.

# Testing the Python Application
    1.Types of Testing
        1. Automated Testing: Testing done by tools/scripts to validate the functionality of the application without manual intervention.
        2. Manual Testing: Testing performed manually by a developer or tester to verify the correctness of the application.
        Modes of Testing
        3. Unit Testing: Focuses on testing individual units or components of the code.
        Integration Testing: Checks the combined functionality of integrated components.

    2.Testing Frameworks
        1. pytest: A popular testing framework for simple unit tests.
        2. unittest: Python's built-in module for unit testing.
        3. pylint: A tool to check for coding standards and errors.
        4. flake8: A comprehensive tool that includes pylint, pycodestyle, and mccabe for checking style, formatting, and complexity.
        5. pycodestyle: Checks Python code against the style conventions in PEP 8.