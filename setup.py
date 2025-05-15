'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements 
    
    """

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="mlproject_customer_churn_prediction_telecom_company",
    version="0.0.1",
    author="Faisal Mehmood",
    author_email="shahfaisal1234@gmail.com",
    packages=find_packages(),
    description="A machine learning project for customer churn prediction in a telecom company",
    long_description="This project uses machine learning algorithms to predict customer churn in a telecom company. It includes data preprocessing, model training, and evaluation.",
    install_requires=get_requirements()
)