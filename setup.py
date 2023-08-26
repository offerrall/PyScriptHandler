from setuptools import setup, find_packages

setup(
    name='pyscripthandler',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'psh=pyscripthandler.main:main',
        ],
    },
)
