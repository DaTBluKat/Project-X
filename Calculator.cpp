#include <iostream> 
#include <cmath>
#include <string>

double arithmeticCalculator();
std::string algebraCalculator();

int main(){
     
    int code;
 
    std::cout << "****** Terminal ******\n";
 
    std::cout << "Enter the code for your chosen destination: ";
    std::cin >> code;
 
    if(code == 1234){
        arithmeticCalculator();
    }
    else if(code == 5678){
        algebraCalculator();
    }
    else{
        std::cout << "Enter an approved code\n";
    }
 
    std::cout << "*********************************";
     
    return 0;
}

double arithmeticCalculator(){
    double num1;
    double num2;
    double result;
    char op;

    std::cout << "Enter #1: ";
    std::cin >> num1;

    std::cout << "Enter op: ";
    std::cin >> op;
    
    std::cout << "Enter #2: ";
    std::cin >> num2;

    switch(op){
        case '+':
            result = num1 + num2;
            std::cout << result << '\n';
            break;
        case '-':
            result = num1 - num2;
            std::cout << result << '\n';
            break;
        case '*':
            result = num1 * num2;
            std::cout << result << '\n';
            break;
        case '/':
            result = num1 / num2;
            std::cout << result << '\n';
            break;
        default:
            std::cout << "Enter a valid response" << '\n';
    }

    std::cout << "************************";

    return result;
}

std::string algebraCalculator(){
    
    std::string equation;
    std::string result;

    std::cout << "Enter equation: ";
    std::cin >> equation;

    std::cout << equation.length() << '\n';
            
    return equation;
}
