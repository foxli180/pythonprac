'''
Created on Jun 3, 2013

@author: fox
'''

from multiprocessing.managers import BaseManager


class MathCls:
    
    def add(self,x,y):
        return x+y
    
    def mul(self,x,y):
        return x*y

class MyManager (BaseManager):
    pass

MyManager.register('Maths', MathCls)

def main():
    with MyManager() as manager:
        maths = manager.Maths()
        print(maths.add(3,4))
        print(maths.mul(3,4))

if __name__ == '__main__':main()
