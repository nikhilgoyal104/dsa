# T=nlogn,S=1
def main(boxTypes, truckSize):
    res = 0
    boxTypes.sort(key=lambda x: -x[1])
    for boxCount, unitsPerBox in boxTypes:
        boxes = min(truckSize, boxCount)
        res += boxes * unitsPerBox
        truckSize -= boxes
        if not truckSize:
            break
    return res


for boxTypes, truckSize in [
    ([[1, 3], [2, 2], [3, 1]], 4),
    ([[5, 10], [2, 5], [4, 7], [3, 9]], 10),
]:
    print(main(boxTypes, truckSize))
