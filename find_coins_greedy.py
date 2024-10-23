def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin

    return result


amount = 3541.01
print("Жадібний алгоритм:", find_coins_greedy(amount))
