c = 0
s = 0
while True:
    n = int(input('Digit um valor(999 p/ Parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores digitados foi {s}!')