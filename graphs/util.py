from collections import defaultdict


def build(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def build2(n, edges):
    graph = {i: [] for i in range(n)}
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def build3(n, edges):
    graph = {i: [] for i in range(n)}
    for src, dest in edges:
        graph[src].append(dest)
    return graph


def build4(n, edges):
    graph = {i: [] for i in range(n)}
    for src, dest, cost in edges:
        graph[src].append((dest, cost))
        graph[dest].append((src, cost))
    return graph


def build5(edges):
    graph = defaultdict(list)
    for src, dest, cost in edges:
        graph[src].append((dest, cost))
        graph[dest].append((src, cost))
    return graph


def build6(grid):
    graph = defaultdict(list)
    m, n = len(grid), len(grid[0])
    for ri in range(m):
        for ci in range(n):
            cost = grid[ri][ci]
            if cost:
                graph[ri].append((ci, cost))
    return graph


def build7(edges, directed):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        if not directed:
            graph[dest].append(src)
    return graph
