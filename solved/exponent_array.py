"""
Write an algorithm that creates a sorted array of positive numbers' squares, such that its maximum element isn't greater than n.

Example:

exponentArray(10) = [1, 4, 9]

    [input] integer n
        0 <= n <= 10^7

    [output] array.integer
        A sorted array of squares.

"""

def exponentArray(n):
	e = []
	i = 1
	while True:
		if i * i <= n:
			print i * i
			e.append(i * i)
		else: return e
		i += 1

print exponentArray(81)
