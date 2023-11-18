T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        count = 0
        # 행검사
        for j in range(n):
            if puzzle[i][j] == 1:
                count += 1
            if puzzle[i][j] == 0 or j == n-1:
                if count == k:
                    answer += 1
                count = 0
                 
        # 열검사
        for j in range(n):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == n-1:
                if count == k:
                    answer += 1
                count = 0                
    print(f"#{test_case} {answer}")