def into_2d_array(tree_graph: list[int]) -> list[list[int]]:
    output = [[] for _ in range(len(tree_graph))]

    for i, node in enumerate(tree_graph):
        if node == -1:
            continue

        output[node].append(i)

    return output


if __name__ == '__main__':
    tree_graph = [-1, 0, 0, 1, 2, 2, 11, 4, 5, 5, 5, 1, 1, 10, 12, 9, 9]
    result = into_2d_array(tree_graph)
    print(result)
