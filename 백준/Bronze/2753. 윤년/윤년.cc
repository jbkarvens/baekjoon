#include <iostream>
using namespace std;
int main(){
	int year, ans;
	cin >> year;
	if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
	{
		ans = 1;
	}
	else
		ans = 0;
	cout << ans;
}