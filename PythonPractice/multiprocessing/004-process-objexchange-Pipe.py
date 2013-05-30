'''
Created on May 30, 2013
2 way of object exchange in process
2nd is Pipe
@author: fox
'''

from multiprocessing import Pipe, Process

def f(conn):
    conn.send([42,None,'Hello'])
    conn.close()
    
def main():
    parent_conn, child_conn = Pipe()
    p = Process(target = f, args=(child_conn,))
    p.start()
    # if you comment this line you can get the result after join
    print(parent_conn.recv())
    p.join()
    print('Hello: ', parent_conn.recv())
    
if __name__ == '__main__':main()