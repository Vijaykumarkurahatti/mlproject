from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove the editable install flag if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Vijaykumar',
    author_email='vijayfk123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
