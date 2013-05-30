'''
Created on May 30, 2013

@author: fox
'''

from multiprocessing import Process    
import os


def info(title):
    print(title)
    print('module name: ', __name__)
    
    if hasattr(os,'getppid'):
        print('Parent Process : ', os.getppid())
    print('process ID: ', os.getpid())

def f (name):
    info('function f')
    print('Hello', name)
    
def main():
    info('main line')
    p = Process(target = f,args=('Fox',))
    p.start()
    p.join()

if __name__ == '__main__':main()
    
    