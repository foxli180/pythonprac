'''
Created on May 30, 2013

@author: fox
'''
from multiprocessing import Manager, Process

def f(d,l):
    d[1] = 1
    d['2'] = '2'
    d[0.25] = None
    l.reverse()

def main():
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        p = Process(target = f, args = (d,l))
        p.start()
        p.join()
        print(d)
        print(l) 
        
    
if __name__ == '__main__':main()