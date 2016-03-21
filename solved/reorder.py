"""
This is another Reverse Challenge. No description provided. Have fun!

    [input] integer n
        A positive integer

    [input] string word
        A non-empty string consisting of various English letters and symbols.

    [output] string
"""
def Reorder(n, word):
	length = len(word)
	if n == length:
		return word
	elif n < length:
		return word[n:] + word[:n]
	else:
		if n % length == 0:
			return n
		else:
			while n > length:
				n = n - length
			return word[n:] + word[:n]

print Reorder(9,"mind")
print Reorder(5,"WorldHello")
print Reorder(4,"rainT")
print Reorder(2,"ha")
print Reorder(5,"breakfast")