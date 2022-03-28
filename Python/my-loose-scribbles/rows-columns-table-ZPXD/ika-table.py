from itertools import cycle

rows = int(input("Ile wierszy: "))
columns = int(input("Ile kolumn: "))
number_cycle = cycle('0123456789')
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(next(number_cycle))
    print(' '.join(row))

