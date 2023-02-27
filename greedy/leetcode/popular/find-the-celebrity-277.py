def knows(a, b):
    return True


def isCeleb(potentialCeleb, n):
    for person in range(n):
        if potentialCeleb != person and (knows(potentialCeleb, person) or not knows(person, potentialCeleb)):
            return False
    return True


# T=n²,S=1
def x(n):
    for potentialCeleb in range(n):
        if isCeleb(potentialCeleb, n):
            return potentialCeleb
    return -1


# T=n,S=1
def y(n):
    potentialCeleb = 0
    for person in range(1, n):
        if knows(potentialCeleb, person):
            potentialCeleb = person
    if isCeleb(potentialCeleb, n):
        return potentialCeleb
    return -1


for n in [
    4
]:
    print(x(n))
    print(y(n))
