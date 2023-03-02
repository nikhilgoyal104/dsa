graph = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
]


def knows(a, b):
    return graph[a][b]


def isCeleb(potentialCeleb, n):
    for person in range(n):
        if potentialCeleb == person:
            continue
        if knows(potentialCeleb, person) or not knows(person, potentialCeleb):
            return False
    return True


# T=n²,S=1
def main(n):
    for potentialCeleb in range(n):
        if isCeleb(potentialCeleb, n):
            return potentialCeleb
    return -1


print(main(3))


# T=n,S=1
def main(n):
    potentialCeleb = 0
    for person in range(1, n):
        if knows(potentialCeleb, person):
            potentialCeleb = person
    if isCeleb(potentialCeleb, n):
        return potentialCeleb
    return -1


print(main(3))
