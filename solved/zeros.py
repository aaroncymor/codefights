k = {}

def fact(n):
	if n == 0:
		return 1
	elif n in k:
		return k[n]
	else:
		result = n *  fact(n - 1)
		k[n] = result
	return result

def trailing_zeros(str_num):
	if str_num[-1] != '0':
		return 0
	else:
		return trailing_zeros(str_num[:-1]) + 1

def Zeros_Original(N):
	str_num = str(fact(N))
	return trailing_zeros(str_num)



def Zeros_Solution(N):
	"""
	As seen in https://en.wikipedia.org/wiki/Trailing_zeros,
	we can solve this problem by n/5^i or [n/5^1] + [n/5^2] + .... [n/5 ^ n]
	as long as (5 ^ i) <= n
	"""
	i = 1
	result = 0
	while N >= i:
		i *= 5
		result += N/i #Python returns floor of N/i or round down
	return result

print Zeros_Solution(50)