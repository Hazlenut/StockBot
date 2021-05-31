# x = int(input())
# y = int(input())
# z = x + y
# print(z)

# choice = input('s for stocks, c for crypto: ')
# if choice == 'c':
#     print('doge')
# if choice == 's':
#     print('fucck u')

import robin_stocks.robinhood as rs

your_username = input('email: ')
your_password = input('password: ')

rs.login(username=your_username,
         password=your_password,
         expiresIn=86400,
         by_sms=True)

choice = input('s for stocks, c for crypto: ')
if choice == 's':
    print('stonk')
    symbol = input('Type in stock symbol: ')
    price_or_quantity = input('p for price, q for quantity: ')
    if price_or_quantity == 'p': 
        print('price')
        #still need to add ammount in dollars variable and quqantity variable
        
            # rs.orders.order_buy_fractional_by_price(symbol,
            #                            ammountInDollars,
            #                            timeInForce='gtc',
            #                            extendedHours=False)
    if price_or_quantity == 'q':
        print('quantity')
            # rs.orders.order_buy_fractional_by_quantity(symbol,
            #                               quantity,
            #                               timeInForce='gtc',
            #                               extendedHours=False)






if choice == 'c':
    print('doge')
    c_symbol = input('Type in crypto symbol: ')
    c_amountInDollars = float(input('Type in how much in dollars. $X.XX'))
    rs.orders.order_buy_crypto_by_price(c_symbol, 
                                 c_amountInDollars,
                                 timeInForce='gtc')
