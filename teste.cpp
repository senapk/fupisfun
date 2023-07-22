#include <iostream>
#include <limits>
#include <climits>


int main() {
    //initialize value with INT_MAX
    unsigned int value = UINT_MAX;
    std::cout << "value: " << value << std::endl;
    value += 1;
    std::cout << "value: " << value << std::endl;
}