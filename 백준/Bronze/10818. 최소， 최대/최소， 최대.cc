#include <iostream>
using namespace std;
int main() {
	int N;
	const int M = 1000000;
	cin >> N;
	int arr[M+1];
	int max,min;
	min = M+1;
	max = -(M+1);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		if (arr[i] < min)
			min = arr[i];
		if (arr[i] > max)
			max = arr[i];
	}
	cout << min << " " << max;
	return 0;
}