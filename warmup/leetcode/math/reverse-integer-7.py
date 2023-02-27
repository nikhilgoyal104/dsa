# T=logn,S=1
def main(n):
    res = 0
    factor = -1 if n < 0 else 1
    range = 2 ** 31
    n = abs(n)
    while n:
        res = 10 * res + n % 10
        n //= 10
    if res < -range or res > range:
        return 0
    return factor * res


for n in [
    123, -123, 120, 0, 1534236469
]:
    print(main(n))
