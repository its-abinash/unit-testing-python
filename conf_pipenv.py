import os

#######################################  Installing PIPENV for python #####################################

def install_requirements():
    os.system('pip3 install pipenv')

    os.system('pipenv install pytest-cov')

    os.system('pipenv install pytest --dev')

    os.system('pipenv install coverage --dev')