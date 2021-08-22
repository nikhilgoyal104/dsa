def clean(p):
    i, n, res = 0, len(p), []
    while i < n:
        res.append(p[i])
        while i + 1 < n and p[i] == p[i + 1] == '*':
            i += 1
        i += 1
    return ''.join(res)


for p in [
    'a***b', 'a***b*****', '*', '**'
]:
    print(clean(p))
