import cryptocompare as cc

def coins_list(coins):
    for coin in coins:
        print(coin)

def add_coin(coins):
    all_coins = cc.get_coin_list()
    coin = input("Wprowadź symbol waluty: ")
    if not coin in coins:
        if coin in all_coins:
            coins.append(coin)
            print("Dodano walutę " + coin)
        else:
            print("Nie ma takiej waluty!")
    else:
        print("Waluta jest już dodana")

def remove_coin(coins):
    coin = input("Wprowadź symbol waluty: ")
    if coin in coins:
        coins.remove(coin)
        print("Usunięto walutę " + coin)
    else:
        print("Waluta nie została dodana!")