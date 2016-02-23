def arrayMode(sequence):
    c,l,x,can = 0,0,list(set(sequence)),0
    for i in range(len(x)):
        for j in range(len(sequence)):
            if x[i] == sequence[j]:
                c += 1
        if l < c:
            l,c,can = c,0,x[i]
    return can

print arrayMode([1,3,3,3,1,2,2,2,5,5,5,5,5,5])