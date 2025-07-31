# T=logn,S=1
def main(n):
    res = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n:
        lastDigit = n % 10
        res = 10 * res + lastDigit
        n //= 10
    if res < -2 ** 31 or res > 2 ** 31:
        return 0
    return sign * res


for n in [
    123, -123, 120, 0, 1534236469
]:
    print(main(n))
