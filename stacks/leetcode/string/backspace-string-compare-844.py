def process(s):
    res = []
    for char in s:
        if char != '#':
            res.append(char)
        elif res:
            res.pop()
    return res


# T=m+n,S=m+n
def main(s, t):
    return process(s) == process(t)


for s, t in [
    ('ab#c', 'ad#c'),
    ('ab##', 'c#d#'),
    ('a##c', '#a#c'),
    ('a#c', 'b'),
    ('y#fo##f', 'y#f#o##f')
]:
    print(main(s, t))
