def SortByGuide(a,guide):
	sort_a = []
	sort_guide = []
	index = []
	for i in range(len(a)):
		if guide[i] != -1:
			sort_a.append(a[i])
			sort_guide.append(guide[i])
			index.append(i)

	restart = False
	i = 0
	while True:
		if (i + 1) < len(sort_guide):
			if sort_guide[i] > sort_guide[i + 1]:
				temp = sort_guide[i + 1]
				sort_guide[i + 1] = sort_guide[i]
				sort_guide[i] = temp

				temp = sort_a[i + 1]
				sort_a[i + 1] = sort_a[i]
				sort_a[i] = temp

				restart = True
		if restart and i == len(sort_guide) - 1:
			restart = False
			i = 0
		elif not restart and i == len(sort_guide) - 1:
			break
		else:
			i += 1

	for i in range(len(index)):
		a[index[i]] = sort_a[i]
	return a

print SortByGuide([27, 67, 80, 38, 21],[2, 5, 3, 1, 4])
print SortByGuide([70, 10, 15, 800, 400, 4, 225, 438, 509, 1000],[6, 1, 4, -1, -1, 2, -1, -1, 5, 3])
print SortByGuide([700, 800, 400, 100, 900, 325],[2, -1, 1, -1, 3, -1])
print SortByGuide([2, 5, 3, 1, 4, 70, 8],[2, 5, 1, 3, -1, 4, -1])
print SortByGuide([45, 56, 78],[-1, 2, 1])
print SortByGuide([56, 78, 3, 45, 4, 66, 2, 2, 4],[3, 1, -1, -1, 2, -1, 4, -1, 5])