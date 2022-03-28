# czy w podanej liście numbers istnieją 2 liczby, których suma równa jest zmiennej value
# liczbę value, listę liczb dodatnich numbers


def check(value: int, numbers: list[int]) -> bool:
    numbers = sorted(list(set(numbers)), key=lambda x: x <= value)
    for num in numbers:
        if (value - num) in numbers:
            return True
    return False


a, b = 126, [12, 26, 14, 18, 30, 50, 60, 55, 88, 96, 128, 203, 405]
print(check(a, b))
