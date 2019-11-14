N, K = [int(inp) for inp in input().split()]
coins = []
totalCoins = 0

for _ in range(N):
    coins.append(int(input()))

while K!=0:
    for coin in reversed(coins):
        if coin<=K:
            totalCoins += int(K/coin)
            K -= int(K/coin)*coin

print(totalCoins)


