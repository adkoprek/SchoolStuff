#include <iostream>
#include <vector>

int main() {
    std::vector<std::vector<int>> matrix = {};
    int nodes, requests;
    std::cin >> nodes >> requests;

    for (int i = 0; i < nodes; i++) {
        std::vector<int> row(nodes, 0);
        matrix.push_back(row);
    }

    for (int i = 0; i < nodes; i++) {
        int num = 0;
        std::cin >> num;
        int temp = 0;
        for (int j = 0; j < num; j++) {
            std::cin >> temp;
            matrix[i][temp] = 1;
        }
    }

    for (int i = 0; i < requests; i++) {
        int from, to;
        std::cin >> from >> to;
        if (matrix[from][to] == 1) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}
