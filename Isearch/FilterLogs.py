import re
itit=raw_input("enter the number of iterations")
for i in range(0,int(itit)):
    regex = "^(uri=\")"
    dest='/home/bhaddy-linux/Downloads/isearchlog_uri_1_itit.log'
    log='/home/bhaddy-linux/Downloads/isearchlog.txt'
    g = open(dest, 'a')
    f = open(log, 'r')
    last="\n"
    for line in f:
        word = line.split()
        uri = word[8].split("uri=\"")
        urireplace = uri[1].strip("\"")+'\n'
        #print urireplace
        g.write(urireplace)
    print i
    i=i+1
print("*******completed***********")
g.close()
f.close()



