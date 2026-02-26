#pragma once
#include <cstddef>
#include <iostream>


template <typename  T>
void print_array(T* data, size_t size) {
    std::cout << "[";
    for (size_t i = 0; i < size; i++) {
        std::cout << data[i];
        if (i < (size - 1)) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}
