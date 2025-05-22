// loop_without_break.cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 3; i++) {
        switch (i) {
            case 1:
                cout << "i is 1" << endl;

            case 2:
                cout << "i is 2" << endl;

            case 3:
                cout << "i is 3" << endl;

            default:
                cout << "i is something else" << endl;
        }
    }

    return 0;
}
