def fileNaming(names):
	group = {}
	for i in range(len(names)):
		if names[i] not in group: 
			group[names[i]] = [i,0] #index,occurence

	#Add all occurences in key which has a value of list.
	#Add 1 specifically to e[1] or 2nd element of list everytime
	#it encounters the same file name 
	for key in group:
		for j in range(len(names)):
			if key == names[j]:
				group[names[j]][1] += 1 

	for key in group:
		n = 0
		for k in range(len(names)):
			#If the name is equal to the key and the occurences are more than 1...
			if key == names[k] and group[names[k]][1] > 1:
				temp = names[k]
				names[k] += "("+ str(n) +")" if n > 0 else ""
				#If the newly appended filename is in group
				if names[k] in group and n > 0:
					#If index of the current element is less than the index of the original element
					#We add to the occurences Else, we skip and add 1 again to the file
					if k < group[names[k]][0]:
						group[names[k]][1] += 1
					else:
						n += 1
						names[k] = temp + "("+ str(n) +")" if n > 0 else ""
				n +=1

	return names

print fileNaming(["doc","doc","image","doc(1)","doc"])
print fileNaming(["a(1)","a(6)","a","a","a","a","a","a","a","a","a","a"])
print fileNaming(["a(1)","a(6)","a","a","a","a","a","a(3)","a","a","a","a"])
