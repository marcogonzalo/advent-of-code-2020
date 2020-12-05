import functools 
import input

def entries_that_sum_2020(arr):
    n = len(arr)
    for a in range(n):
        for b in range(a+1,n):
            rest = 2020 - (arr[a] + arr[b])
            for c in range(b+1,n):
                if arr[c] == rest:
                    return arr[a], arr[b], arr[c]
    return false

values = entries_that_sum_2020(input.values)
print("2020 =", " + ".join(str(x) for x in values))
print("Product:", functools.reduce(lambda a,b : a*b, values)) 