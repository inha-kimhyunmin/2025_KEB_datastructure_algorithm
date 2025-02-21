#include <iostream>
#include <vector>
using namespace std;


int main() {

	vector<int> v;
	vector<int> a;
	int k, n;
	int startpoint, endpoint;

	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		v.push_back(i+1);
	}

	startpoint = 0; //시작점 0으로 설정
	while (v.empty() != true) {
		endpoint = ((startpoint + k - 1) % v.size());
		a.push_back(v.at(endpoint));
		startpoint = endpoint;
		v.erase(v.begin() + endpoint);
	}
	
	cout << "<";
	for (auto it = a.begin(); it < a.end(); it++) {
		cout << *it;
		if (it < a.end() - 1) {
			cout << ", ";
		}
	}
	cout << ">";
	return 0;
}
