'''
Created on May 30, 2013

@author: fox
from user manual 
'''
from multiprocessing import Pool
import multiprocessing

def satr_process():
    print('starting processing : ', multiprocessing.current_process().name)


def f(x):
    return x*x

def main():
    p = Pool(4,initializer = satr_process,maxtasksperchild = 3)
    output = p.map(f,[1,2,3,4,5,6,7,8,9,10,11])
    print(output)
    
if __name__ == '__main__':main()