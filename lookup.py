import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from tkinter import *
import json
import requests
import os
os.system('cls')

def red_green(amount):
    if amount >=0:
        return "green"
    else:
        return 'red'
root = Tk()
root.title('Crypto Currency Portfolio')
name = Label(root, text='Name', bg='white', font='Helvetica 18 bold')
name.grid(row=0,column=0, sticky=N+S+E+W)
rank = Label(root, text='Rank', bg='silver', font='Helvetica 18 bold')
rank.grid(row=0,column=1, sticky=N+S+E+W)
current_price = Label(root, text='Current Price', bg='white',font='Helvetica 18 bold')
current_price.grid(row=0,column=2, sticky=N+S+E+W)
price_paid = Label(root, text='Price Paid', bg='silver', font='Helvetica 18 bold')
price_paid.grid(row=0,column=3, sticky=N+S+E+W)
profit_loss = Label(root, text='P/L Per', bg='white', font='Helvetica 18 bold')
profit_loss.grid(row=0,column=4, sticky=N+S+E+W)
one_hour = Label(root, text='1 Hour Change', bg='silver', font='Helvetica 18 bold')
one_hour.grid(row=0,column=5, sticky=N+S+E+W)
twenty_four_hour = Label(root, text='24 Hour Change', bg='white', font='Helvetica 18 bold')
twenty_four_hour.grid(row=0,column=6, sticky=N+S+E+W)
week_change = Label(root, text='7 Days Change', bg='silver', font='Helvetica 18 bold')
week_change.grid(row=0,column=7, sticky=N+S+E+W)
current_value = Label(root, text='Current Value', bg='white', font='Helvetica 18 bold')
current_value.grid(row=0,column=8, sticky=N+S+E+W)
total = Label(root, text='Total L/P', bg='silver', font='Helvetica 18 bold')
total.grid(row=0,column=9, sticky=N+S+E+W)


portfolio_profit_loss = 0
print('----------------------------------------')

def lookup():
    global_url = 'https://api.coinmarketcap.com/v1/ticker/'
    request = requests.get(global_url)
    results = request.json()
    my_portfolio = [
        {
            'sym':'STEEM',
            'amount_owned': 3000,
            'price_paid_per': .80
        },
        {
            'sym':'BTC',
            'amount_owned': 5,
            'price_paid_per': 4887.80
        },
        {
            'sym':'XRP',
            'amount_owned': 3110,
            'price_paid_per': .10
        },
        {
            'sym':'USDT',
            'amount_owned': 3110,
            'price_paid_per': 1.10
        },
        {
            'sym':'ADA',
            'amount_owned': 1000,
            'price_paid_per': .10
        }
    ]
    portfolio_profit_loss =0
    row_count = 1
    total_current_value = 0
    pie = []
    pie_size=[]

    for result in results:
        for coin in my_portfolio:
            if coin['sym'] == result['symbol']:

                total_paid = float(coin['amount_owned']) * float(result['price_usd'])
                worth_now = float(coin['amount_owned']) * float(coin['price_paid_per'])
                profit_loss =  float(total_paid) - float(worth_now)
                portfolio_profit_loss +=profit_loss
                per_coin_loss = float(result['price_usd']) - float(coin['price_paid_per'])
                current_value = float(coin['amount_owned']) * float(result['price_usd'])
                other_value = float(float(coin['amount_owned']) * float(coin['price_paid_per']))
                loss = current_value - other_value
                total_current_value+=current_value
                pie.append(result['name'])
                pie_size.append(coin['amount_owned'])
                name = Label(root, text=result['name'], bg='white')
                name.grid(row=row_count,column=0, sticky=N+S+E+W)
                rank = Label(root, text=result['rank'], bg='silver')
                rank.grid(row=row_count,column=1, sticky=N+S+E+W)
                current_price = Label(root, text='${0:.2f}'.format(float(result['price_usd'])), bg='white')
                current_price.grid(row=row_count,column=2, sticky=N+S+E+W)
                price_paid = Label(root, text='${0:.2f}'.format(float(coin['price_paid_per'])), bg='silver')
                price_paid.grid(row=row_count,column=3, sticky=N+S+E+W)
                profit_loss = Label(root, text='${0:.2f}'.format(float(per_coin_loss)), bg='white', fg=red_green(float(per_coin_loss)))
                profit_loss.grid(row=row_count,column=4, sticky=N+S+E+W)
                one_hour = Label(root, text='%{0:.2f}'.format(float(result['percent_change_1h'])), bg='silver', fg=red_green(float(result['percent_change_1h'])))
                one_hour.grid(row=row_count,column=5, sticky=N+S+E+W)
                twenty_four_hour = Label(root, text='%{0:.2f}'.format(float(result['percent_change_24h'])), bg='white', fg=red_green(float(result['percent_change_24h'])))
                twenty_four_hour.grid(row=row_count,column=6, sticky=N+S+E+W)
                week_change = Label(root, text='%{0:.2f}'.format(float(result['percent_change_7d'])), bg='silver', fg=red_green(float(result['percent_change_7d'])))
                week_change.grid(row=row_count,column=7, sticky=N+S+E+W)
                current_value = Label(root, text='${0:.2f}'.format(float(current_value)), bg='white')
                current_value.grid(row=row_count,column=8, sticky=N+S+E+W)
                total = Label(root, text='${0:.2f}'.format(float(loss)), bg='silver', fg=red_green(float(loss)))
                total.grid(row=row_count,column=9, sticky=N+S+E+W)

                row_count+=1

    root.title('Crypto Currency Portfolio - Portfolio Value: ${0:.2f}'.format(float(total_current_value)))
    portfolio_profits = Label(root, text='P/L: ${0:.2f}'.format(float(portfolio_profit_loss)), bg='white', fg=red_green(float(portfolio_profit_loss)))
    portfolio_profits.grid(row=row_count,column=0, sticky=W, padx=10, pady=10)
    results = ""
    update_button = Button(root, text="Update", command=lookup)
    update_button.grid(row = row_count, column = 9, sticky=E+S, padx=10, pady=10)

    def graph(pie, pie_size):
        # Data to plot
        labels = pie
        sizes = pie_size
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    graph_button = Button(root, text="Pie Chart", command = lambda:  graph(pie, pie_size))
    graph_button.grid(row = row_count, column =8, sticky=E+S, padx=10, pady=10)
    print(pie_size)

lookup()

root.mainloop()
