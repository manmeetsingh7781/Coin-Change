def get_coin_type(coin_type):
    if coin_type == 10:
        coin_type = 'Dime'
    elif coin_type == 25:
        coin_type = 'Quarter'
    elif coin_type == 5:
        coin_type = 'Nickle'
    elif coin_type == 1:
        coin_type = "Penni"
    return coin_type


def getChange(cents):
    drawer = [25, 10, 5, 1]
    filtered_drawer = set()
    remainder = 0
    coin_type = get_coin_type(25)
    min_amount = 25
    for i in drawer:
        if i <= cents:
            filtered_drawer.add(i)

    for i in sorted(filtered_drawer):
        result = cents // i
        remainder = cents % i
        if result < min_amount:
            coin_type = i
            min_amount = result
    if remainder != 0:
        print(getChange(remainder))
    coin = get_coin_type(coin_type)
    return f'{min_amount} of {coin}s'


print(getChange(67))
