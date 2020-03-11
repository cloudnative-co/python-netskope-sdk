from setuptools import setup, find_packages

setup(
    name="Netskope-SDK",
    version="0.4",
    description="Netskope SDK for Python",
    author="sebastian",
    author_email="seba@cloudnative.co.jp",
    packages=find_packages(),
    install_requires=[
        "jsonschema"
    ],
    entry_points={
        "console_scripts": [
        ]
    },
)
