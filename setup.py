from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List:
    """
    :param file_path:
    :return: the list of requirements
    """

    requirements = []
    with open(file_path, "r") as requirements_file:
        requirements = requirements_file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='deryl',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)