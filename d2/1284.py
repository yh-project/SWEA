for i in range(int(input())):
    P, Q, R, S, W = map(int, input().split())
    A = P*W
    B = Q if W <= R else Q + (W-R) * S
    print(f"#{i+1} {A if A<=B else B}")