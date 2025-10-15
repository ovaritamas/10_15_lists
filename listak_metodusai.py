honapok = ['január', 'február','március', 'április', 'május', 'június']

honapok.append('július')
print(honapok)

honapok.pop()
print(f"Utolsó hónap törlése után a lista: {honapok}")
torolt_honapok = honapok.pop()
print(torolt_honapok)
print(honapok)
print(f"Utolsó hónap törölve: {honapok}")

#Adott indexű elem kitörlése
honapok.pop(0)
print(f"Január kitörölve")
print(honapok)

#Érték alapján törlés
honapok.remove("február")
print(f"február kitörölve")
print(honapok)

honapok.insert(1, "február")
print(honapok)

del honapok[2]

#Lista ürítése
honapok.clear()
print(honapok)