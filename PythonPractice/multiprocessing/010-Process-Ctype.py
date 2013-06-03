'''
Created on Jun 3, 2013

@author: fox

for the s = Array('c', 'hello world', lock = lock)
there is defect in Python 3.0
http://bugs.python.org/issue17991
'''
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double


class Point(Structure):
    _fields_ = [('x',c_double),('y',c_double)]
    
def modify(n,x,A):
    n.value **= 2
    x.value **= 2
    #s.Value = s.Value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2

def main():
    lock = Lock()
    n = Value('i', 7)
    x = Value(c_double, 1.0/3.0, lock = False)
    #s = Array('u', 'hello world', lock = lock)
    #s = Array('c', 'hello world', lock = lock)
    A = Array(Point,[(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock = lock)
    #A = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)

    p = Process(target = modify, args = (n,x,A,))
    p.start()
    p.join()
    
    print(n.value)
    print(x.value)
    #print(s.Value)
    print([(a.x,a.y) for a in A])
    
if __name__ =='__main__':main()
    