import time
import requests as req

currencies = open("currencies.txt", "r").read().split("\n")
miniCurrencies = ["TRY", "USD", "EUR", "SAR", "YER", "CAD"]

offlineRate = {"TRY": 0.1, "USD": 1, "EUR": 1.16, "SAR": 0.27, "YER": 0.001, "CAD": 0.81}

cache = {}


def current_milli_time():
    return round(time.time() * 1000)


def _exchangeFromInternet(key):
    url = f"https://free.currconv.com/api/v7/convert?q={key}&compact=ultra&apiKey=2965b854e24b26e824ca"
    res = req.get(url)
    if res.status_code != 200:
        return -1
    value = res.json()[key]
    cache[key] = (value, current_milli_time())
    return value


def exchange(fromm, to, amount):
    key = f"{fromm.upper()}_{to.upper()}"
    value, lastReqTime = cache.get(key, (None, 0))
    if (value != None and lastReqTime + 60 * 60 * 1000 > current_milli_time()):
        return round(value * amount, 2)
    else:
        return round(_exchangeFromInternet(key) * amount, 2)


def exchangeOffline(fromm, to, amount):
    if fromm not in miniCurrencies or to not in miniCurrencies:
        return -1
    return round(offlineRate[fromm] / offlineRate[to] * amount, 2)