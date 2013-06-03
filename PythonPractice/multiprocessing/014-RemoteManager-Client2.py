'''
Created on Jun 3, 2013

@author: fox
'''
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
     pass


QueueManager.register('get_queue')

def main():
    m = QueueManager(address=('159.99.249.57', 50000), authkey=b'abracadabra')
    while True:
        m.connect()
        queue = m.get_queue()
        print(queue.get())

if __name__ =='__main__':main()
