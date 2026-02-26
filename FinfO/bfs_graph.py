class Node:
    visited: bool
    dicovered_from: int
    name: int

    def __init__(self, name: int):
        self.name = name
        self.visited = False
        self.dicovered_from = -1

if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        n, m = map(int, input().split())
        graph: dict[Node, list[Node]] = {}
        for i in range(n):
            graph[Node(i)] = []
        for i in range(m):

