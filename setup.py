from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'  # Corrected value

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of required packages
    by reading from the given requirements file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if present

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Rithi',
    author_email='rithikaravichandran25@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
