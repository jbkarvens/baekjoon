#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<int> kmp(string S, string W) {
	vector<int> T(W.size()+1, 0);
	int pos = 1, cnd = 0;
	T[0] = -1;
	while (pos < W.size()) {
		if (W[pos] == W[cnd])T[pos] = T[cnd];
		else {
			T[pos] = cnd;
			while (cnd >= 0 and W[pos] != W[cnd])cnd = T[cnd];
		}
		++pos;
		++cnd;
	}
	T[pos] = cnd;

	int j = 0, k = 0;
	vector<int> P;
	while (j < S.size()) {
		if (W[k] == S[j]) {
			++j;
			++k;
			if (k == W.size()) {
				P.push_back(j - k);
				k = T[k];
			}
		}
		else {
			k = T[k];
				if (k < 0) {
					++j;
					++k;
				}
		}
	}
	return P;
}
int main() {
	string T,P;
	getline(cin, T);
	getline(cin, P);
	vector<int> res;
	res = kmp(T, P);
	for (int i = 0; i < res.size(); i++)
		++res[i];
	cout << res.size() << endl;
	for (int i = 0; i < res.size(); i++) {
		cout << res[i];
		if (i < res.size() - 1)
			cout << " ";
	}
	cout << endl;
	return 0;
}