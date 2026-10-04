#include <iostream>

using namespace std;

bool good(int cnt, int q, int s, int t){
	return t / q + t / s >= cnt;
}

int main(){
	int n, quick, slow;
	
	cin >> n >> quick >> slow;
	if (quick > slow){
		int temp = quick;
		quick = slow;
		slow = temp;
	}
	
	int l = 0;
	int r = (n-1) * slow;
	while (r - l > 1){
		int m = (r+l) / 2;
		if (not good(n - 1, quick, slow, m)){
			l = m;
		}
		else{
			r = m;
		}
	}
	cout << r + quick;
}
