"""Write a python program to find number of occurrences of each character in a given string.

For eg. If "Linkedin" is input then output should be :
l=1
i=2
n=2
k=1
e=1
d=1
"""

import timeit
import_module = "import random"

testcode1 = ''' 
def code1():
    test_string = "linkedin"
    for i in sorted(set(test_string), key=test_string.index):
        print(i, test_string.count(i))
'''

testcode2 = ''' 
def code2():
    test_string = "linkedin"
    test_string = test_string.lower()
    d = {}
    for i in test_string:
        d[i] = 0
    for i in test_string:
        d[i] = d[i] + 1          
    for (k, v) in d.items():
        print(k, v)
'''

print(timeit.timeit(stmt=testcode1, setup=import_module)) # typically slower: 0.0426984
print(timeit.timeit(stmt=testcode2, setup=import_module)) # typically faster : 0.0401631
