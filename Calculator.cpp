#include <iostream> 
#include <cmath>

double arithmeticCalculator();
std::string algebraCalculator();
void passcodeVerifier();

int main(){

    passcodeVer`ifier();
     
    std::string code;
 
    std::cout << "****** Terminal ******\n";
 
    std::cout << "Enter the code for your chosen destination: ";
    std::cin >> code;
 
    if(code == 1234){
        arithmeticCalculator();
    }
    else if(code == 123xyz){
        algebraCalculator();
    }
    else{
        std::cout << "Enter an approved code\n"
    }
 
    std::cout << "*********************************";
     
    return 0;
}

double arithmeticCalculator(){
    double num1;
    double num2;
    double result;
    std::string enteredCode;

    do{
        std::cout << "Enter code: ";
        std::cin >> enteredCode;
    }
    while(enteredCode != "1+1" || enteredCode != "1-1" || enteredCode != "1*1" || enteredCode != "1/1")

    std::cout << "Enter #1: ";
    std::cin >> num1;
    
    std::cout << "Enter #2: ";
    std::cin >> num2;

    switch(enteredCode){
        case '1+1':
            result = num1 + num2;
            std::cout << result;
            break;
        case '1-1':
            result = num1 - num2;
            std::cout << result;
            break;
        case '1*1':
            result = num1 * num2;
            std::cout << result;
            break;
        case '1/1':
            result = num1 / num2;
            std::cout << result;
            break;
        default:
            std::cout << "Enter a valid response";
    }

    std::cout << "************************";

    return result;
}

std::string algebraCalculator(){
    std::string equation;
    std::string result;
    int varNum;
    std::string var1;
    std::string var2;
    std::string var3;
    std::string var4;
    std::string var5;
    std::string var6;


    std::cout << "Number of variables(Max: 6): ";
    std::cin >> varNum;

    std::cout << "Enter equation: ";
    std::cin >> equation;

    std::cout << "Enter coefficient with variable\n";

    switch(varNum){
        case 1:
            std::cout << "Enter your variable: ";
            std::cin >> var1;
        case 2:
            std::cout << "Enter variable 1: ";
            std::cin >> var1;
            std::cout << "Enter variable 2: ";
            std::cin >> var2
        case 3:
            std::cout << "Enter variable 1: ";
            std::cin >> var1;
            std::cout << "Enter variable 2: ";
            std::cin >> var2;
            std::cout << "Enter variable 3: ";
            std::cin >> var3;
        case 4:
            std::cout << "Enter variable 1: ";
            std::cin >> var1;
            std::cout << "Enter variable 2: ";
            std::cin >> var2;
            std::cout << "Enter variable 3: ";
            std::cin >> var3;
            std::cout << "Enter variable 4: ";
            std::cin >> var4;
        case 5:
            std::cout << "Enter variable 1: ";
            std::cin >> var1;
            std::cout << "Enter variable 2: ";
            std::cin >> var2;
            std::cout << "Enter variable 3: ";
            std::cin >> var3;
            std::cout << "Enter variable 4: ";
            std::cin >> var4;
            std::cout << "Enter variable 5: ";
            std::cin >> var5;
        case 6:
            std::cout << "Enter variable 1: ";
            std::cin >> var1;
            std::cout << "Enter variable 2: ";
            std::cin >> var2;
            std::cout << "Enter variable 3: ";
            std::cin >> var3;
            std::cout << "Enter variable 4: ";
            std::cin >> var4;
            std::cout << "Enter variable 5: ";
            std::cin >> var5;
            std::cout << "Enter variable 6: ";
            std::cin >> var6;
    }

    return result;
}

void passcodeVerifier(){
    std::string passcode = skibidi rizz;
    std::string enteredPasscode; 

    do{
        std::cout << "Enter passcode: ";
        std::cin >> enteredPasscode;
    }
    while(enteredPasscode != passcode)
} 