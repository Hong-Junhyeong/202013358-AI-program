st = 'Programing'

for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        break
    print(ch)
print('The end')


st = 'Programing'

for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(ch)
print('The end')
