# T=nlogn,S=n
def main(trips, capacity):
    time = []
    for change, start, end in trips:
        time.append((start, change))
        time.append((end, -change))
    time.sort()
    for _, change in time:
        capacity -= change
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
