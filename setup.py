from setuptools import setup, find_packages

setup(
    name='memorize-wizard',
    version='0.1.1',
    packages=find_packages(), 
    include_package_data=True, 
    install_requires=[
        "Flask==1.1.2", 
        "click==8.0.1", 
        "gTTS==2.2.2", 
        "requests==2.25.1", 
        "simple-term-menu==1.2.1", 
        "pydub==0.25.1"
    ],
    entry_points={
        'console_scripts': [
            'wizard = wizard.main:cli',
        ],
    },
)
