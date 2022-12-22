from binarytree import build2
from collections import defaultdict, deque

r1 = build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
r2 = build2([0, 1, None, 3, 2])
r3 = build2([1])

inputs = [
    (r1, r1.left, 2),
    (r2, r2.left.right, 1),
    (r3, r3, 3)
]


def getRootToNodePath(root, target):
    def dfs(root):
        if not root:
            return []
        if root == target:
            return [root]
        for child in [root.left, root.right]:
            path = dfs(child)
            if path:
                return [root] + path
        return []

    return dfs(root)


def getNodesKDistanceAway(root, blockedNode, k):
    def dfs(root, k):
        if not root or root is blockedNode:
            return []
        if not k:
            return [root.val]
        return dfs(root.left, k - 1) + dfs(root.right, k - 1)

    return dfs(root, k)


def main(root, target, k):
    res, blockedNode = [], None
    rootToNodePath = getRootToNodePath(root, target)
    while rootToNodePath and k > -1:
        node = rootToNodePath.pop()
        res += getNodesKDistanceAway(node, blockedNode, k)
        blockedNode = node
        k -= 1
    return res


for root, target, k in inputs:
    print(main(root, target, k))

print()


# T=n,S=n
def main(root, target, k):
    graph = defaultdict(list)

    def dfs(root, parent):
        if not root:
            return
        if parent:
            graph[root].append(parent)
            graph[parent].append(root)
        dfs(root.left, root)
        dfs(root.right, root)

    dfs(root, None)

    queue, vis = deque([(target, 0)]), {target}
    while queue:
        if queue[0][1] == k:
            return [node.val for node, _ in queue]
        node, dist = queue.popleft()
        for nbr in graph[node]:
            if nbr not in vis:
                vis.add(nbr)
                queue.append((nbr, dist + 1))
    return []


for root, target, k in inputs:
    print(main(root, target, k))
