# Project Name

   CI/CD pipeline for Basic calculator app

## Overview
This project is a continuation from my CA1 Calculator app where i implement a full CI/CD pipeline which does the following:
    Multi stage YAML pipeline
    Automated testing
    static code analysis
    security scanning
    deployment to both test and production enviorments
    approval gates

## Technologies Used

## Application
    Python
    Flask
    HTML

## Testing
    PyTest
    PyTest-cov
    Selenium
    Bandit
    Pylint
    pip-audit

## DevOps
    Azure pipelines
    Azure App Service
    Multi-Stage YAML
    Azure Environments

## Local Development Setup

    1 Clone the repo
        git clone https://github.com/Dean-Farrelly13245/X00171562_CA3_DevOps.git

    2 Install Dependencies
        pip install -r requirements.txt

    3 Run Application
        python app.py

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

    The app now has a Flash web interface with a simple UI to use the calculator , this is fully tested using selenium.
    Deployed to Azure App Services - Test and Production.

## CI Pipeline Implementation

    I have updated my pipeline in azure-pipelines.yml

    This pipeline does the following :
        Uses UsePythonVersion@0 to select Python 3.11

        Installs all requirements from requirements.txt

        Runs Pylint using a minimun score requirement.

        Executes Unit Tests by running "pytest --cov=Calculator --cov-report=xml --cov-fail-under=80" which also checks for code coverage is above 80%.

        Runs a performance test using a pytest timing loop

        Runs security tests:
            Bandit: source code security scan.
            pip-audit: dependency vulnerability scanner.

        publishes test results and code coverage to Azure.

        Publishes a build artefact which is used for deployment to both environments

        Runs selenium UAT tests to validate flask web interface.

        Deploys application to Azure test environment using a Managed Indentity service connection

        Requires manual approval before deploying the same build to the production environment.

        XML coverage uploaded for reporting.

        The pipeline runs automatically when :
            Pushes are made to main or development branch.
            Pull Requests are made to the main or development Branch.

## Pipeline – Successful Run
   <img width="1049" height="264" alt="pipeline_sucess" src="https://github.com/user-attachments/assets/78f46148-d684-43b3-8182-c9a38ddfc8a9" />
## Test Results
   <img width="1565" height="228" alt="Tests_passed" src="https://github.com/user-attachments/assets/e46cfac4-533b-4d0a-903c-92ae52c6ad49" />
Environments
<img width="621" height="298" alt="deployed_enviroments" src="https://github.com/user-attachments/assets/336d5808-b4d9-43a3-b2a0-3402e0ed7618" />
Coverage Summary
<img width="606" height="267" alt="Code_Coverage" src="https://github.com/user-attachments/assets/254946cc-7b2f-45fc-a463-d419de2577b1" />


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



