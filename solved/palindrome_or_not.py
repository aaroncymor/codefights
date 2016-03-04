"""
Find out if the given string is a palindrome or not.
If s is a palindrome return "Yes", otherwise return "No".

Example:

    PalindromeOrNot("aba") = "Yes"
    PalindromeOrNot("abb") = "No"

    [input] string s
        A string of lowercase English letters, 0 ≤ s.length ≤ 300.

    [output] string
        Either "Yes" or "No".
"""


def PalindromeOrNot(s):
	i,j = 0,-1
	while i < len(s) / 2:
		if s[i] != s[j]:
			return "No"
		i += 1
		j -= 1
	return "Yes"