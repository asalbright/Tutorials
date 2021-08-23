#include <iostream>     // this allows us to input and output from terminal
using namespace std;    // inside iostream there are different namespaces (different sections)

// function main which returns an integer
// needs to be called main, calling it something else will result in an error
int main() {
    // becaue we used namespace std we can use cout
    //otherwise std::cout <<
    cout << "Hello World!\n" << "This is something else." << endl << endl;
    // ; is a line terminator, removing it adds lines together basically
    // you dont actually need the return for the main function though it is good practice
    return 0;
}