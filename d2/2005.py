for i in range(int(input())):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N): matrix[j][0] = 1

    for k in range(1, N):
        for l in range(1, N):
            matrix[k][l] = matrix[k-1][l-1] + matrix[k-1][l]
    
    print(f"#{i+1}")
    for m in range(1, N+1):
        print(*matrix[m-1][0:m], sep=" ")