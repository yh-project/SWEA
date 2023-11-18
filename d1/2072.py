T = int(input())

for i in range(T):
    result = sum([x for x in list(map(int, input().split())) if x % 2 != 0])
    print(f"#{i+1} {result}")