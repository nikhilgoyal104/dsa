# T=logn,S=1
def main(n):
    res, quot = 0, abs(n)
    while quot:
        quot, rem = divmod(quot, 10)
        res = 10 * res + rem
    if res < -2 ** 31 or res > 2 ** 31 - 1:
        return 0
    return res if n > 0 else -res


for n in [
    123, -123, 120, 0, 1534236469
]:
    print(main(n))
