'''
Created on Jun 3, 2013

@author: fox
'''
from multiprocessing.managers import BaseManager

mgr = BaseManager(address = ('',5000), authkey = b'abc')
srv = mgr.get_server()
srv.serve_forever()


