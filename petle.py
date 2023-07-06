# jezyki = ["C","Python","Java"]
# cyfry = [1,2,3,4,5,6,7,8,9]
#
# print("jezyki Programowania:")
# for x in range(len(jezyki)):
#     print(jezyki[x])
#
# for x in range(1,len(cyfry),2):
#     print(f'Cyfry: {cyfry[x]}')
#
#
# print(*cyfry, sep='-')
# print(cyfry)



for p in range(3):
    for q in range(4):
        if q == 2:
            print(f'Pomijam q={q}')
            continue
    print(f'(p={p}, q={q})')
