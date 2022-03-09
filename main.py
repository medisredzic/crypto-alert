import argparse

parser = argparse.ArgumentParser()

parser.add_argument('email', help='Email where notifications will be sent', type=str)
parser.add_argument('crypto', help='Crypto code to track. Example: "BTC"', type=str)
parser.add_argument('fiat', help='Fiat currency to compare to. Example: "USD"', type=str)
parser.add_argument('alert', help='Type of alert "down" or "up"', type=str)
parser.add_argument('price', help='Price that triggers alert', type=str)
parser.add_argument('percentage', help='Percentage of increase/decrease that will trigger alert')

args = parser.parse_args()

email = args.email
crypto_code = args.crypto
fiat_code = args.fiat
alert_type = args.alert
price = args.price
percentage = args.percentage

with open('crypto.txt', 'a') as f:
    f.write(f'{email}:{crypto_code}:{fiat_code}:{alert_type}:{price}:{percentage}\n')
