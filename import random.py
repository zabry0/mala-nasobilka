import random

# Násobení A a B, vyhodnocení funkce
def nasobeni(a, b):
    vysledek = a * b
    return vysledek

# Výsledek porovnání a pochvala
def vyhodnoceni(vysledek, porovnani):
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
    vysledek = nasobeni(x, y)
    porovnani = int(input(f'{x} * {y} = '))
    
    if vyhodnoceni(vysledek, porovnani):
        spravne_odpovedi += 1

# Počet správných odpovědí
print(f"Počet správných odpovědí: {spravne_odpovedi} z 10.")
