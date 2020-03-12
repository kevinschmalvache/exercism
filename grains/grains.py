min_range = 1
max_range = 64

def square(number):
    if number < min_range or number > max_range:
        raise ValueError("fuera de rango.")

    return pow(2, number - 1)


def total():
    return sum([pow(2, grains) for grains in range(0, max_range)])