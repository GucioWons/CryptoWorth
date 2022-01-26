import cryptocompare as cc

def rise(coins):
    if not coins:
        print("W liście nie ma żadnej waluty!")
        return
    print("Tendencje wzrostowe:")
    for coin in coins:
        avg3 = 0
        avg10 = 0
        data = cc.get_historical_price_day(coin, 'EUR', limit=3)
        for day in data:
            volumefrom = day['volumefrom']
            volumeto = day['volumeto']
            avg3 = avg3 + volumeto / volumefrom
        avg3 = avg3 / 3
        data = cc.get_historical_price_day(coin, 'EUR', limit=10)
        for day in data:
            volumefrom = day['volumefrom']
            volumeto = day['volumeto']
            avg10 = avg10 + volumeto / volumefrom
        avg10 = avg10 / 10
        if avg3 > avg10:
            print(coin + ": " + str(avg3) + ">" + str(avg10))