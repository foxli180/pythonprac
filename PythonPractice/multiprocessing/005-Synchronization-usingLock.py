'''
Created on May 30, 2013

@author: fox
can use a lock to ensure that only one process prints to standard output at a time:

'''

from multiprocessing import Process, Lock

def fl(l,i):
    l.acquire()
    print('Hello world', i)
    l.release()

def f(i):
    print('Hello world', i)    

def main():
    lock = Lock()
    
    ps = [Process(target = fl, args =(lock,str(i),)) for i in range(10)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print('-'*20)
    
    ps = [Process(target = f, args =(str(i),)) for i in range(10)]
    for p in ps:
        p.start()    
if __name__ =='__main__':main()