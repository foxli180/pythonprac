'''
Created on May 26, 2013

@author: fox
'''
import signal 
import threading
import os
import time

def signal_handler(num,stack):
    print('Recieved signal %d in %s' % \
          (num, threading.currentThread().name))
    
signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
    print('Waiting signal in', threading.currentThread().name)
    signal.pause()
    print('Done Waiting')
    

receiver =  threading.Thread(target = wait_for_signal, name = 'receiver')
receiver.start()
time.sleep(0.1)

def send_signal():
    print('Sending signal in', threading.currentThread().name)
    os.kill(os.getpid(),signal.SIGUSR1)

sender = threading.Thread(target = send_signal, name ='sender')
sender.start()
sender.join()

print('waitting for', receiver.name)
signal.alarm(3)
receiver.join()
