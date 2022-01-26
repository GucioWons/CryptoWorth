import matplotlib.pyplot as plt
from datetime import datetime
import cryptocompare as cc
from matplotlib.animation import FuncAnimation


def live_plot():
    coin = input("Wprowadź symbol waluty: ")
    all_coins = cc.get_coin_list()
    if not coin in all_coins:
        print("Nie ma takiej waluty!")
        return
    plt.style.use('seaborn')
    x_vals = []
    y_vals = []
    def animate(i):
        x_vals.append(datetime.now())
        y_vals.append(cc.get_price(coin, 'EUR')[coin]['EUR'])
        plt.title(cc.get_coin_list()[coin]['FullName'] + " - cena na żywo")
        plt.xlabel('Data')
        plt.ylabel('Cena')

        plt.plot_date(x_vals, y_vals, linestyle='solid', ms=0)
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()

def compare_plot(coins):
    plt.style.use('seaborn')
    days = input("Wprowadź ilość dni: ")
    if days == 0:
        print("Ilość dni nie może być równa 0!")
        return
    if not coins:
        print("W liście nie ma żadnej waluty!")
        return
    for coin in coins:
        x_vals = []
        y_vals = []
        data = cc.get_historical_price_day(coin, 'EUR', limit=days)
        for day in data:
            x_vals.append(datetime.fromtimestamp(day['time']))
            y_vals.append(day['volumeto']/day['volumefrom'])
        plt.plot_date(x_vals, y_vals, linestyle='solid', label=coin)
    plt.title(str(days) + " - dniowy wykres porównawczy")
    plt.xlabel('Data')
    plt.ylabel('Cena')

    plt.legend(loc='best')

    plt.tight_layout()

    plt.show()

def historical_plot():
    coin = input("Wprowadź symbol waluty: ")
    all_coins = cc.get_coin_list()
    if not coin in all_coins:
        print("Nie ma takiej waluty!")
        return
    x_vals = []
    y_vals = []
    days = input("Wprowadź ilość dni: ")
    data = cc.get_historical_price_day(coin, 'EUR', limit=days)
    plt.style.use('seaborn')
    for day in data:
        x_vals.append(datetime.fromtimestamp(day['time']))
        y_vals.append(day['volumeto']/day['volumefrom'])
        plt.title(cc.get_coin_list()[coin]['FullName'] + ": " + days + " - dniowy wykres średniej")
        plt.xlabel('Data')
        plt.ylabel('Cena')

    plt.plot_date(x_vals, y_vals, linestyle='solid', ms=0)
    plt.tight_layout()

    plt.show()