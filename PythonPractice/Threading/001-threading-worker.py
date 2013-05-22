'''
Created on May 22, 2013

@author: fox
'''

import threading
import time

def worker(num):
    print(time.ctime())
    print('Worker: '+ str(num))
    time.sleep(2)
    print(time.ctime())
    
ths = [threading.Thread(target = worker, args=(i,)) for i in range(5)]

for th in ths:
    th.start()
for th in ths:
    th.join()
    
    1