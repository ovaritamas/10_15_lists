harmas = []
otos = []
mindketto = []

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        mindketto.append(i)
    elif i % 3 == 0:
        harmas.append(i)
    elif i % 5 == 0:
        otos.append(i)

print(f"Csak a hármas:{harmas}")
print(f"Csak az ötös:{otos}")
print(f"Mindkettő:{mindketto}")