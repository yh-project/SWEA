for i in range(int(input())):
    n1, n2 = map(int, input().split())
    print(f"#{i+1} {'<' if n1<n2 else '>' if n1>n2 else '='}")
