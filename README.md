# Project Name

    Basic calculator app

## Overview

    I have created a basic calculator app with 4 different features - add, subtract, divide, multiply.
    I have implemented a CI pipeline into my project with the aim to demostrate DevOps practices.

    My goals are :
    Version control workflow.
    Pull requests
    Automated building and testing.
    Enfoced test coverage of 80%
    Azure pipelines CI
    Code analysis
    Branch protection
    documentation

## Technologies Used

    YAML
    GitHub
    Python
    PyTest
    PyTest-cov
    Pylint
    Azure pipelines

## Local Development Setup

    1 Clone the repo
        git clone https://github.com/Dean-Farrelly13245/X00171562_CA2_DevOps.git

    2 Install Dependencies
        pip install -r requirements.txt

    3 Run Application
        python Calculator/calculator.py

    4 Run tests and code coverage
        pytest --cov=Calculator --cov-fail-under=80

## Application Features

    My calculator supports the four main functions you would expect:
    Addition
    Subtraction
    Multiplication
    Division

    The main() loops allowing a user to choose an operation then input two numbers and get the correct result - this repeats till the user chooses to exit the application.

    all four operations and main are unit tested.

## CI Pipeline Implementation

    I have created my pipeline in azure-pipelines.yml

    This pipeline does the following :
        Uses UsePythonVersion@0 to select Python 3.11

        Installs all requirements from requirements.txt

        Runs Pylint using a minimun score requirement.

        Executes Tests by running "pytest --cov=Calculator --cov-report=xml --cov-fail-under=80" which also checks for code coverage is above 80%.

        Unit test results visible in Azure Pipelines.

        XML coverage uploaded for reporting.

        The pipeline runs automatically when :
            Pushes are made to main or development branch.
            Pull Requests are made to the main or development Branch.

Pipeline – Successful Run
<img width="1553" height="165" alt="TestsPassedandcoverage" src="https://github.com/user-attachments/assets/1497dec9-8ddf-477a-9c62-c536c08cd456" />
Test Results
<img width="1554" height="217" alt="testssummary" src="https://github.com/user-attachments/assets/9fa7c1ce-b8d6-479e-82cc-e2b9500c4b1e" /> 
Coverage Summary
<img width="609" height="277" alt="CoverageSummary" src="https://github.com/user-attachments/assets/f964804f-bb58-4bbc-a9c2-da02eb45b923" />


## Branch Policies and Protection

    My project is setup to use a main and development branch.
    Development is the active working branch.
    Main is the protected release branch.

    Branch protection configured on main:
        Require pull requests before merging
        Status checks to pass
        disabled direct pushes
        branch must be up to date before merging

Main Branch Protection Rules
<img width="692" height="830" alt="Branchpol1" src="https://github.com/user-attachments/assets/6dc297eb-91de-477e-97af-817d51e811ed" />
<img width="692" height="125" alt="branchpol2" src="https://github.com/user-attachments/assets/afd3f376-aed3-440d-9366-dcc25a21f9eb" />


    NOTE!
    I setup the branch rules fully but get the error "Your protected branch rules for your branch won't be enforced on this private repository until you move to a GitHub Team or Enterprise organization account." - the CA Brief states the github repo must be private so i kept it as private.
<img width="770" height="144" alt="Screenshot 2025-11-13 153628" src="https://github.com/user-attachments/assets/303f925a-4cf4-4d0c-afc8-8c7920974699" />

Pull Request 
<img width="836" height="625" alt="pullRequest" src="https://github.com/user-attachments/assets/c136aff0-6e35-44d2-811c-2032198fa61a" />

## Testing Strategy

    My tests are done using pytest which covers:
        All my arithmetic functions
        Division by 0 error handling
        CLI behaviour using monkeypatch to mimic user input and capsys to validate printed output

    My Code Coverage currently is over 95%.



## Troubleshooting Guide
Tests Pass Locally but Fail in CI
causes:
    Wrong file paths
    Different Python versions
    Missing dependencies in requirements.txt

Fix:
    install dependencies locally using:

    pip install -r requirements.txt

Ensure Azure Pipelines contains the same installation step:

    pip install -r requirements.txt
    

Branch Protection Warning on GitHub
    GitHub Free accounts do not enforce branch protection on private repos anymore.

