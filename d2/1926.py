for i in range(1, int(input())+1):
    tmp = sum([1 for c in list(str(i)) if int(c) != 0 if int(c) % 3 == 0])
    if tmp > 0: print("-"*tmp, end=" ")
    else: print(i, end=" ")