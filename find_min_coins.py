def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # масив для зберігання мін. кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0 

    # Зберігатимемо, які монети використовуються для складання конкретної суми
    coin_used = [-1] * (amount + 1)

    # Для кожної монети проходимо всі можливі значення суми
    for coin in coins:
        for current_amount in range(coin, amount + 1):
            if min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                coin_used[current_amount] = coin

    # Якщо сума не може бути складена, повертаємо пустий результат
    if min_coins[amount] == float('inf'):
        return {}

    # Відновлюємо кількість монет для отриманої суми
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Введення суми
try:
    amount_input = input("Введіть суму для видачі решти: ")
    amount_input = amount_input.replace(',', '.')
    total_amount = float(amount_input)
    
    integer_amount = int(total_amount)
    fractional_part = round(total_amount - integer_amount, 2)  
    
    
    if fractional_part > 0:
        print(f"У Попа здачі нема! {fractional_part * 100} копійок на чай персоналу.")
    
    
except ValueError as e:
    print(f"Помилка: {e}")
else:
    result = find_min_coins(integer_amount)
    print(f"Динамічне програмування для суми {integer_amount}: {result}")
