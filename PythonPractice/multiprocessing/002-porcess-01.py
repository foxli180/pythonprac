'''
Created on May 30, 2013

@author: fox
from user manual

join --- main process will wait for the sub process terminate to continue 

'''

from multiprocessing import Process

import time 

def say_hello(name):
    print('Hello : ', name)
    time.sleep(3)
    print('Hello again: ', name)

def main():
    p = Process(target = say_hello, args = ('Fox',))
    p.start()
    print('not join!')
    p.join()
    print('joined')
    
if __name__ == '__main__':main()



