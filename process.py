import requests
import sched
from win10toast import ToastNotifier

toast = ToastNotifier()


def check_price(crypto_code, fiat_code, alert_type, price, percentage):

    price = float(price)

    if not isinstance(price, float):
        raise AttributeError('Price has to be float or integer')

    crypto_code = crypto_code.upper()
    fiat_code = fiat_code.upper()

    params = {'symbol': crypto_code+fiat_code}

    query = f"https://api.binance.com/api/v3/ticker/price"

    try:
        r = requests.get(url=query, params=params)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    alert = alert_type.lower()
    data = r.json()

    try:
        symbol = data['symbol']
        current_price = data['price']
    except KeyError:
        print(data['msg'])

    current_price = float(current_price)

    if alert == 'up':
        if current_price > price:
            percentage_increase = (current_price-price) / price * 100
            if percentage_increase >= percentage:
                toast.show_toast(f"PRICE ALERT | {crypto_code} - {fiat_code}",
                                 f"Price has increased by {round(percentage_increase, 3)}\nCurrent price: {float(current_price)}", duration=20, icon_path="logo.ico")

    if alert == 'down':
        if current_price < price:
            percentage_decrease = (price-current_price) / price * 100
            if percentage_decrease >= percentage:
                toast.show_toast(f"PRICE ALERT | {crypto_code} - {fiat_code}",
                                 f"Price has dropped by {round(percentage_decrease, 3)}\nCurrent price: {current_price}", duration=20, icon_path="logo.ico")
