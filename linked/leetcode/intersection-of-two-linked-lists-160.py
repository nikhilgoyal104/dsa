from linked.util import intersected

inputs = []

for intersectVal, listA, listB, skipA, skipB in [
    (8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3),
    (2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1),
    (0, [2, 6, 4], [1, 5], 3, 2)
]:
    headA, headB = intersected(intersectVal, listA, listB, skipA, skipB)
    inputs.append((headA, headB))


# T=m+n,S=m
def main(headA, headB):
    seen = set()
    tempA = headA
    tempB = headB
    while tempA:
        seen.add(tempA)
        tempA = tempA.next
    while tempB:
        if tempB in seen:
            return tempB
        tempB = tempB.next
    return None


for headA, headB in inputs:
    print(main(headA, headB))


def getSize(head):
    temp = head
    size = 0
    while temp:
        size += 1
        temp = temp.next
    return size


# T=m+n,S=1
def main(headA, headB):
    sizeA = getSize(headA)
    sizeB = getSize(headB)
    tempA = headA
    tempB = headB
    if sizeA > sizeB:
        for _ in range(sizeA - sizeB):
            tempA = tempA.next
    else:
        for _ in range(sizeB - sizeA):
            tempB = tempB.next
    while tempA and tempB:
        if tempA == tempB:
            return tempA
        tempA = tempA.next
        tempB = tempB.next
    return None


for headA, headB in inputs:
    print(main(headA, headB))
