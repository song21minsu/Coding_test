import sys
def maxProfit(prices):
    # profit=-sys.maxsize   # 빈배열[] 이 들어오면 output이 -max로 나온다
    profit=0
    min_price=sys.maxsize

    for price in prices:
        min_price=min(min_price,price)
        profit=max(profit,price-min_price)

    return  profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))