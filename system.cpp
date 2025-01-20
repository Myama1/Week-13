#include "system.h"
#include <iostream>

System::System() {
    std::cout << "I am constructing the System!" <<std::endl;
}

void System::updateRule(){
    std::cout << "Updating the system..." <<std::endl;
}