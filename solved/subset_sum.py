import itertools

def SubsetSum(ARR,SUM):
	count = 0 if SUM != 0 else 1
	for i in range(1,len(ARR)+1):
		combs = itertools.combinations(ARR,i)
		for comb in combs:
			if sum(comb) == SUM:
				count += 1
	return count

print SubsetSum([1, 2, 3, 4, -5], 0)

#USING ITERTOOLS
def GetCombinationsForSum(ARR,SUM):
	answers = []
	for i in range(1,len(ARR)+1):
		combs = itertools.combinations(ARR,i)
		for comb in combs:
			if sum(comb) == SUM:
				answers.append(comb)
	return answers

#COMBINATIONS THE HARD WAY
def choose_iter(elements,length):
	for i in xrange(len(elements)):
		if length == 1:
			yield (elements[i],)
		else:
			#print elements[i],elements[i+1:len(elements)],length-1
			for next in choose_iter(elements[i+1:len(elements)],length-1):
				#print next
				yield (elements[i],) + next

def choose(l,k):
	return list(choose_iter(l,k))

#print list(choose_iter("abcde",4))
