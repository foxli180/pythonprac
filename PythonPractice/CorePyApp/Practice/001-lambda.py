'''
Created on May 27, 2013

@author: fox
'''


''' 
lambda used in key of sorting date 
'''
import random 
x = []
for i in range(100):
    x.append('192.168.1.'+str(i))
    
random.shuffle(x)
for m in x:
    print(m)
    
''' 
now i want to sort x var last number
simply using sort or sorted can not solve the problem
'''
sortx = sorted(x)
print ('\n---------------------------------\n')
for m in sortx:
    print(m)
    

'''
using lambda to solve it, now we can get the expected result
'''
sorty = sorted(x, key = lambda k: int(k.split('.')[3]))

print ('\n----------------------------------\n')
for m in sorty:
    print(m)


'''
another way to use lambda
'''

alist = [1,2,3,4,5,6,7,8,9,]
low = 3
high = 7

t = filter(lambda x: high>x>low, alist)
print(list(t))

'''
using list express to do same as lambda
'''
t2 = [item for item in alist if high>item>low]
print (t2)

