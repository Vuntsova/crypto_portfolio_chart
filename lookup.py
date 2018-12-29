import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from tkinter import *
import json
import requests
import os
import string
import random
os.system('cls')

def red_green(amount):
    if amount >=0:
        return "green"
    else:
        return 'red'
root = Tk()
root.title('Crypto Currency Portfolio')
date = Label(root, text='Position', bg='yellow', font='Helvetica 18 bold')
date.grid(row=14,column=0, sticky=N+S+E+W)
name = Label(root, text='Name', bg='yellow', font='Helvetica 18 bold')
name.grid(row=14,column=1, sticky=N+S+E+W)
rank = Label(root, text='Rank', bg='yellow', font='Helvetica 18 bold')
rank.grid(row=14,column=2, sticky=N+S+E+W)
amount = Label(root, text='Amount', bg='yellow', font='Helvetica 18 bold')
amount.grid(row=14,column=3, sticky=N+S+E+W)
current_price = Label(root, text='Current Price', bg='yellow',font='Helvetica 18 bold')
current_price.grid(row=14,column=4, sticky=N+S+E+W)
price_paid = Label(root, text='Price Paid', bg='yellow', font='Helvetica 18 bold')
price_paid.grid(row=14,column=5, sticky=N+S+E+W)
profit_loss = Label(root, text='P/L Per', bg='yellow', font='Helvetica 18 bold')
profit_loss.grid(row=14,column=6, sticky=N+S+E+W)
one_hour = Label(root, text='1 Hour Change', bg='yellow', font='Helvetica 18 bold')
one_hour.grid(row=14,column=7, sticky=N+S+E+W)
twenty_four_hour = Label(root, text='24 Hour Change', bg='yellow', font='Helvetica 18 bold')
twenty_four_hour.grid(row=14,column=8, sticky=N+S+E+W)
week_change = Label(root, text='7 Days Change', bg='yellow', font='Helvetica 18 bold')
week_change.grid(row=14,column=9, sticky=N+S+E+W)
current_value = Label(root, text='Current Value', bg='yellow', font='Helvetica 18 bold')
current_value.grid(row=14,column=10, sticky=N+S+E+W)
total = Label(root, text='Total L/P', bg='yellow', font='Helvetica 18 bold')
total.grid(row=14,column=11, sticky=N+S+E+W)

