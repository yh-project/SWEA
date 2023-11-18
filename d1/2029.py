for i in range(int(input())):
    n1, n2 = map(int, input().split())
    print(f"#{i+1} {n1//n2} {n1%n2}")