N = int(input())
print(*[num for num in range(1, N+1) if N % num == 0], sep=" ")