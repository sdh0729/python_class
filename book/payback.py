money = int(input('pay: '))
count = 0
coin_types=[500,100,50,10]

for coin in coin_types:
    count +=money//coin
    money %= coin

print(count)