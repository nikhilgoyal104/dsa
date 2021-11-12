def main(num, den):
    if not num:
        return '0'
    res = []
    if num * den < 0:
        res.append('-')
    num, den = abs(num), abs(den)
    quot, rem = divmod(num, den)
    res += list(str(quot))
    if rem == 0:
        return ''.join(res)
    res.append('.')
    hm = {rem: len(res)}
    while rem:
        quot, rem = divmod(rem * 10, den)
        res.append(str(quot))
        if rem in hm:
            res.insert(hm[rem], '(')
            res.append(')')
            return ''.join(res)
        hm[rem] = len(res)
    return ''.join(res)


for num, den in [
    (0, -5),
    (47, 18),
    (14, 3),
    (4, 333),
    (1, 6),
    (37, 2),
    (428, 125),
    (1, 2),
    (2, 1),
    (2, 3),
    (1, 5),
    (93, 7),
    (1, 333),
    (-50, 8),
    (-2147483648, 1)
]:
    print(main(num, den))
