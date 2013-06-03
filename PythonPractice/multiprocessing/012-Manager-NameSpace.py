'''
Created on Jun 3, 2013

@author: fox

this is diff with executing from shell step by step , unknown why!

Found: should be Namespace not NameSpace

'''
import multiprocessing 


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    #ns = manager.NameSpace() # fail
    ns = mgr.Namespace()
    ns.x = 10
    ns.y = 'Hello'
    ns._z = 12.3
    print (ns)