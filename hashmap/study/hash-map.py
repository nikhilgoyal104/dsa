hm = {'India': 135, 'China': 200, 'Pakistan': 30, 'US': 20, 'UK': 10}
print(hm)
print(hm.keys())
print(hm.values())
print(hm.items())

print(hm.pop('India'))
print(hm)
del hm['China']
print(hm)
print(hm.popitem())
print(hm)

print(dict.fromkeys([1, 2, 3, 4], 10))

hm.update(India=135, China=200)
print(hm)
hm.update([('x', 2), ('z', 3)])
print(hm)
hm['India'] = 140
print(hm)

print(hm.get('India'))
print(hm.get('Iran'))

print('Iraq' in hm)
print('Iran' in hm)
print('India' in hm)

for k, v in hm.items():
    print(k, v)

print(hash(10) % 10)
print(hash(30) % 10)
print(hash(31) % 10)
print(hash(5) % 10)
print(hash(15) % 10)

x = [1, 2, 3]
del x[1]
print(x)
