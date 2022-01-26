from avg import half_year_avg
from coins import coins_list, add_coin, remove_coin
from decrease import decrease
from plot import live_plot, historical_plot, compare_plot
from rise import rise

API_KEY = '30e423dc533f856001bdd66654bb7ade9ee478237f223e4fa1ef1e9689aa741f'

import cryptocompare as cc


ccobj = cc.cryptocompare._set_api_key_parameter(API_KEY)

coins = ['BTC', 'ETH', 'LUNA', 'FTM', 'BNB', 'BUSD', 'DOGE', 'SOL', 'ADA', 'ATOM']





while True:
  print("Wybierz jedna z dostępnych opcji:")
  print("1 - Możliwe tendencje wzrostowe")
  print("2 - Możliwe tendencje spadkowe")
  print("3 - Waluty których wartość jest wyższa niż średnia półroczna")
  print("4 - Wyświetl waluty")
  print("5 - Dodaj walute")
  print("6 - Usuń walutę")
  print("7 - Wykres cen na żywo")
  print("8 - Wykres cen z dni")
  print("9 - Wykres porównawczy z dni")
  print("10 - Zakończ")
  x = input("Wprowadź wartość: ")
  match x:
        case '1':
            rise(coins)
        case '2':
            decrease(coins)
        case '3':
            half_year_avg(coins)
        case '4':
            coins_list(coins)
        case '5':
            add_coin(coins)
        case '6':
            remove_coin(coins)
        case '7':
            live_plot()
        case '8':
            historical_plot()
        case '9':
            compare_plot(coins)
        case '10':
            break


#
#
#
