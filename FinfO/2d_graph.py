def into_tree_graph(graph: list[list[int]]) -> list[int] | None:
    output = [-1 for _ in range(len(graph))]

    for node, children in enumerate(graph):
        for child in children:
            output[child] = node

    return output

if __name__ == '__main__':
    input = [[1, 2], [3, 11, 12], [4, 5], [], [7], [8, 9, 10], 
             [], [], [], [15, 16], [13], [6], [14], [], [], [], []]
    result = into_tree_graph(input)
    print(result)
