def series(n):  # 5
    return round(sum([1 / (i * 3 + 1) for i in range(n)]), 2)


print(series(2))
print(series(5))
