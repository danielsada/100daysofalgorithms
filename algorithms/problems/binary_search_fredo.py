"""
Fredo is assigned a task today. He is given an array A containing N integers.
His task is to update all elements of array to some minimum value x, that is, A[i] = x, 1 <= i <= N
such that product of all elements of this new array is strictly greater than the
product of all elements of the initial array.

Note that x should be as minimum as possible such that it meets the given condition.
Help him find the value of .

Input Format:
The first line consists of an integer  N, denoting the number of elements in the array.
The next line consists of  space separated integers, denoting the array elements.

Output Format:
The only line of output consists of value of .
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


def binary_multiply(low, high, N, mult):
    if low+1 == high or low == high:
        return low
    else:
        mid = low + ((high - low) // 2)
        pw = mid ** N
        if pw > mult:
            return binary_multiply(low, mid, N, mult)
        else:
            return binary_multiply(mid, high, N, mult)


from functools import reduce
import math

N = int(input())
A = list(map(int, input().split(" ")))
p = 1

for elems in A:
    p *= elems**(1/N)

if p == 1:
    p += 1
print(math.ceil(p))
