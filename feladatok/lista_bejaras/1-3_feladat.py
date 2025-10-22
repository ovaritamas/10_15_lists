"""Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!"""

harommal = []
hattal = []

for i in range(1, 41):
    if i % 3 == 0:
        harommal.append(i)
    if i % 6 == 0:
        hattal.append(i)

print(f"Az 1-40-ig tartó számok közül 3-al osztható számok:\n{harommal}")
print(f"Az 1-40-ig tartó számok közül 3-al osztható páros számok:\n{hattal}")
