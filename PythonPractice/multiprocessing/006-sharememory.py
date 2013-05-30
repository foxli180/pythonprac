'''
Created on May 30, 2013

@author: fox

share memory using Value and Array
'''

from multiprocessing import Value, Array, Process

def f(n,a):
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] = -a[i]
    
def main():
    num = Value('d' ,0.0)
    arr = Array('i', range(10))
    print (num.value)
    print(arr[:])
    p = Process(target = f, args = (num,arr,))
    p.start()
    p.join()
    print (num.value)
    print(arr[:])
    
if __name__ == '__main__':main()
    