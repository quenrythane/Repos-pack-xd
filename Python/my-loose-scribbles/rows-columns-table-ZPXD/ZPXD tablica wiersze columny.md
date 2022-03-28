# _herodisiac
```python
a = 9
for i in range(rows):
    temp = []
    for j in range(col):
        a += 1
        temp.append(a%10)
    print(*temp)
```
<br>

# Artur_Babinski👑
```python
def tablica(rows, columns):
    numbers_list = [i % 10 for i in range(rows * columns)]
    result = [[] for row in range(rows)]  # create list of empty lists (each list is a row)
    [result[index // columns].append(str(number)) for index, number in enumerate(numbers_list)]  # fill the lists
    for lst in result:  # display the table 
        print(' '.join(lst))
```
```python
def tablica2(rows, columns):
    numbers_list = [i % 10 for i in range(rows * columns)]
    for i in range((rows * columns) // columns):
        print(*numbers_list[i * columns:(i + 1) * columns])
```
<br>

# Bartek
```python
def kolejna(liczba):
    wynik = 0
    if liczba + 1 > 9:
        wynik = 0
    else:
        wynik = liczba + 1
    return wynik

wiersz = int(input('Ile wierszy: '))
kolumna = int(input('Ile kolumn: '))
lista = ''

zmienna = 0

while wiersz != 0:

    for i in range(kolumna):
        wynik = zmienna
        lista = lista + str(wynik) + ' '
        zmienna = kolejna(zmienna)

    print(lista)
    lista = ''
    wiersz -= 1
```
<br>

# Boomer
```python
kolumny = 3
wiersze = 5
def prs(kol, wier):
   str = "" 
   arr = [i%10 for i in range(kol*wier)]
   for j in range(len(arr)):
      str += "{0}, ".format(arr[j])
      if j%kol==kol-1 and j>0:
         str += "\n"
   str_d = str.replace(',', '')
   return str_d

print(prs(kolumny, wiersze))
```
<br>


# Czarny
```python
def gen_table(row, col):
    from itertools import cycle
    steps = 10 * row * col//10
    iter_cycle = cycle(range(10))

    for i in range(steps):
        if i % col == 0 and i != 0:
            print()
        print(next(iter_cycle), end=" ")
```
<br>

# ika
```python
from itertools import cycle

rows = int(input("Ile wierszy: "))
columns = int(input("Ile kolumn: "))
number_cycle = cycle('0123456789')
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(next(number_cycle))
    print(' '.join(row))
```
<br>

# RafalK
```python
def funkcja(r, c):
   i=0
   for a in range(0, r):
      temp=[]
      for b in range(0, c):
         temp.append(i)
         if i ==9:
            i=0
         else:
            i +=1
      print(*temp)
      temp.clear()
funkcja(3,4)
```
<br>

# Sebastian K.
```python
def arr(w, k):
    i = 0
    for y in range(w):
        for x in range(k):
            print(i, end=" ")
            i += 1
            if i == 10:
                i = 0
        print()
```
<br>

# svenson
```python
def tablica(inputTable):
    numberOfALL = inputTable[0]*inputTable[1]
    tempDigit = 0

    for i in range(1, numberOfALL+1):
        if i % inputTable[1] == 0:
            print(tempDigit)
        else:
            print(tempDigit, end=' ')

        tempDigit += 1
        if tempDigit > 9:
            tempDigit = 0
```
<br>

# Urbid
```python
def tablica (n, m):
  ret = []
  nice_list = [(lambda x: str(x%10))(x) for x in list(range(0,n*m+1))]
  start, end = 0, m

  for _ in range(n):
    ret.append(" ".join(nice_list[start:end]))
    start, end = end, end+m

  return "\n".join(ret)
```
<br>
