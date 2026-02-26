#include <cstddef>
#include <cstdint>
#include <utility>
#include "helper.hpp"


void even_odd(uint64_t* data, size_t lenght) {
    size_t even_ptr = 0;
    size_t odd_ptr = lenght - 1;
    while (even_ptr < odd_ptr) {
        if (!(data[even_ptr] % 2)) even_ptr++;
        else {
            std::swap(data[even_ptr], data[odd_ptr--]);
        }
    }
}

int main() {
    uint64_t data[] = {0, 4, 3, 6, 18, 20, 70};
    size_t size = sizeof(data) / sizeof(uint64_t);
    even_odd(data, size);
    print_array(data, size);
}
