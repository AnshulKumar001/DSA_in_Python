prices = [7,1,5,3,6,4]
n=len(prices)
max_pro=0
for i in range(n):
    for j in range(i+1,n):
        profit=prices[j]-prices[i]
        if profit > max_pro:
            max_pro=profit
print(max_pro)            