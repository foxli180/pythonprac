'''
Created on Jun 3, 2013

@author: fox
'''

def f():
    for i in range(10):
        yield i*i
        
def main():
    it = f()
    m = 0
    for i in it:
        
        print(str(m),i)
        m = m+1
    '''
    print(next(it))
    print(next(it))
    print(next(it))
    '''
    print(list(it))

if __name__=='__main__':main()