nums = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
nums = filter(lambda x: x % 2 == 0, nums)
print(nums)
print(next(nums))
print(list(nums))

nums = map(lambda x: x % 2 == 0, nums)
print(list(nums))

nums = map(lambda x: x // 2, nums)
print(list(nums))

p = map(lambda x, y: x + y, (1, 2, 3), (4, 5, 6))
print(p)
print(list(p))

animals = ['dog', 'cat', 'parrot', 'rabbit']
animals = list(map(lambda animal: animal.upper(), animals))
print(animals)
