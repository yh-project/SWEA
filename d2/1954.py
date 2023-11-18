T = int(input())

for i in range(T):
    N = int(input())
    print(f"#{i+1}")
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)] # x, y
    result = [[0 for _ in range(N)] for _ in range(N)]
    idx = num = 0
    point = (0, 0) # x, y

    for j in range(1, N**2+1):
        # num += 1
        num += 1
        # 찍고
        result[point[1]][point[0]] = num
        # 이동이 가능한지 검증
        if(not(0<=point[0]+dir[idx][0]<N and 0<=point[1]+dir[idx][1]<N) or result[point[1]+dir[idx][1]][point[0]+dir[idx][0]] != 0):
            # 불가능 -> idx = (idx+1)%4
            idx = (idx+1)%4
        # 이동
        point = (point[0]+dir[idx][0], point[1]+dir[idx][1])
        
    for k in range(N):
        print(*result[k], sep=" ")        