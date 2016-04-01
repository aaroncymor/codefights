"""
You are given 4 integers, a, b, c and d. Let k be equal to (a2 + b2) * (c2 + d2).

Find all possible ways to represent k as i2 + j2, such that i and j are positive integers, i <= j, and return all such pairs [i, j] in an array.

Example

For a = 1, b = 2, c = 3 and d = 4, the answer is
rewriteTheProduct(a, b, c, d) = [[2,11],[5,10]].

k = (12 + 22) * (32 + 42) = 5 * 25 = 125. It is possible to represent 125 as 22 + 112 and 52 + 102, so the answer is [[2,11],[5,10]].

    [input] integer a

    Any integer value.

    [input] integer b

    Any integer value.

    [input] integer c

    Any integer value.

    [input] integer d

    Any integer value.

    [output] array.array.integer

    A two-dimensional array containing all possible representations sorted by the first elements.

"""
def rewriteTheProduct(a,b,c,d):
	k = (a**2 + b**2) * (c**2 + d**2)
	answers = []
	i = 2
	while i**2 < k:
		j = 2
		while j**2 < k:
			if (i**2 + j**2) == k:
				answers.append([i,j])
			elif (i**2 + j**2) > k:
				break
			j += 1

		if len(answers) == 2:
			return answers
		else:
			i += 1

print rewriteTheProduct(1,2,3,4)
print rewriteTheProduct(1,-3,5,7)
print rewriteTheProduct(2,4,6,8)