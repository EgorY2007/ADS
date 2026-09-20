#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void CountSort(vector<int>& vec){
	int k = *max_element(vec.begin(), vec.end());
    vector<int> counter(k+1, 0);

    for (int x : vec) {
        counter[x]++;
    }

    vec.clear();

    for (int num = 0; num <= k; ++num) {
        vec.insert(vec.end(), counter[num], num);
    }
}

int main(){
    int x;
    vector<int> arr;
    
    while (cin >> x) {
        arr.push_back(x);
    }
    
 	CountSort(arr);
 	for(int i = 0; i < arr.size(); i++){
        cout << arr[i] << " ";
    }
}
