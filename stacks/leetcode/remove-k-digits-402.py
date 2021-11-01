# T=n,S=n
def main(num, k):
    if len(num) == k:
        return '0'
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k:
        stack.pop()
        k -= 1
    output = ''.join(stack)
    return output.lstrip('0') or '0'


for num, k in [
    ('12345264', 4),
    ('1432219', 3),
    ('10200', 1),
    ('10', 2),
    ('112', 1),
    ('10', 1),
    ('100', 1)
]:
    print(main(num, k))
