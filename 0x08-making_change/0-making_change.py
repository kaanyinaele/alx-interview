def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        # Use as many coins of this denomination as possible
        coin_count += total // coin
        total %= coin

    # If total is not 0, it means we can't meet the amount
    if total != 0:
        return -1
    return coin_count
