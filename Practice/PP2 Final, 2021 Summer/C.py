inp = input()
with open('output.txt', 'w') as txt:
    txt.write(f'Hi, {inp}')
with open('output.txt') as txt:
    print(txt.read())