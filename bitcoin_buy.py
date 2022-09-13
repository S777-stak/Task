price = input("Bitcoin price: ")
cash = input("Cash: ")

try:
    int_price = float(price)
    int_cash = float(cash)
    print("{} BTC".format(int_cash/int_price))
except Exception as ex:
    print("Input data is not a numbers")
