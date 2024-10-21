n = int(input())
prices = [int(input()) for i in range(n)]
prices.sort(reverse=True)
total=sum(prices)
for i in range(2, len(prices), 3):
    total-=prices[i]
print(total)