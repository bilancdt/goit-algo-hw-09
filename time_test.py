import timeit

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for current_amount in range(coin, amount + 1):
            if min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                coin_used[current_amount] = coin

    if min_coins[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Вибір суми для тесту
amount = 9876 

# Вимірювання часу роботи жадібного алгоритму
greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд")

# Вимірювання часу роботи алгоритму динамічного програмування
dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)
print(f"Час виконання алгоритму динамічного програмування: {dp_time:.6f} секунд")
