'''
Created on Jun 3, 2013

@author: fox
'''
from multiprocessing import Process,freeze_support

def f():
    print('Hello World')

def main():
    freeze_support()
    Process(target =f).start()
    
if __name__ =='__main__':main()