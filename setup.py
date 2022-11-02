from setuptools import find_packages, setup
from typing import List

def get_requirements()->List of get_requirements

requirement_list:List[str] = []




return requirement_list

setup(
    name="sensor",
    version="0.01",
    author="Hansraj",
    author_email="shansraj451@gmail.com",
    packages = find_packages(),
    install_require=["pymongo==4.2.0"],
)