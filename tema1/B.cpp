#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& arr){
	int n;
	n = arr.size();
	
	for (int i = 1; i < n; i++){
		int key = arr[i];
		int j = i;
		
		while (j >= 1 and arr[j-1] > key){
			arr[j] = arr[j - 1];
            j -= 1;
		}
		arr[j] = key;
	}
}
int main(){
	vector<int> arr;
	int x;
	
    while (cin >> x)
    {
        arr.push_back(x);
    }

	InsertionSort(arr);
	
	for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
}
