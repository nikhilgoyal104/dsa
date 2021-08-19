from math import inf

nums = [1, 2, 1, -5, 3, 4, -5, -1, -2]
firstMin, secondMin = inf, inf

for val in nums:
    if val < firstMin:
        secondMin, firstMin = firstMin, val
    elif val < secondMin:
        secondMin = val

print(firstMin, secondMin)

nums = [1, 2, 1, -5, 3, 4, -5, -1, -2]
firstMin, secondMin = inf, inf

for val in nums:
    if val < firstMin:
        secondMin, firstMin = firstMin, val
    elif firstMin < val < secondMin:
        secondMin = val

print(firstMin, secondMin)
