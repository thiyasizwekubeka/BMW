# Tech Talent Day 2023 :: Data Engineering


## Pre-requisite Knowledge

* Experience and knowledge working with python
* Basic knowledge of git source control
* Experience in deploying and maintaining data engineering jobs in AWS.
* Knowledge working with Infrastructure as Code (Terraform) is required.
* Familiarity working with Linux is required. 


## Recommended Software

The following software is required to be installed on the laptop to participate in the Tech Talent Day

* Python 3.10.8 or above - [Python Windows Downloads](https://www.python.org/downloads/windows/) or [Python macOS Downloads](https://www.python.org/downloads/macos/) or download python for Linux using the relevant Python 3 package manager. 

* Source Control - [GIT Source Control](https://git-scm.com/downloads)  - Download and install the Git client from [here](https://git-scm.com/downloads). This step is required as all the code and the challenges will be hosted in a git repository.  

* Install the latest version of the AWS CLI. Follow the instructions on the home page. [AWS Command Line Interface](https://aws.amazon.com/cli/)

* IDE - [Visual Studio Code](https://code.visualstudio.com/download) -It is recommended that Visual studio code or a supported Python IDE like Pycharm.  The following extensions for Visual Studio code are recommended. 
    - [Python Visual Studio code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Provides rich support for the Python Language.
    - [HashiCorp Terraform - Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform) - Adds editing features for Terraform files such as  files such as syntax highlighting, IntelliSense, code navigation, code formatting, module explorer and much more!

* Infrastructure as Code (IaC) [Terraform](https://developer.hashicorp.com/terraform/downloads) - Terraform version `1.3.4` or above must be installed.

## Getting Started


a. Check if your python is installed correctly
```bash
# Check the version of python installed
python --version

# OR run the below command if you have not aliased python version on linux. 
python3 --version

```

b. Create a virtual environment so that the application is not influenced by global dependencies. The section below shows how the virtual environment can be setup in Linux
```bash
# Create a virtual environment using the command below on linux
virtualenv venv

# Start the virtual environment
source venv/bin/activate
```

c. Install the pre-requisites for python using the `requirements.txt` file. 
```bash
# Install cookiecutter and other libraries required. 
pip install -r requirements.txt

# Set a phrase to print
export PHRASE="Welcome to BMW Tech Talent Day 2023"

# Check if python is working
# You should see cool picture- Welcome to BMW Tech Talent Day 2023
python sample.py

# OR if python is not aliased. 
python3 sample.py

# Check if your cookiecutter is working
cookiecutter -V

```
d. Check if your `cookiecutter ` application is working correctly.



e. Check if the correct version of terraform is installed. 

```bash
# Navigate to the infrastructure folder within the repository and running the following commands. 
cd ./infrastructure

# Run the terraform version and init command
terraform --version

# Run the init and the plan command. 
terraform init && terraform plan

# Apply the configuration and test
terraform apply
```

# BMW
# BMW
