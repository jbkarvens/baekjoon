#include <iostream>
#include <string>
using namespace std;
int main() {
	string line;
	while (true) {
		getline(cin, line);
		if (line == "")
			break;
		cout << line << endl;
	}
	return 0;
}