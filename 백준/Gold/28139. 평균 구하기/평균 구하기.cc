#include <iostream>
#include <vector>
#include<math.h>
using namespace std;
int main() {
	int N;
	cin >> N;
	vector<int> x, y;
	long double d = 0;
	for (int i = 0; i < N; i++)
	{
		int u, v;
		cin >> u >> v;
		x.push_back(u);
		y.push_back(v);
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = i+1; j < N; j++)
		{
			d += sqrt(pow(x[i] - x[j],2) + pow(y[i] - y[j],2));
		}
	}
	d = (d*2)/N;
	cout.precision(10);
	cout << d;
}