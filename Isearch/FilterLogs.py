import re

regex = "^(uri=\")"
dest='/home/bhaddy-linux/Downloads/isearchlog_uri_1.log'
log='/home/bhaddy-linux/Downloads/isearchlog.txt'
g = open(dest, 'a')
f = open(log, 'r')
last="\n"
for line in f:
    word = line.split()
    uri = word[8].split("uri=\"")
    urireplace = uri[1].strip("\"")+'\n'
    print urireplace
    g.write(urireplace)
print("*******completed***********")
g.close()
f.close()



