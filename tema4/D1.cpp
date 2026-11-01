#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Heap {
    vector<int> heap;
    int size;

public:
    Heap() {
        heap.push_back(0);
        size = 0;
    }

    void shift_up(int i) {
        while (i / 2 > 0 && heap[i] > heap[i / 2]) {
            swap(heap[i], heap[i / 2]);
            i = i / 2;
        }
    }

    void insert(int x) {
        heap.push_back(x);
        size += 1;
        shift_up(size);
    }

    int ind_max_child(int i) {
        if (i * 2 + 1 > size) return i * 2;
        if (heap[i * 2] > heap[i * 2 + 1]) return i * 2;
        return i * 2 + 1;
    }

    void shift_down(int i) {
        while (i * 2 <= size) {
            int j = ind_max_child(i);
            if (heap[i] < heap[j]) {
                swap(heap[i], heap[j]);
            }
            i = j;
        }
    }

    int del_max() {
        int removed = heap[1];
        heap[1] = heap[size];
        size = size - 1;
        heap.pop_back();
        shift_down(1);
        return removed;
    }

    void clear() {
        heap.clear();
        heap.push_back(0);
        size = 0;
    }

    bool empty() const {
        return size == 0;
    }
};

int main() {
    Heap h;
    string cmd;

    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            h.clear();
        } 
		else if (cmd == "ADD") {
            int n;
            cin >> n;
            h.insert(n);
        } 
		else if (cmd == "EXTRACT") {
            if (h.empty()) {
                cout << "CANNOT\n";
            } else {
                cout << h.del_max() << "\n";
            }
        }
    }
    return 0;
}
