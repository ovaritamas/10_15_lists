"""
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, 
ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! 
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, 
és a program törölje ennek a számnak valamennyi előfordulását a listából, 
majd írja ki a módosított listát a képernyőre!

"""

import random as r

szamok = []

for i in range(1,11):
    rszam = r.randint(1,3)
    szamok.append(rszam)

print(szamok)

user = int(input("Adj meg egy számot 1 és három között: "))

if user in szamok:
    while user in szamok:
        szamok.remove(user)
    print(f"Kitöröltem a számodat. Jelenleg a lista:\n {szamok}")

else:
    print("Kérlek a megfelelő intervallumban adj számot")