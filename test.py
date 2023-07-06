menu="""
**************
*    MENU    *
**************
"""
print(menu)

imie = input("podaj imię:").lower()
rok = input("podaj rok:")
# print(type(imie))
# print(type(rok))
lata = (rok,imie)
print(type(lata))
if int(rok) < 2020:
    print("to jest data przed 2020...")
elif int(rok) > 2023:
    print("to jest data przyszła...")
    if imie=="Andrzej":
        print('tojest andrzej przyszłości')

else:
    print("to jest data miedzy 2020-2023")


print('zawartość krotki:',lata)

print(imie.upper())
print(imie.lower())
#print(lata.index('andrzej'))
