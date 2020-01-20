import os

def file_path():
    return str(os.getcwd() + '/file_app/')

def test_file_path():
    return str(os.getcwd() + '/file_app/test_app.py')

def report_file_path():
    return str(os.getcwd() + '/htmlcov/index.html')

def number_of_failed_tc():
    l = ['testsuites', 'testsuite', '@failures']
    return l

def number_of_tc():
    l = ['testsuites', 'testsuite', '@tests']
    return l