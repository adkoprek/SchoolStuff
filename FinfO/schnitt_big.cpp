#include <cstddef>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>


// This is my global helper function (usually in a .hpp)
template <typename  T>
void print_array(T* data, size_t size) {
    std::cout << "[";
    for (size_t i = 0; i < size; i++) {
        std::cout << data[i];
        if (i < (size - 1)) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}

size_t in_ordered_list(std::vector<uint64_t>* list, uint64_t element, size_t start) {
    size_t left = start;
    size_t right = list->size() - 1; 
    while (left <= right) {
        size_t middle = (left + right) / 2;
        if (element == list->at(middle)) return middle;
        else if (list->at(middle) < element) left = middle + 1;
        else if (list->at(middle) > element) right = middle - 1;
    
    }
    return -1;
}

std::vector<uint64_t> schnitt(std::vector<uint64_t> list_1, std::vector<uint64_t> list_2) {
    std::vector<uint64_t>* list_1_ptr = &list_1;
    std::vector<uint64_t>* list_2_ptr = &list_2;
    if (list_1.size() > list_2.size()) std::swap(list_1_ptr, list_2_ptr);
    std::vector<uint64_t> output;
    size_t last_index = 0;
    
    for (const uint64_t element : *list_1_ptr) {
        size_t index = in_ordered_list(list_2_ptr, element, last_index);
        if (index != -1) {
            output.push_back(element);
            last_index = index;
        }
    }
    
    return output;
}

int main() {
    // Some dummy data
    std::vector<uint64_t> list_1 { 0, 2, 5, 6, 8, 10, 14 }; 
    std::vector<uint64_t> list_2 { 1, 2, 5, 4, 9, 10 }; 
    auto output = schnitt(list_1, list_2);
    print_array<uint64_t>(output.data(), output.size());
}
