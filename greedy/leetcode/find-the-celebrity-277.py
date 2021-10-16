def knows(a, b):
    return True


def isCeleb(candidate, n):
    for person in range(n):
        if candidate == person:
            continue
        if knows(candidate, person) or not knows(person, candidate):
            return False
    return True


# T=n²,S=1
def x(n):
    for person in range(n):
        if isCeleb(person, n):
            return person
    return -1


# T=n,S=1
def y(n):
    candidate = 0
    for person in range(1, n):
        if knows(candidate, person):
            candidate = person
    if isCeleb(candidate, n):
        return candidate
    return -1


for n in [
    4
]:
    print(x(n))
    print(y(n))
