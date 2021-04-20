import robin_stocks as rs

rs.login(username=your_username,
         password=your_password,
         expiresIn=86400,
         by_sms=True)

rs.orders.order_buy_fractional_by_price(symbol,
                                       ammountInDollars,
                                       timeInForce='gtc',
                                       extendedHours=False) 


rs.orders.order_buy_fractional_by_quantity(symbol,
                                          quantity,
                                          timeInForce='gtc',
                                          extendedHours=False)

rs.orders.order_buy_crypto_by_price('ETH', 
                                 1000,
                                 timeInForce='gtc')