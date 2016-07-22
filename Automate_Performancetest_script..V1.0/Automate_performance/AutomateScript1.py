# This is to Automate the performance test execution using MSTEST and Subprocess module
'''
    Author :Bharadwaj Aryasomayjaula
    email id:baryasom@asu.edu
    Instructions for execution:
    1. Should have MsTEST and VSTS installed.
    2. Should have Python as Environment Variables
    Notes to Developers:
    Development Scope:
    * Getting Response Time to the Results
    * Making Report from the results
    * Distributed using Multithreading
'''
from subprocess import *
import os,glob
import datetime
# this is for getting files in directory

class Automate_performancetest:
    def __init__(self):
        self.Locationoffiles=""

    # This method gets the location and file names in folder where the test scripts reside.
    def get_filenames(self):
        self.list_of_files=[]
        self.Locationoffiles=raw_input("Enter the path for getting the files: ")
        self.Locationoffiles.replace("\\","//")
        print self.Locationoffiles
        os.chdir(self.Locationoffiles)
        for file in glob.glob("*.webtest"):
            print file
            self.list_of_files.append(file)

        print("File names have been retrieved")
    # At the moment the environment variables are not added. This resulted in change in Environment Variables
    '''def check_add_environ(self):
        path_values=os.environ['PATH']
        print path_values
        #this is the path of mstest i.e visual studio dev cmd
        mstest_dev_path="C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools".replace("\\","//")
        for a in path_values:
            if a==mstest_dev_path:
                print "already exists"
            else:
                os.environ['PATH']= path_values+mstest_dev_path
                exit()'''
    # This method aims to use call to execute the performance test scripts
    def execute_the_commands(self):
        filename=raw_input("Enter the file name with format you want to save the results: ")
        f=open(filename,'a')
        for file in  self.list_of_files:
            mstest_dev_path = ("cd C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\ && MSTest/testcontainer:"+self.Locationoffiles+"\\"+file).replace("\\", "//")
            call(mstest_dev_path,shell=True,stderr=f,stdout=f)
            print file+" performance test has been completed"
        print"*************** Succesfullycompleted************"
        f.close()
    def putting_all_togather(self):
        self.get_filenames()
        self.execute_the_commands()
x=Automate_performancetest()
x.putting_all_togather()

