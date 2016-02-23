"""
Given an array of integers, find the leftmost number 
that has a decimal representation which doesn't contain 
any digits more than once. If there is no such number, 
return -1 instead.

Example

    For [22, 111, 101, 124, 33, 30], the output should be 124.
    For [1111, 404], the output should be -1.

"""

def differentDigitsNumberSearch(inputArray):

    for i in range(len(inputArray)):
        cur = inputArray[i] ##22
        was = [False] * 10
        ok = True
        while cur > 0:
            if was[cur % 10]:
                ok = False
            was[cur % 10] = True
            cur /= 10
        if ok:
            return inputArray[i]

    return -1
