T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N): matrix.append(list(map(int, input().split())))
    row = col = 0 # row, col
    result = 0
    for _ in range(N-M+1):
        for _ in range(N-M+1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += matrix[row+k][col+l]
            if tmp > result: result = tmp
            col += 1
        row += 1
        col = 0
    print(f"#{i+1} {result}")