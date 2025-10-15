honapok = ['január', 'február','március', 'április', 'május', 'június', 'július']

print(type(honapok))
print(len(honapok))
print(honapok(0))
print(honapok(1))
print(honapok(2))
print(honapok(3))
print(f"Az utolsó hónap:"(honapok[-1]))

#csak bizonyops elemek


#a 3.indexel bezárólag
print(honapok[:3])

#az 1.indextől kezdve
print(honapok[1:])

# join(): a lista elemeit egy sztringgé fűzi össze
# a megadott elválasztó karakterekkel tagolva
print(', '.join(honapok))

for i in range(len(honapok)):
    print(honapok[i])

print('\nHonapok:\n')
for honap in honapok:
    print(honap)

