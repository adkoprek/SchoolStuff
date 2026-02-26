#include "helper.hpp"
#include <cstddef>
#include <cstdint>
#include <utility>


void dutch_national_flag(uint64_t* data, size_t size, uint64_t pivot) {
    size_t smaller_ptr = 0;
    size_t bigger_ptr = size - 1;
    while (smaller_ptr < bigger_ptr) {
        if (data[smaller_ptr] < pivot) smaller_ptr++;
        else std::swap(data[smaller_ptr], data[bigger_ptr--]);
    }

    smaller_ptr = bigger_ptr + 1;
    bigger_ptr = size - 1;
    while (smaller_ptr < bigger_ptr) {
        if (data[smaller_ptr] == pivot) smaller_ptr++; 
        else std::swap(data[smaller_ptr], data[bigger_ptr--]);
    }
}

int main() {
    uint64_t data[] = {0, 1, 0, 2, 1};
    uint64_t pivot = 1;
    size_t size = sizeof(data) / sizeof(uint64_t);
    dutch_national_flag(data, size, pivot);
    print_array(data, size);
}
