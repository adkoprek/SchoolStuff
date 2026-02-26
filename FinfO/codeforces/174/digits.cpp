#include <cmath>
#include <cstddef>
#include <iostream>
#include <sys/types.h>

#define uint unsigned long long

uint factorial(uint num) {
    if (num == 0) return 1;
    return num * factorial(num - 1);
}

uint num_builder(uint count, uint num) {
    if (count == 0) return num;
    return std::pow(10, count) * num + num_builder(count - 1, num);
}

int main() {
    uint test_cases;
    std::cin >> test_cases;

    uint count[test_cases];
    uint num[test_cases];
    for (size_t i = 0; i < test_cases; i++) std::cin >> count[i] >> num[i];

    std::cout << std::fixed;
    for (size_t i = 0; i < test_cases; i++) {
        if (count[i] > 7) count[i] = 7;

        uint entire_num = num_builder(count[i] - 1, num[i]);
        std::cout << "1 ";
        if (entire_num % 3 == 0) std::cout << "3 ";
        if (entire_num % 5 == 0) std::cout << "5 ";
        if (entire_num % 7 == 0) std::cout << "7 ";
        if (entire_num % 9 == 0) std::cout << "9 ";
        std::cout << std::endl;


        std::cout << std::endl;
    }
}
