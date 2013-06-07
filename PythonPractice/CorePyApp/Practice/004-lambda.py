'''
Created on Jun 7, 2013

@author: fox
'''

x = 10
def foo():
    y = 5 
    bar = lambda y=y: x+y
    print(bar()) #15
    y = 8 
    print (bar()) #15 y defined in lambda
    
def foo2():
    y = 5
    bar = lambda z : z+x
    print(bar(y)) #15
    y = 8         #18   
    print(bar(y))
    
def foo3():
    bar = lambda z : [i for i in range(x+z)]
    print(bar(5))
    print(bar(2))
    
def main():
    foo()
    foo2()
    foo3()
    
if __name__ == "__main__":main()