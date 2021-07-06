import re

inp = '''
{
    "Subscriptions": [
        {
            "name": "Three month subscription",
            "price": "39900",
            "discount": "50"
        },
        {
            "name": "One month subscription",
            "price": "19900",
            "discount": "30"
        },
        {
            "name": "Premium free trial",
            "price": "40000",
            "discount": "10"
        }
    ]
}'''
name = re.findall('"name": "(.+)"', inp)
price = re.findall('"price": "(\d+)', inp)
discount = re.findall('"discount": "(\d+)', inp)
sums = []

for i in range(len(price)):
    sums.append(int(price[i]) - (int(price[i]) * int(discount[i]) // 100))

for i in range(len(name)):
    if sums[i] == min(sums):
        print(f'Name: {name[i]}\nPrice: {sums[i]}')
        exit()