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
