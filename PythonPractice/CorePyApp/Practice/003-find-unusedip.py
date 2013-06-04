'''
Created on Jun 4, 2013

@author: fox
'''
import os, multiprocessing, re



def execmd(ip_4):
    ip = "192.168.2.%s" % ip_4
    if os.sys.platform == "win32":
        #print("win32")
        cmd = "ping %s -n 1" % ip
        patl = "Destination host unreachable" 
    elif os.sys.platform == "linux":
        #print("linux")
        cmd = "ping %s -b -c 1" % ip
        patl = "100% packet loss" 
    else:
        cmd = ""
        patl = ""   
    r = os.popen(cmd)
    result = r.read()
    r.close()
    
    if len(re.findall(patl,result)) != 0:
        #print(ip)
        return ip
    
    
def main():
    #iplist = []
    with multiprocessing.Pool(processes=50) as pool:
        #pool.map(execmd, range(1,254))
        #pool.close()
        #pool.join()
        #print(iplist)
        #sorted(iplist, key= lambda x: int(x.split(".")[3]) )  
        #print(iplist[:])
        #for i in range(1,255):
            #iplist.append(pool.map)
        iplist = pool.map(execmd, range(110,120))
        while None in iplist:
            iplist.remove(None)
            
        sorted(iplist, key= lambda k: int(k.split(".")[3]) )
        print(iplist[:])   
        print(len(iplist))
        
if __name__ =="__main__":main()
               