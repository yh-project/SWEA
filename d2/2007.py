for i in range(int(input())):
    str = input()
    flag = 1
    for j in range(1, 11):
        if not flag: continue
        tmp = set([str[k:k+j] for k in range(0, 30-j, j)])
        if len(tmp) == 1:
            print(f"#{i+1} {len(list(tmp)[0])}"); flag = 0;