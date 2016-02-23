def num_to_eng(n):
	base = {0:"zero",1:"one", 2:"two", 3:"three",
			4:"four",5:"five",6:"six",
			7:"seven",8:"eight",9:"nine",
			11:"eleven", 12:"twelve",13:"thirteen",
			14:"fourteen", 15:"fifteen"
			}
	tens = {10:"ten",20:"twenty",30:"thirty",
			40:"forty",50:"fifty",60:"sixty",
			70:"seventy",80:"eighty",90:"ninety"}

	if n in base.keys():
		return base[n]
	elif n in tens.keys():
		return tens[n]
	else:
		if n > 15 and n < 20:
			b = n % 10
			s = "teen" if b != 8 else "een"
			return num_to_eng(b) + s
		else:
			dm = divmod(n,10)
			return num_to_eng(dm[0] * 10) + "-" + num_to_eng(dm[1])

if __name__ == '__main__':
	for i in range(100):
		print num_to_eng(i)