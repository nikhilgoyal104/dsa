# T=1,S=1
def main(num):
    res, i = [], 0
    digits = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
        ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
    while num:
        symbol, val = digits[i]
        count, num = divmod(num, val)
        res.append(count * symbol)
        i += 1
    return ''.join(res)


for num in [
    3, 4, 9, 58, 478, 1994, 671, 3888, 3999
]:
    print(main(num))
