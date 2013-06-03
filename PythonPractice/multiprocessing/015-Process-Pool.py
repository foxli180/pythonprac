'''
Created on Jun 3, 2013

@author: fox
'''
from multiprocessing import Pool
import multiprocessing

def f(x):
    return x*x

def main():
    with Pool(processes = 4) as pool:
        result = pool.apply_async(f,(10,))
        print(result.get(timeout=1))
        print(pool.map(f, range(10)))
        it = pool.imap(f, range(10))
        print(next(it))
        print(next(it))
        print(it.next(timeout=1))
        import time
        result = pool.apply_async(time.sleep,(10,))
        try:
            print(result.get(timeout=1))
        except multiprocessing.TimeoutError as terror:
            print(terror)
        finally:
            print('Done')
        
if __name__ =='__main__':main()