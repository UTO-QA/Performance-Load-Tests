# Script to combine single-sign module with httperf for iseaarchloadtesting
'''
    Author:Bharadwaj (braddy)
    email:baryasom@asu.edu
    Instructions to execute :
    1. Need to have Following files
            ASULogin.py,FilterLogs.py,httpe_selenium.py,,user_input.py
    2. Need to Linux Machine for Httperf
'''
from subprocess import call
import threading
from httpe_selenium import getselenium

class httperf_test(threading.Thread):

    def __init__(self, name,sessionvalue):
        self.sessionvalue=sessionvalue
        threading.Thread.__init__(self)
        self.name = "thread " + name

    def run(self):
        print "Starting " + self.name
        self.connect()
        print "Exiting " + self.name

    def connect(self):
        print "starting"
        if(self.sessionvalue!="novalue"):
            print "inlogin"
            call(
                " httperf --add-header 'Cookie:SSESSd0b53dd39734cedf16e25bb4ade4ff0b=" + self.sessionvalue + ";SSONAME=Bharadwaj\n' --ssl --server isearch.asu.edu  --wsesslog 1,0,/home/bhaddy-linux/isearchlog_uri_2.log ",shell=True)
        else:
            call(" httperf --ssl --server isearch.asu.edu  --wsesslog 1,0,/home/bhaddy-linux/isearchlog_uri_3.log",shell=True)

        print "finished"

value=""
length = raw_input("Enter the number of threads")
threads = []
userlogin=raw_input("DO you want to login or Proceed Without login yes/no")
if userlogin=="yes":
    create_session = getselenium()
    value = create_session.connect_selenium()
    print value
else:
    print"not logging in"
    value="novalue"

for i in range(0, int(length)):
    thread = httperf_test(str(i),value)
    threads += [thread]
    thread.start()
print"completed"
