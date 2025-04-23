#include <iostream> 
#include <cmath>
 
void arithmeticCalculator(){
     double num1;
     double num2;
     double result;
     char op;
 
 
     std::cout << "****** Calculator ******";
     std::cout << "Arithemetic Calculator\n";
 
     std::cout << "Enter #1: ";
     std::cin >> num1;
 
     std::cout << "Enter operator(+ - * /): ";
     std::cin >> op;
 
     std::cout << "Enter #2: ";
     std::cin >> num2;
 
     switch(){
         case '+':
             result = num1 + num2;
             std::cout << result;
             break;
         case '-':
             result = num1 - num2;
             std::cout << result;
             break;
         case '*':
             result = num1 * num2;
             std::cout << result;
             break;
         case '/':
 @@ -39,17 +39,28 @@
         default:
             std::cout << "Enter a valid response"
     }
     
     
     
     
     
     std::cout << "************************"
 }
 
 int main(){
 
     calculator();
     
     std::string calcType;
 
     std::cout << "****** Calculator Terminal ******\n";
 
     std::cout << "Enter calculator type (arithmetic, algebra): ";
     std::cin >> calcType;
 
     if(calcType = arithmetic){
         arithmeticCalculator();
     }
     else if(calcType = algebra){
         std::cout << "Still developing this feature\n"
     }
     else{
         std::cout << "Enter a valid response\n"
     }
 
     std::cout << "*********************************";
     
     return 0;
 }
