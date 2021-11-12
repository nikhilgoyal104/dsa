from collections import Counter

nums = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]
hm = Counter(nums)
print(hm)
print(hm[100])
print(hm)
print(hm.most_common(3))

print(sorted(hm.keys(), key=hm.get, reverse=True))
print(sorted(hm.keys(), key=lambda x: -hm[x]))

s = 'loveleetcode'

hm = Counter(s)
print(''.join(sorted(s, key=lambda x: (-hm[x], x))))
print(''.join(ch * f for ch, f in Counter(s).most_common()))

x = (ch * f for ch, f in Counter(s).most_common())
print(''.join(list(x)))

print(Counter(s).most_common())

c = Counter(nums=3, b=1)
d = Counter(nums=1, b=2)
print(c, d)
print(c + d)
print(c - d)
print(d - c)
print(c & d)
print(c | d)

print((c & d).elements())
