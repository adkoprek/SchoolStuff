#include <cmath>
#include <cstddef>
#include <iostream>
#include <sys/types.h>

#define uint unsigned long long


int main() {
    uint test_cases;
    std::cin >> test_cases;

    uint data[test_cases];
    for (size_t i = 0; i < test_cases; i++) std::cin >> data[i];

    std::cout << std::fixed;
    for (size_t i = 0; i < test_cases; i++) {
        uint exponent = 0;
        while (data[i] >= 4) {
            data[i] = data[i] >> 2;
            exponent++;
        }
        std::cout << (uint)(std::pow(2, exponent)) << std::endl;
    }
}
