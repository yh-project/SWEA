T = int(input())

for i in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    while(True):
        tmp = prices[0:prices.index(max(prices))+1]
        prices = prices[prices.index(max(prices))+1:]
        profit += sum([tmp[-1]-j for j in tmp])
        if len(prices) == 0 or len(tmp) == 0: break
    print(f"#{i+1} {profit}")