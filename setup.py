from setuptools import setup, find_packages

setup(
    name='CDKGuardian',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'cdk_guardian = cdk_guardian.main:main',
        ],
    },
)
