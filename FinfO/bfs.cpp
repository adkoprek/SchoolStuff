#include <deque>
#include <vector>
#include "helper.hpp"


int main() {
    std::vector<int> tree { -1, 0, 0, 1, 1, 2, 2, 6, 4, 4 };
    std::deque<int> queue;
    queue.push_back(0);
    std::vector<int> visited;
    int index = 1;

    while (!queue.empty()) {
        int to_explore = queue.front();
        std::cout << "To Explore: " << to_explore << std::endl;
        queue.pop_front();
        visited.push_back(to_explore);
        while (tree[index] == to_explore) queue.push_back(index++);
    }
    
    print_array(visited.data(), visited.size());
}
