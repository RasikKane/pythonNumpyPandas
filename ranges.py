from math import *
import numpy as np
import time
import numexpr as ne
import unittest

# random Evaluation operation for range
def f(x):
    return 3 * log(x) + cos(x) ** 2

# random Evaluation operation for numpy range
def np_f(x):
    return 3 * np.log(x) + np.cos(x) ** 2

# Evaluation time for numeric expression
def getExpr():
    return '3 * log(np_a) + cos(np_a) ** 2'


# Evaluation time for pythonic range
def pythonRange(a):
    start = time.time()
    r = [f(x) for x in a]
    end = time.time()
    print("Time elapsed with pythonic range is:", end-start)
    return [round(elem, 8) for elem in r]

# Evaluation time for numpy range
def npRange(np_a):
    start = time.time()
    r = np_f(np_a)
    end = time.time()
    print("Time elapsed with Numpy range is:", end-start)
    return [round(elem, 8) for elem in r]

# 1 thread
def nExpr(np_a, thread):
    ne.set_num_threads(thread)
    start = time.time()
    f = getExpr()
    r = ne.evaluate(f)
    end = time.time()
    print("Time elapsed with numexpression [{} threaded] is:{}".format(thread,end-start))
    return [round(elem, 8) for elem in r]

# Unit testing for results ensuring calculations by all types of ranges are correct and essentially same
class rangeUnitTest(unittest.TestCase):
    '''
    In all the below methods, using list comprehension to call the factorial functions and checking equality
    with the elements in the factorial_values list.
    '''
    result = [0.29192658, 2.25261973, 4.27592201, 4.58613307, 4.90877797, 6.29720539, 6.40609906, 6.25949488, 7.42183209]

    def test_pythonRange(self):
        self.assertEqual(pythonRange(range(1, 10)), rangeUnitTest.result)

    def test_npRange(self):
        self.assertEqual(npRange(np.arange(1, 10)), rangeUnitTest.result)

    def test_nExpr1(self):
        self.assertEqual(nExpr(np.arange(1, 10), 1), rangeUnitTest.result)

    def test_nExpr4(self):
        self.assertEqual(nExpr(np.arange(1, 10), 4), rangeUnitTest.result)

# Calling the main function from unittest. This will cause to run all the test_ methods
unittest.main(argv=[''], verbosity=2, exit=False)


# Check performance significance for large ranges such used in data anlytics
loops = 5000000
# Normal range
a = range(1, loops)
# Numpy range
np_a = np.arange(1, loops)

# Call functions to evaluate numeric operations for each type of ranges 
pythonRange(a)
npRange(np_a)
nExpr(np_a,1)
nExpr(np_a, 4)
