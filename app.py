'''

__author__ = Abinash Biswal
All rights reserved (c) 2019 Abinash Biswal.

'''
import os
import location as loc                   # It contains the location of some useful files
import xmltodict
from email_user import send_email        # It contains the code to email an attachment
import email_credentials as ec           # It contains the credentials of user and administrator for mail purpose
from get_percentage import percentage    # It contains the code, which calculates the percentage of testCases ran(during testing)
import message_rep as mr                 # It contains the message of report, which has to be used while sending mail to the user

'''
    Install PIPENV if it is not installed and configure all files which will be needed
'''
from conf_pipenv import install_requirements

install_requirements()   # Installing the virtual env to run all files in separate env

contain = len(os.listdir(os.getcwd() + '/testfiles/')) # Precalculation of length of the folder(/testfiles contains the testcase files created by administrators)

getTotalPerc = 0.0
maxPerc = contain * 100

os.system('pipenv run pytest ./userfile/. ./testfiles/. --junitxml=coverage.xml')   # This command will iteratively run each userCode with testCode, which are residing at /userfile and /testfiles inside /testfile
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/testfile/'
my_file = os.path.join(THIS_FOLDER, 'coverage.xml')  # Merged the directory containing .xml reportFile

with open(my_file) as fd:
    doc = xmltodict.parse(fd.read())  # Converting XML -> Dictionary(name of dict is 'doc')

getTotalPerc += percentage(int(doc[loc.number_of_failed_tc()[0]][loc.number_of_failed_tc()[1]][loc.number_of_failed_tc()[2]]), int(doc[loc.number_of_tc()[0]][loc.number_of_tc()[1]][loc.number_of_tc()[2]])) # Calculating the percentage of correctness of code against testCases and adding it to a variable 'getTotalPerc'
report = open("report.pdf", "w") # Creating reportFile
report.seek(0)
report.truncate()                # Removing everything before appending new record

totalPerc = float((getTotalPerc / maxPerc) * 100.00) # Total percentage
print('perc: ', totalPerc)
if(totalPerc > 75.0):    # Criteria is set to >= 75% (This is an example)
    report.write(mr.success_msg() + "{:.2f}".format(totalPerc) + '%')
else:
    report.write(mr.failure_msg())

report.close()

send_email(ec.sender(), ec.token(), ec.receiver(), 'REPORT', 'Your exam result') #Sending email to the user containign corresponding attachment
os.system('rm coverage.xml report.pdf') # Clearing current files
os.system('rm -rf ../.pytest_cache/ ../__pycache__')
