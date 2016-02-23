"""
Let's call some element of the given array A bad if it equals 0 and 
there are no good (i.e. not bad) elements in the array before or 
after it.

Remove all bad elements from array A and then return it.

Example

    removeBadMembersfor([0, 9, 0, 4]) = [9, 0, 4]
    removeBadMembersfor([0, 9, 5, 0, 0, 0, 0, 2, 0, 0]) = [9, 5, 0, 0, 0, 0, 2]
    removeBadMembersfor([1, 6, 0, 2]) = [1, 6, 0, 2]

"""

def removeBadMembers(A):
    B = A
    a,b = 0, 0
    while True:
        i = 0
        if A[i] == 0:
            del A[i]
        else:
            if a == 0:
                a += 1

        j = len(A) - 1

        if A[j] == 0:
            del A[j]
        else:
            if b == 0:
                b += 1

        if b == 1 and a == 1:
            break

        if a == 0:
            i += 1
        if b == 0:
            j -=1
    return A
            
        
print removeBadMembers([0,0,9,0,1,0,0])