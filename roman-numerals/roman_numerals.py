def roman(number):
    ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numerals = ""
    for i in range(len(ints)):
        count = int(number // ints[i])
        numerals += (syms[i] * count)
        number -= ints[i] * count
    return numerals