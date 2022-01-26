import cryptocompare as cc

def half_year_avg(coins):
    if not coins:
        print("W liście nie ma żadnej waluty!")
        return
    print("Średnia roczna:")
    for coin in coins:
        avg = 0
        data = cc.get_historical_price_day(coin, 'EUR', limit=182)
        for day in data:
            volumefrom = day['volumefrom']
            volumeto = day['volumeto']
            avg = avg + volumeto / volumefrom
        avg = avg / 182
        print(coin + ": " + str(avg))
        if cc.get_price(coin)[coin]['EUR'] > avg:
            print("Wyższa")
        else:
            print("Niższa")