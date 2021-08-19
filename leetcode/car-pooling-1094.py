def main(trips, capacity):
    lst = []
    for n, start, end in trips:
        lst.append((start, n))
        lst.append((end, -n))
    lst.sort()
    for pair in lst:
        capacity -= pair[1]
        if capacity < 0:
            return False
    return True


for trips, capacity in [
    ([[2, 1, 5], [3, 3, 7]], 4),
    ([[2, 1, 5], [3, 3, 7]], 5),
    ([[2, 1, 5], [3, 5, 7]], 3),
    ([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11),
]:
    print(main(trips, capacity))