portfolio_profit_loss = 0
print('----------------------------------------')
my_portfolio = []
def lookup():
    print('updating')
    global_url = 'https://api.coinmarketcap.com/v1/ticker/'
    request = requests.get(global_url)
    results = request.json()
    portfolio_profit_loss =0
    row_count = 15
    position = 1
    total_current_value = 0
    pie = []
    pie_size=[]
    chart_colors=[]

    # does not exist
    Label(root, text="Add Currency", font='Helvetica 18 bold').grid(row=0, column=4)
    # Label(root, text="Remove Currency (Use Position)", font='Helvetica 18 bold').grid(row=3, column=3)
    Label(root, text = '$', bg='yellow').grid(row=11, column=4)
    Label(root, text="Your Current Portfolio", font='Helvetica 18 bold').grid(row=12, column=4)


    Label(root, text="Symbol").grid(row=1, column=3)
    Label(root, text="Amount").grid(row=1, column=4)
    Label(root, text="Price Paid").grid(row=1, column=5)
    # Label(root, text="Symbol").grid(row=4, column=3)

    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    # e4 = Entry(root)

    e1.grid(row=2, column=3)
    e2.grid(row=2, column=4)
    e3.grid(row=2, column=5)
    # e4.grid(row=4, column=3)
    color=''
    def getRandomColor():
        example = 'abcdef'
        letters = "0123456789ABCDEF"
        color = '#'
        for e in example:
            color+=random.choice(letters)
        return color
    # getRandomColor()    print(gfg)
    for result in results:
        for coin in my_portfolio:

            if coin['sym'] == result['symbol']:

                print()
                total_paid = float(coin['amount_owned']) * float(result['price_usd'])
                worth_now = float(coin['amount_owned']) * float(coin['price_paid_per'])
                profit_loss =  float(total_paid) - float(worth_now)
                portfolio_profit_loss +=profit_loss
                per_coin_loss = float(result['price_usd']) - float(coin['price_paid_per'])
                current_value = float(coin['amount_owned']) * float(result['price_usd'])
                loss = current_value - worth_now
                total_current_value+=current_value
                pie.append(result['name'])
                pie_size.append(coin['amount_owned'])
                chart_colors.append(getRandomColor())
                date = Label(root, text=position, bg='white')
                date.grid(row=row_count,column=0, sticky=N+S+E+W)
                name = Label(root, text=result['name'], bg='silver')
                name.grid(row=row_count,column=1, sticky=N+S+E+W)
                rank = Label(root, text=result['rank'], bg='white')
                rank.grid(row=row_count,column=2, sticky=N+S+E+W)
                amount= Label(root, text= coin['amount_owned'], bg='silver')
                amount.grid(row=row_count,column=3, sticky=N+S+E+W)
                current_price = Label(root, text='${0:.2f}'.format(float(result['price_usd'])), bg='white')
                current_price.grid(row=row_count,column=4, sticky=N+S+E+W)
                price_paid = Label(root, text='${0:.2f}'.format(float(coin['price_paid_per'])), bg='silver')
                price_paid.grid(row=row_count,column=5, sticky=N+S+E+W)
                profit_loss = Label(root, text='${0:.2f}'.format(float(per_coin_loss)), bg='white', fg=red_green(float(per_coin_loss)))
                profit_loss.grid(row=row_count,column=6, sticky=N+S+E+W)
                one_hour = Label(root, text='%{0:.2f}'.format(float(result['percent_change_1h'])), bg='silver', fg=red_green(float(result['percent_change_1h'])))
                one_hour.grid(row=row_count,column=7, sticky=N+S+E+W)
                twenty_four_hour = Label(root, text='%{0:.2f}'.format(float(result['percent_change_24h'])), bg='white', fg=red_green(float(result['percent_change_24h'])))
                twenty_four_hour.grid(row=row_count,column=8, sticky=N+S+E+W)
                week_change = Label(root, text='%{0:.2f}'.format(float(result['percent_change_7d'])), bg='silver', fg=red_green(float(result['percent_change_7d'])))
                week_change.grid(row=row_count,column=9, sticky=N+S+E+W)
                current_value = Label(root, text='${0:.2f}'.format(float(current_value)), bg='white')
                current_value.grid(row=row_count,column=10, sticky=N+S+E+W)
                total = Label(root, text='${0:.2f}'.format(float(loss)), bg='silver', fg=red_green(float(loss)))
                total.grid(row=row_count,column=11, sticky=N+S+E+W)

                row_count+=1
                position+=1

    def add():
        if e1.get() and e2.get() and e3.get():
            global my_portfolio
            my_portfolio.append({'sym':e1.get(),'amount_owned': e2.get(), 'price_paid_per':e3.get(), 'position':position})
            print(my_portfolio)
            lookup()
    def remove():
        if e1.get() and e2.get() and e3.get():
            global my_portfolio
            my_portfolio.append({'sym':e1.get(),'amount_owned': e2.get(), 'price_paid_per':e3.get(), 'position':position})
            print(my_portfolio)
            lookup()
    add_button = Button(root, text="+ Add", command=add)
    add_button.grid(row = 2, column = 6, sticky=E+S, padx=10, pady=10)
    # remove_button = Button(root, text="- Remove", command=remove)
    # remove_button.grid(row = 4, column = 4, sticky=E+S, padx=10, pady=10)
    root.title('Crypto Currency Portfolio - Portfolio Value: ${0:.2f}'.format(float(total_current_value)))
    portfolio_profits = Label(root, text='P/L: ${0:.2f}'.format(float(portfolio_profit_loss)), bg='yellow', fg=red_green(float(portfolio_profit_loss)), font='Helvetica 18 bold')
    portfolio_profits.grid(row=row_count,column=0, sticky=W, padx=10, pady=10)

    results = ""
    update_button = Button(root, text="Update", command=lookup)
    update_button.grid(row = row_count, column = 9, sticky=E+S, padx=10, pady=10)

    def graph(pie, pie_size):
        # Data to plot
        labels = pie
        sizes = pie_size
        colors = chart_colors
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    graph_button = Button(root, text="Pie Chart", command = lambda:  graph(pie, pie_size))
    graph_button.grid(row = row_count, column =8, sticky=E+S, padx=10, pady=10)

    # print(pie_size)

lookup()

root.mainloop()
