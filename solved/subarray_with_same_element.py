"""
Given an array of positive integers a and an integer k, 
find the first and last index of the longest subarray of a 
that consists only of k. If the array contains multiple 
subarrays of the same length, return indices of the last one. 
If k doesn't exist in a, return [-1,-1]

Example:

    For a = [2,1,1,1,1,3,3,4,5,1,1,1] and k = 3 the answer is
    findSubArrayWithSameElement(a, k) = [5,6].
    The longest subarray of a that contains 3s starts at index 5 and ends at index 6.

    For a = [2,1,1,1,1,3,3,4,5,1,1,1,1] and k = 1 the answer is
    findSubArrayWithSameElement(a, k) = [9, 12].
    There are two subarrays of 1, and they have equal length. One goes from index 1 to 4, and another one from index 9 to 12. The answer should be [9,12] as it is last to occur.

    For a = [1, 2, 3] and k = 9 the answer is
    findSubArrayWithSameElement(a, k) = [-1, -1]
"""

def findSubArrayWithSameElement(a,k):
	ctr, largest, start, kstart_ctr, end = 0,0,0,0,0
	coordinates = [-1,-1]
	for i in range(len(a)):
			if a[i] == k:
				ctr += 1
				if kstart_ctr == 0:
					start = i
					kstart_ctr +=1

				if (i + 1) < len(a):
					if a[i + 1] != k:
						if largest <= ctr:
							largest,end = ctr,i
							coordinates = [start,end] 
						ctr,kstart_ctr = 0,0
				elif i == len(a) - 1:
					if largest <= ctr:
						largest, end = ctr,i
						coordinates = [start,end] 
	return coordinates

print findSubArrayWithSameElement([2,1,1,1,1,3,3,4,5,1,1,1,],1)