from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)-> List[str]:
    """
    This function will return a list of requirements

    Args:
        file_path (str): The path of the file as a string

    Returns:
        List[str]: Returns a list of requirements
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        # Removing the vertical space (\n)
        requirements = [requirement.replace('\n',"") for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name = "mlproject",
    version = '0.0.1',
    author = "Hari Hara Chandar",
    author_email = "hariharachandar0715@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)