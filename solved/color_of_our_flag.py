def colorOfOurFlag(words):
	bindex = 0
	rindex = 0
	blue_list = ['b','l','u','e']
	red_list = ['r','e','d']
	for n in words.lower():
		## Blue
		if n in blue_list and blue_list[bindex] == n:
			bindex += 1
			if bindex == len(blue_list): return "FREE"
	## Red
		if n in red_list and red_list[rindex] == n:
			rindex += 1
			if rindex == len(red_list): return "WAR"

print colorOfOurFlag("ABAbcvalrDFUEsfeFDFCRddeDXX")
print colorOfOurFlag("XCVcRebludcEXBDlXxuECVCD")
