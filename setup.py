from setuptools import setup, find_packages
from typing import List  # Add this import statement

def get_requirements(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="diamond price",
    version="0.0.1",
    author="indranil saha",
    author_email="indranilsaha047@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
