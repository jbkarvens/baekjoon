#include <iostream>
#include <string>
using namespace std;
int main() {
	long long int N, R;
	cin >> N >> R;
	long long int Q = N - R;
	if (Q <= R) {
		cout << 0;
		return 0;
	}
	long long int ans, m;
	ans = 0;
	m = 1;
	while (m * m <= Q) {
		if (Q % m == 0) {
			ans += m > R ? m : 0;
			ans+=(Q / m > R and Q/m!=m) ? Q / m : 0;
		}
		++m;
	}
	cout << ans;
	return 0;
}