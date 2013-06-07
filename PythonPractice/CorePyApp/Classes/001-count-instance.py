'''
Created on Jun 7, 2013


@author: fox

method howmany return how many instances of class have been created

'''

class InstCt(object):
    
    count = 0 # a class member
    
    def __init__(self): # add count when initialize an object
        InstCt.count += 1
    
    def __del__(self): # reduce count when object destroyed
        InstCt.count -= 1
        
    def howmany(self):
        return InstCt.count
    


def main (): 
    a = InstCt()
    b = InstCt()
    print(a.howmany())
    print(b.howmany())
    del a
    #print(a.howmany())
    print(b.howmany())
    del b
    print(InstCt.count)
    
if __name__ == "__main__":main()    