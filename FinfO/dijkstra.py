import heapq


def shortest_path(graph: list[list[tuple[int, int]]]) -> int:
    visited: list[bool] = [False for _ in range(len(graph))]
    d = [float('int') for _ in range(len(graph))]
    d[0] = 0
    q = []

    while q:
        current_distance, o = heapq.heappop(q)

        for c, weight in graph[o]:
            if d[c] > d[o] + weight:
                d[c] = d[o] + weight
                heapq.heappush(q, (d[c], weight))

    

    return 0
