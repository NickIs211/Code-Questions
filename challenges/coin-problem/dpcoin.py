def min_coins(coins, change):
    table = [0 for i in range(change+1)]
    for c in range(1, change+1):
        table[c] = c  # Where c is the worst case
        for coin in coins:
            if(coin <= c and table[c-coin] + 1 < table[c]):
                table[c] = table[c-coin]+1
    return table[c]


coins = [1, 2, 5, 8]
change = 50
print(min_coins(coins, change))
