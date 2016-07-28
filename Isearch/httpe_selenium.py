from user_input import User_input

class getselenium:

    def connect_selenium(self):
        x=User_input()
        cookies=x.connect()
        print "here"
        session1=[]
        session1=cookies[6]
        print session1
        self.sessionvalue=session1['value']
        return self.sessionvalue

