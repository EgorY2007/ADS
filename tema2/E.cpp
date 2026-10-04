#include <iostream>
#include <vector>

using namespace std;

bool good(const vector<int>& boxes, int k, int r){
	int cow_cnt = 1;
	int last_box = boxes[0];
	for (size_t i = 1; i < boxes.size(); ++i) {
        if (boxes[i] - last_box >= r) {
            cow_cnt++;
            last_box = boxes[i];
        }
    }
	return cow_cnt >= k;
}

int main(){
	vector<int> arr;
	int x, n, k;
	
	cin >> n >> k;
	while (cin >> x)
    {
    	arr.push_back(x);
    }
    
    int l = 0;
    int r = arr.back() - arr[0] + 1;
	while (r - l > 1){
		int m = (l + r) / 2;
		if (good(arr,k,m)){
			l = m;
		}
		else{
			r = m;
		}
	}
	cout << l;
}
