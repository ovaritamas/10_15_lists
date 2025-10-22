"""Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!"""

oszthatosag = []

for i in range(1, 41):
    if i % 3 == 0:
        oszthatosag.append(i)

print(f"Az 1-40-ig tartó számok közül 3-al osztható számok:\n{oszthatosag}")
