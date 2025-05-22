// loop_with_break.cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 3; i++) {
        switch (i) {
            case 1:
                cout << "i is 1" << endl;
                break;
            case 2:
                cout << "i is 2" << endl;
                break;
            case 3:
                cout << "i is 3" << endl;
                break;
            default:
                cout << "i is something else" << endl;
        }
        break; // Exit the loop after first iteration
    }

    return 0;
}