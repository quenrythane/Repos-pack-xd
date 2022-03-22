import random

def tablica1(rows, columns):
    numbers_list = [i % 10 for i in range(rows * columns)]
    result = [[] for x in range(rows)]  # create list of empty lists (each list is a row)
    [result[index // columns].append(str(number)) for index, number in enumerate(numbers_list)]  # fill the lists
    for lst in result:  # display the table
        print(' '.join(lst))


def tablica2(rows, columns):
    numbers_list = [i % 10 for i in range(rows * columns)]
    for i in range((rows * columns) // columns):
        print(*numbers_list[i * columns:(i + 1) * columns])


# same as above but in one line - just for fun :)
def tablica3(rows, columns):
    [print(*[i % 10 for i in range(rows * columns)][i * columns:(i + 1) * columns]) for i in range((rows * columns) // columns)]


tablica1(7, 3)
print()
tablica2(7, 3)
print()
tablica3(7, 3)
print('\n')

r, c = random.sample(range(5, 20), 2)
tablica1(r, c)
print()
tablica2(r, c)
print()
tablica3(r, c)
print()
