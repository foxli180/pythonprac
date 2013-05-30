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

def procResult(result):
    #pat1 = 'No ARP Entries Found.'
    pat1 = '\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}'
    Mac = re.findall(pat1,result)
    if len(Mac) == 0:
        return False
    return Mac[0]

def getpanelID():
    x = []
    try:
        with open('Panels.txt','r') as f:
            for line in f:
                (MAC,PID) = line.split()
                #x[MAC]=PID
                x.append([PID,MAC])

    except IOError as err:
        print('File Error: '+err)


    return x


    

if __name__ == '__main__':
    os.popen('arp -d')
    s = []
    count = 0
    #os.popen('ping 192.168.8.1 -n 1')
    for x in range(1,56):
        ip = '192.168.8.%d' %x
        cmd1 = 'arp -a %s' %ip
        cmd2 = 'ping %s -n 1' %ip
        result2 = execCmd(cmd2)
        #print(result2)
        result1 = execCmd(cmd1)        
        Mac = procResult(result1)
        if Mac:
            Mac = 'MAC'+Mac.replace('-','').upper()
            x = getpanelID()
            for y in x:
                if Mac in y:
                    y.append(ip)
                    s.append(y)
            count = count +1
    s=sorted(s)      
    print ("total panel: " +str(count))
    print ('PanelID'+'\t\t'+'MacAddress'+'\t\t\t'+'IPAddress ')
    print ('-'*70)
    for eachpanel in s:
        #pass
        print(eachpanel[0]+'  |\t'+eachpanel[1]+'  |\t\t'+eachpanel[2])

    if (len(s)) < 31:
        m = []
        print ("\nOffline Panel: \n")
        for eachpanel in s:
            m.append(eachpanel[0])
        for i in range(1,10):
            pid = 'Panel-'+'0'+str(i)
            if pid not in m:
                print(pid)
        for i in range(11,32):
            pid = 'Panel-'+str(i)
            if pid not in m:
                print(pid)
