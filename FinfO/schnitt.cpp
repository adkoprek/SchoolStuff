#include "helper.hpp"
#include <cstddef>
#include <cstdint>
#include <vector>


std::vector<uint64_t> schnitt(std::vector<uint64_t> list_1, std::vector<uint64_t> list_2) {
    size_t index_1 = 0;
    size_t index_2 = 0;
    uint64_t last_element;
    std::vector<uint64_t> output;

    
    while (index_1 < list_1.size() || index_2 < list_2.size()) {
        if      (list_1[index_1] < list_2[index_2]) index_1++;
        else if (list_1[index_1] > list_2[index_2]) index_2++;
        else if (last_element != list_1[index_1]){
            last_element = list_1[index_1];
            output.push_back(list_1[index_1++]);
            index_2++;
        }

    }

    return output;
}

int main() {
    std::vector<uint64_t> list_1 { 0, 2, 5, 6, 8, 10, 14 }; 
    std::vector<uint64_t> list_2 { 1, 2, 5, 4, 9, 10 }; 
    auto output = schnitt(list_1, list_2);
    print_array(output.data(), output.size());
}
