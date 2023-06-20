#include <iostream>
#include <vector>
#include<string>
using namespace std;
int find(vector<int>& arr,int left,int right, int x,bool mode=true) {
	if (right < left)
		return -1;
	int low, high;
	low = left;
	high = right;
	if (mode and arr[high] < x)
		return -1;
	if (not mode and arr[low] > x)
		return -1;
	while (low <= high) {
		int mid = (low + high) / 2;
		if (mode)
			if (arr[mid] < x)
				low = mid + 1;
			else
				high = mid - 1;
		else
			if (arr[mid] > x)
				high = mid - 1;
			else
				low = mid + 1;
	}
	return mode ? low : high;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N, Q;
	cin >> N >> Q;
	string sen;
	cin >> sen;
	vector<int> R, B;
	for (int i = 0; i < N; i++)
	{
		if (sen[i] == 'R')
			R.push_back(i);
		else if (sen[i] == 'B')
			B.push_back(i);
	}
	for (int i = 0; i < Q; i++)
	{
		int u, v;
		cin >> u >> v;
		int a, b, c, d;
		a = find(R, 0, R.size() - 1, u, true);
		d = find(B, 0, B.size() - 1, v, false);
		b = a + 1;
		c = d - 1;
		if (a <0 or b <0 or a>=R.size() or d>=B.size() or b >= R.size() or c<0 or R[b] > B[c]) {
			cout << to_string(-1)+"\n";
			continue;
		}
		else
			cout << to_string(R[a]) + " " + to_string(R[b]) + " " + to_string(B[c]) + " " + to_string(B[d]) + "\n";
	}
}