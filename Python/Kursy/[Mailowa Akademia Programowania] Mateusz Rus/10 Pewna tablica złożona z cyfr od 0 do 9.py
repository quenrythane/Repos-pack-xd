def tablica(rows, columns):
    numbers_list = [i % 10 for i in range(rows * columns)]
    result = [[] for row in range(rows)]  # create list of empty lists (each list is a row)
    [result[index // columns].append(str(number)) for index, number in enumerate(numbers_list)]  # fill the lists
    for lst in result:  # display the table
        print(' '.join(lst))

tablica(3, 4)
tablica(5, 6)






