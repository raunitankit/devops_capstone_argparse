from setuptools import setup, find_packages

setup(
    name="devops_capstone",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "requests",
        "schedule",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "capstone=app.app:main"
        ]
    },
)