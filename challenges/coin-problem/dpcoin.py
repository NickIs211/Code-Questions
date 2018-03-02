def min_coins(coins, change):
    maximum = 999999999999999
    table = [0 for i in range(change+1)]
    for c in range(1, change+1):
        table[c] = maximum  # Where c is the worst case
        for coin in coins:
            if(coin <= c and table[c-coin] + 1 < table[c]):
                table[c] = table[c-coin]+1
    return table[c] if table[c] != maximum else None


coins = [2, 5, 8]
change = 19
print(min_coins(coins, change))
