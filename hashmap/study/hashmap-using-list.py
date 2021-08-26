hm = [[] for _ in range(10)]


def put(key, val):
    bucket = hcode(key)
    for i, (k, _) in enumerate(hm[bucket]):
        if key == k:
            hm[bucket][i] = (key, val)
            return
    hm[bucket].append((key, val))


def get(key):
    for k, v in hm[hcode(key)]:
        if key == k:
            return v


def remove(key):
    bucket = hcode(key)
    for i, (k, _) in enumerate(hm[bucket]):
        if key == k:
            del hm[bucket][i]
            return


def hcode(key):
    return hash(key) % 10


put(10, 'Nepal')
put(25, 'USA')
put(26, 'India')
put(20, 'Iran')
put(20, 'Israel')
print(hm)
remove(20)
print(hm)
