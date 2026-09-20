#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& arr) {
    int n;
	n = arr.size();
    
    for (int i = 0; i < n - 1; ++i) {
        int key = arr[i];
        int ind = i;

        for (int j = i + 1; j < n; ++j) {
            if (arr[j] > key) {
                key = arr[j];
                ind = j;
            }
        }

        if (i != ind) {
            swap(arr[i], arr[ind]);
        }
    }
}

int main() {
	vector<int> arr;
	int x;
	
    while (cin >> x)
    {
        arr.push_back(x);
    }

	SelectionSort(arr);
	
	for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
}
