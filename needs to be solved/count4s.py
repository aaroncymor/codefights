"""
http://www.geeksforgeeks.org/count-numbers-from-1-to-n-that-have-4-as-a-a-digit/
Find the total number of times digit 4 occurs in the range [0,n).

Example:

    For n = 14, the output should be
    Count4s(n) = 1.
    The only time 4 appears is in number 4.
    For n = 15, the output should be
    Count4s(n) = 2.
    4 appears in 4 and 14.
    For n = 44, the output should be
    Count4s(n) = 8.
    For n = 45, the output should be
    Count4s(n) = 10.

"""
def Count4s(n):
	counter = 0
	for i in range(1,n):
		while i != 0:
			if i % 10 == 4:
				counter += 1
			i /= 10
	return counter

print Count4s(1000000000)