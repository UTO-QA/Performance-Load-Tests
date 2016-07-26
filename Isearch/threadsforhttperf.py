
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
        call(
            " httperf --add-header 'Cookie:SSESSd0b53dd39734cedf16e25bb4ade4ff0b=" + self.sessionvalue + ";SSONAME=Bharadwaj\n' "
                                                                                                         "--ssl --server isearch.asu.edu  --wsesslog 1,0,/home/bhaddy-linux/isearchlog_uri_1.log",
            shell=True)
        print "finished"

create_session=getselenium()
value=create_session.connect_selenium()
print value
length = raw_input("Enter the number of threads")
threads = []
for i in range(0, int(length)):
    thread = httperf_test(str(i),value)
    threads += [thread]
    thread.start()
print"completed"
