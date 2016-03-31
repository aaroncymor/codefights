"""
You are given a string s composed of letters and numbers, which was compressed with some algorithm. Every letter in s is followed by a number (possibly with leading zeros), which represents the number of times this letter occurs consecutively. For example, "aaaaaaaabbbbbbcc" would be given as "a8b6c2".

<img src="https://i.gyazo.com/debe8416069b0c3c6394935e81d62586.png" width=600px>

Decompress s, sort its letters and return the kth (1-based) letter of the obtained string.

Note: each letter occurs in s no more than 251 times.

Example

Expand_It("a2b3c2a1", 2) = "a"

The decompressed s equals "aabbbcca", and once sorted it becomes "aaabbbcc". Its second 1-based letter is 'a', which is the answer.

    [input] string s

    The compressed string, 2 <= s.length <= 104.
    The length of the decompressed string is no greater than 1018.

    [input] integer k

    A non-negative integer, the 1-based index of the letter to return. If the length of the decompressed string is less than k, return "-1" instead.

    [output] string

    The kth letter of the decompressed string, or "-1" if it does not exist.


"""

def Expand_It(s,k):
	d = {}
	length = len(s)
	i = 0
	temp = ''
	entered_j = False
	while i < length-1:
		if not s[i].isdigit():
			if s[i] not in d:
				d[s[i]] = 0
			temp = s[i]
			i += 1
		else:
			n = ""
			for j in range(i,len(s)):
				if s[j].isdigit():
					n += s[j]
				else:
					d[temp] += int(n)
					i = j
					break
				if j == len(s) - 1:
					entered_j = True
					d[temp] += int(n)
					i = j
	if not entered_j:
		d[temp] += int(s[i:])

	for char in sorted([c for c in d.keys()]):
		k -= d[char]
		if k <= 0:
			return char
	return -1

print Expand_It("a2b3c2a1",100)
print Expand_It("a2b3c2a1",2)
print Expand_It("a2b3c2a1",5)
print Expand_It("a2b3c2a1",1)
print Expand_It("a2b3c2a1",8)
print Expand_It("r000000000023801d231636249w323f800501940d8264r289578380y000011937c156850795r21002q72102976l6063t45523262o00000024696f505882808m377q334615650l3008y115534560x000000000023615x623773644q18277c325237380v15157l61023501x00012650p981150420l24910s9769903j10027r25000320m0000011416c188379632s15260u359792512f17334b353414596m000018540f83202408s18182q65743212n6335e215003310y00030512n408955788g32281n148019018p6374o403233149",774270049)




