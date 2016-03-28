"""
Fibonacci sequence is defined as follows:
F1 = 0, F2 = 1. For each i > 2: Fi = Fi - 1 + Fi - 2.
So the sequence starts with 0,1,1,2,3,5,8,13, ....

Your goal is to find the last digit of the nth number in this sequence, i.e. find F(n) mod 10.

Example

    LastFibDigit(1) = F(1) mod 10 = 0 mod 10 = 0
    LastFibDigit(2) = F(2) mod 10 = 1 mod 10 = 1
    LastFibDigit(8) = F(8) mod 10 = 13 mod 10 = 3
"""

def LastFibDigit(n,c={}):
    if n > 0:
        if n == 1:
            return 0
        elif 1 < n < 4:
            return 1
    if n not in c:
        r = LastFibDigit(n-2,c) + LastFibDigit(n-1,c)
        c[n] = r % 10
    return c[n]
"""
print LastFibDigit(1)
print LastFibDigit(2)
print LastFibDigit(3)
print LastFibDigit(4)
print LastFibDigit(5)
print LastFibDigit(6)
print LastFibDigit(7)
print LastFibDigit(8)
print LastFibDigit(9)
print LastFibDigit(10)
print LastFibDigit(11)
print LastFibDigit(12)
print LastFibDigit(13)
print
print LastFibDigit(121)
print LastFibDigit(122)
print LastFibDigit(123)
print LastFibDigit(124)
print LastFibDigit(125)
print LastFibDigit(126)
print LastFibDigit(127)
print LastFibDigit(128)
print LastFibDigit(129)
print LastFibDigit(130)
print LastFibDigit(131)
print LastFibDigit(132)
print LastFibDigit(133)
"""