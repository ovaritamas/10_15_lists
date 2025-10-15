"""
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, 
és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót,
és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket! 
"""

szinek = ["kék", "piros", "fehér", "fekete", "lila"]

user = input("Adj egy színt: ")

if user in szinek:
    print("A megadott szín szerepel a listában")

else:
    print("A szín még nem szerepel a litában")

print(f"A lista tartalma: \n{", ".join(szinek)}")