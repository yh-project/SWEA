P, K = map(int, input().split())
print(P-K+1 if P>=K else 1001-K+P)