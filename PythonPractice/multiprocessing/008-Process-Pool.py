'''
Created on May 30, 2013

@author: fox
'''

from multiprocessing import Pool

def f(x):
    return x*x

def main():
    with Pool(processes = 4) as pool:
        result = pool.apply_async(f,[10])
        print (result.get(timeout = 1))
        print (pool.map(f, range(10)))
 
if __name__ =='__main__':main()        