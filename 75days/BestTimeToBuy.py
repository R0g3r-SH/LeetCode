def maxProfit(prices):

    buy = 0
    sell = buy+1

    if len(prices) == 0 :
        return 0

    rev = 0
        

    while sell < len(prices):
        valbuy = prices[buy]
        valsell = prices[sell]

        if valbuy<=valsell:
            currev = valsell - valbuy
            rev = max(rev,currev)
        else:
            buy = sell
        sell +=1

    return rev


        
prices = [7,6,4,3,1]
print(maxProfit(prices))






                