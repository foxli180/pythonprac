'''
Created on May 30, 2013

@author: fox
2 way of object exchange in process
1st is Queue
'''

from multiprocessing import Queue, Process

def f(q):
    q.put([43,None,'Hello'])
    
def main():
    q = Queue()
    p = Process(target = f, args = (q,))
    p.start()
    print(q.get())
    # if you comment this line you can get the result after join
    p.join()
    print('cannot get anything after join')
    print(q.get())
    
if __name__ =='__main__':main()