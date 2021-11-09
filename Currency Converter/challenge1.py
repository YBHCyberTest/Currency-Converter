from CurrencyExchanger import miniCurrencies, exchangeOffline
def start():
  print("Please choose your currencies: ")
  for i in range(0, len(miniCurrencies)):
    print(f"{i+1}.{miniCurrencies[i]}")
  fromm = int(input("From currency: "))

  for i in range(0, len(miniCurrencies)):
    print(f"{i+1}.{miniCurrencies[i]}")
  to = int(input("To currency: "))

  amount = float(input("Please Enter the amount you want to exchange: "))

  total = exchangeOffline(miniCurrencies[fromm-1], miniCurrencies[to-1], amount)
  print(f"{total}{miniCurrencies[to-1]}")
