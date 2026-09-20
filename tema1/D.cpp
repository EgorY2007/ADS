#include <iostream>
#include <vector>

using namespace std;

int BubbleSort(vector<int>& vec){
    int n;
    n = vec.size();
	int count = 0;
	
    for(int i = 0; i < n - 1; i++){
        bool swapped = false;
        for(int j = 0; j < n - 1; j++){
            if(vec[j] > vec[j+1]){
                swap(vec[j],vec[j+1]);
                swapped = true;
                count++;
            }
        }
        if(!swapped) {
            break;
        }
    }
    return count;
}

int main(){
    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    cout << BubbleSort(arr) << endl;
}
