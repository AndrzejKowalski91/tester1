dozwoloneWaluty = ('PLN','EUR','USD')
# waluta = input("Podaj walutę: ")
#
# if waluta in dozwoloneWaluty:
#     print("poprawna waluta")
# else:
#     print(f"Nieznany kod waluty, podano: {waluta}")
#     print("Nieznany kod waluty, podano: {}".format(waluta))
#     print(f"Nieznany kod waluty, podano: %s" % waluta)

lista = []
lista2 =["ania","jaroslaw","kaczynski"]


lista.append("Andrzej")
lista.append("Jan")
lista.append("Paweł")
lista.insert(1,'Maria')
lista.append(dozwoloneWaluty)
lista.pop(0)
lista.remove('Maria')
lista.append(lista2)
# lista.clear()
lista[0] = "Jan"
# lista.sort()
lista.reverse()
# lista[1] =lista[2]
print(lista[0])
# zmienna = lista[1:4]
# ostatni = lista[-1][0]

print(lista)
# print(zmienna)
# print(ostatni)