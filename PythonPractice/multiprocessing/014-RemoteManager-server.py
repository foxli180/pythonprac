'''
Created on Jun 3, 2013

@author: fox
'''
from multiprocessing.managers import BaseManager
import queue 

queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_queue', callable=lambda:queue)

def main():
    m = QueueManager(address=('159.99.249.57', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()

if __name__ =='__main__':main()