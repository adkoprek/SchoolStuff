#include <cstdint>
#include <iostream>
#include <string>


std::string strong_password(std::string pass) {
    uint8_t i;
    for (i = 1; i < pass.length(); i++) {
        if (pass[i - 1] == pass[i]) {
            char new_char = (pass[i - 1] + pass[i]) % 26 + 'a';
            if (new_char == pass[i - 1] || new_char == pass[i]) 
                new_char = (new_char + 2 - 'a') % 26 + 'a';

            pass.insert(pass.begin() + i, new_char);
            break;
        }
    }

    if (i == pass.length()) {
        if (pass[0] == 'a') pass = 'b' + pass;
        else pass = 'a' + pass;
    }
    
    return pass;
}

int main() {
    std::string password = "password";
    password = strong_password(password);
    std::cout << password << std::endl;
}

