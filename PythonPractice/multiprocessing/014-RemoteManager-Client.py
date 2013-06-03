'''
Created on Jun 3, 2013

@author: fox
put message
'''
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): 
    pass


QueueManager.register('get_queue')
def main():
    m = QueueManager(address=('159.99.249.57', 50000), authkey=b'abracadabra')
    m.connect()
    queue = m.get_queue()
    #time.sleep(2)
    queue.put('hello2')
    
if __name__ == '__main__':main()