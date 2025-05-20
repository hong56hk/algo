# Given a list (vector), write a function "partial_reverse(a,i,j)"

def partial_reverse(a,i,j):
    data = []
    for idx in range(0,i,1):
        data.append(data[i])
        