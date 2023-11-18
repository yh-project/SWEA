T = int(input())

for i in range(T):
    input();cnt = {}
    for j in map(int, input().split()):
        cnt[j] = cnt.get(j, 0) + 1
    print(f"#{i+1} {list(cnt.keys())[list(cnt.values()).index(max(list(cnt.values())))]}")