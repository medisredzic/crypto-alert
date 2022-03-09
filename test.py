from process import check_price

check_list = []

with open('crypto.txt', 'r') as f:
    for n in f:
        split = n.split(':')
        check_list.append(f'{split[1]} {split[2]} {split[3]} {split[4]} {split[5].strip()}')

while True:
    for n in range(len(check_list)):
        split = check_list[n].split(' ')
        check_price(split[1], split[2], split[3], split[4], split[5])