# T=n,S=n
def main(s):
    res = []
    for char in s:
        if res and res[-1] == char:
            res.pop()
        else:
            res.append(char)
    return ''.join(res)


for s in [
    'abbaca', 'azxxzy'
]:
    print(main(s))
