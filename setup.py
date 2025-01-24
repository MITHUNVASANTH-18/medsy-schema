from setuptools import setup, find_packages

setup(
    name="medsy-schema",
    version="0.1.0",
    description="Schema for Flask Admin and User backends",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
)
