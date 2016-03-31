"""
You are given a number N.
Your task is to return a string which represents N! as the product of its prime factors raised to their respective powers.

Example

    factorial_fun(5) = "2(3)*3(1)*5(1)"
    N! = 120 = 2*2*2*3*5
    factorial_fun(6) = "2(4)*3(2)*5(1)"
    N! = 720 = 2*2*2*2*3*3*5
    factorial_fun(20) = "2(18)*3(8)*5(4)*7(2)*11(1)*13(1)*17(1)*19(1)"

    [input] integer N
        2 <= N <= 104.

    [output] string
        The string representing N! as shown in the examples.
"""

def factorial_fun(N):
	if N > 0 and N <= 2:
		return N
	return factorial_fun(N-1) * N

print factorial_fun(5)

#factorial_fun(5-1) * 5
#factorial_fun(4-1) * 4
#factorial_fun(3-1) * 3
#factorial_fun(2-1) * 2
#factorial_fun(1-1) * 1