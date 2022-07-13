from setuptools import setup
from typing import List



# Declaring Variables for setup Functions.
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Mohammed Ismail"
DESCRIPTION="This is a first FSDS NOV batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


# Return list which will have string in it to install requirements and housing/packages.
def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    Mention in requirements.txt file.
    
    return: This function is going to return a list which contain name of libraries mentioned 
    in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,       
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)
