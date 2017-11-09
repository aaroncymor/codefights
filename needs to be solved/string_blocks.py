def stringBlocks(sentence, n):
	maxi, cocktail = 0, []
	words = str.split(sentence)
	for word in words:
		sub_cocktail = []
		count = 0
		for i in range(0, len(word), n):
			sub_cocktail.append(word[i:i+n])
			count += 1
		cocktail.append(sub_cocktail)

		if count > maxi:
			maxi = count

	wat = [''] * maxi

	for sub_cocktail in cocktail:
		for i in range(len(sub_cocktail)):
			wat[i] += sub_cocktail[i] + ' '

	#Not yet finished
	#Need spaces
	return wat
	#for sub_cocktail in cocktail:
	#	for jib in sub_cocktail:


print(stringBlocks("This is example one", 3))