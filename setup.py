from setuptools import find_packages, setup
from typing import List

Edot = "-e . "


def get_requirements(file_path: str) -> List[str]:
    """
    This function return list of requirements

    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if Edot in requirements:
            requirements.remove(Edot)
    print(requirements)
    return requirements


setup(
    name="handproj",
    version="0.0.1",
    author="AbdelrhmanFawzy",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
