"""
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, 
hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! Ha a megadott szín nincs még tárolva,
továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg! 
"""

szinek = ["kék", "piros", "fehér", "fekete", "lila"]

user = input("Adj egy színt: ")

if user in szinek:
    print("A megadott szín szerepel a listában")
    print(szinek.count(user))

else:
    print("A szín még nem szerepel a litában")

print(f"A lista tartalma: \n{", ".join(szinek)}")