#Tento kód generuje 10 příkladů na násobeni dělení sčítání a odečítání s konečným vyhodnocením bodů z 10 (10 příkladů)

import random

# násobení A a B, vyhodnocení funkce
def nasobeni(a, b):
    vysledek = a * b
    return vysledek

# dělení A a B, vyhodnocení funkce
def deleni(a, b):
    vysledek = a / b
    return vysledek

# sčítání A a B, vyhodnocení funkce
def scitani(a, b):
    vysledek = a + b
    return vysledek

# odečítání A a B, vyhodnocení funkce
def odecitani(a, b):
    vysledek = a - b
    return vysledek

# Výsledek porovnání a pochvala
def vyhodnoceni(operace, vysledek, porovnani):
    if vysledek == porovnani:
        print('Ty jsi šikulka')
        return True
    else:
        print('Ahh, zrovna ses spletl')
        return False

# Počet správných odpovědí
spravne_odpovedi = 0

# 10 příkladů s náhodnou generací dvou čísel od 1 do 10 s vyhodnocením příkladů
for i in range(10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    operace = random.choice(['+', '-', '*', '/'])
    if operace == '+':
        vysledek = scitani(x, y)
    elif operace == '-':
        vysledek = odecitani(x, y)
    elif operace == '*':
        vysledek = nasobeni(x, y)
    elif operace == '/':
        vysledek = deleni(x, y)
    porovnani = int(input(f'{x} {operace} {y} = '))
    
    if vyhodnoceni(operace, vysledek, porovnani):
        spravne_odpovedi += 1

# Počet správných odpovědí
print(f"Počet správných odpovědí: {spravne_odpovedi} z 10.")
