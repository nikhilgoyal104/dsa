from math import inf


# T=n,S=1
def main(s):
    res = ones = 0
    for char in s:
        if char == '1':
            ones += 1
        else:
            res = min(ones, res + 1)
    return res


for s in [
    '00110',
    '010110',
    '00011000'
]:
    print(main(s))
