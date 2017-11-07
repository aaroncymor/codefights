"""
Given positive integer numbers a, b and n return the maximum number that can be obtained by lengthening number a repeatedly no more than n times.

Lengthening number a means appending exactly one digit (in the decimal notation) to the right hand side of a such that the resulting number is divisible by number b. If it is impossible to obtain a number that is divisible by b, then the lengthening operation cannot be performed.

Example

For a = 12, b = 11 and n = 2, the output should be
addDigits(a, b, n) = "1210".

Lengthening operations can be 12->121->1210.
"""
def addDigits(a, b, n):
    ans = a
    end = False
    for i in range(n):
        a = (a * 10) + 9
        for j in range(10):
        	#print(a)
        	if a % b == 0:
        		ans = a
        		#print("ans",ans)
        		break
        	a = a - 1
        	#print("j",j)
        	if j == 9:
        		end = True
        if end == True:
        	break
    return ans


print(addDigits(12,11,2))
print(addDigits(4,13,10))
print(addDigits(4,3,9))
print(addDigits(412,11,4))