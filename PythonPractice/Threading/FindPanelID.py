'''
Created on May 28, 2013

@author: fox
'''
import os,re

def execCmd(cmd):
    r= os.popen(cmd)
    text = r.read()
    r.close()
    return text

for x in range(1,55):
    ip = '192.168.1.%d' %x
    cmd1 = 'arp -a %s' %ip
    cmd2 = 'ping %s -n 1' %ip
    result2 = execCmd(cmd2)
    print(result2)
    #result1 = execCmd(cmd1)        