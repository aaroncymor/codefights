"""
Let's define a regular brackets sequence in the following way:

    "" is a regular sequence;
    if S is a regular sequence, then (S)is a regular sequence;
    if A and B are regular sequences, then AB is a regular sequence.

Write a function that determines whether the given number is brackety. 
We can the number brackety if its binary form with all 0s substituted by ')'s and all 1s substituted by '(' is a regular brackets sequence.



bracketyNumber(42) = true
4210 = 1010102 => "()()()", which is a regular sequence.

bracketyNumber(58) = false
5810 = 1110102 => "((()()", which isn't a regular sequence.

"""

## This is my old solution but it's is not yet OK.
## This is still wrong
def bracketyNumberOldAndIncorrect(n):
	a = ''
	while n > 1:
		if n % 2 == 0:
			a += '0'
		else:
			a += '1'
		n /= 2
	a += '1'
	bi =  a[::-1]

	if len(bi) % 2 != 0:
		return False
	else:
		j, i = len(bi) - 1, 0
		while i < len(bi)/2:
			s = int(bi[i])
			e = int(bi[j])
			if s == 1:
				if e != 0:
					return False

			elif s == 0:
				if e != 1:
					return False
			i += 1
			j -= 1
	return True

##This one was molded from the solution i got from
## checkio site 1 is '(' and 0 is ')'
def bracketyNumber(n):
	# Convert the number to binary 1 = '(' and 0 = ')'
	a = bin(n)[2:]
	while a:
		#go the Stackless solution for the logic.. ahah
		a0, a = a, a.replace('10', '')
		if a0 == a:
			return False
	return True


##Stack Solution
def checkio(data):
    stack = []  # Yes, we can use deque 
    pairs = {'(': ')', '[': ']', '{': '}'}
    for token in data:
        if token in pairs.keys():
            stack.append(token)
        elif token in pairs.values():
            if stack and token == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    return not bool(stack)

## Stackless Solution
def checkio(expression):
    s = ''.join(c for c in expression if c in '([{}])')
    while s:
    	##This will remove all bracket pairs in a string 
    	##	while there is still char in var s
    	##If there are any left in s, it will be 
    	##	assigned to var s0 so they would be equal and return False
        
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        print "s0:",s0,"s: ",s
        if s == s0:
            return False
    return True

#print checkio("())(()")

##100110

print bracketyNumber(38)
print bracketyNumber(2)