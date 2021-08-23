#include <iostream>    
#include <string>
using namespace std;

/* 
Main Data Types
int:    3, -5, 35, -9083
float:  2.5, -0.1, 0.0001
bool:   true, flase
string: "Anything", "numbers1234" "x"
char:   'x', '1', '0'
*/

int main() {
    // cpp will try to apply the assigned value to the var so floats will become ints
    int x = 2;
    // var names cannot start with a number
    // standard naming convention is CamelCase not snake_case
    string y = "Dirtboy";
    cout << x << endl << y << endl;
    // you can intialize a var without assigning a value
    int z;
    z = 37;
    cout << z << endl;
    // initialize multi vars
    int a, b, c;
    return 0;
}