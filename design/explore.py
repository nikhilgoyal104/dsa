import random

print(random.randint(1, 5))
random.choice([1, 2, 3, 4, 5])
print(random.choice(list({1, 2, 3})))

a = [8, 12, 17, 91, 24]

print(any([1, 3, 4]))

nums = [7, 2, 5, 9]
hm = {
    7: 0,
    2: 1,
    5: 2,
    9: 3
}

print(nums)
print(hm)

val = 2
last = nums[-1]
index = hm[val]
nums[index] = last
hm[last] = index
nums.pop()
del hm[val]

print(nums)
print(hm)
