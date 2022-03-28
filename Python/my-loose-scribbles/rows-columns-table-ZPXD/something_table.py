

'''


Dostając na wejście liczbę wierszy i kolumn wyrysuj na ekranie tablicę, która będzie wypełniona cyframi od 0 do 9. Każdy element tablicy w wierszu
ma być oddzielony spacją. Dla przykładu wywołanie tablica(3, 4) ma wypisać na ekran tablicę w następujący sposób:
0 1 2 3
4 5 6 7
8 9 0 1


'''


row = int(input('Podaj ile ma byc rzedow: '))
column = int(input('Podaj ile ma byc kolumn: '))
l = 0

#if column >= row:
for x in range(1,row+1,1):
    for y in range(1,column+1,1):
        if l < 10:
            print(l, end=" ")
            l+=1
        else:
            l = 0
            print(l,end=" ")
            l+=1

    print()



#Kuba comment

# mew comment by Artur


