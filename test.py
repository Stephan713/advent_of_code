def strictly_increasing(L):
    return [x<y and (1 <= abs(x-y) <= 3)  for x, y in zip(L, L[1:])]


print(strictly_increasing([1,2,8,4,5]))