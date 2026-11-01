#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    priority_queue<int> h;
    string cmd;

    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            h = priority_queue<int>();
        } 
        else if (cmd == "ADD") {
            int n;
            cin >> n;
            h.push(n);
        } 
        else if (cmd == "EXTRACT") {
            if (h.empty()) {
                cout << "CANNOT\n";
            } else {
                cout << h.top() << "\n";
                h.pop();
            }
        }
    }
    return 0;
}
