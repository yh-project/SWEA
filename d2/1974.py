for i in range(int(input())):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    # 가로 체크
    for j in range(9):
        if len(set(sudoku[j])) < 9:
                flag = 0
            
    # 세로 체크
    if not flag: print(f"#{i+1} 0"); continue;
    for j in range(9):
            if len(set([sudoku[k][j] for k in range(9)])) < 9:
                flag = 0
        
    # 격자 체크
    if not flag: print(f"#{i+1} 0"); continue;
    row = col = 0
    for j in range(3):
        row = 3*j
        for k in range(3):
            col = 3*k
            if len(set([sudoku[row+l][col+m] for l in range(3) for m in range(3)])) < 9:
                flag = 0 

    if not flag: print(f"#{i+1} 0")
    else: print(f"#{i+1} 1")