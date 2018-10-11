#include <iostream>
#include <vector>
using namespace std;

int triangle(int n) {
    int triangle_nr = 0; 
	for (int i = 0; i<n+1; i++) {
        triangle_nr += i;
    }
    return triangle_nr;    
}

int main () {
	// Ignored code work if the other code is ignored out. 
	//vector<int> N{1,2,3,4,5};
	//for (int n: N) {
	//	cout << triangle(n) << endl;
	//}
	//cout << triangle(761) << " " << 761*(761+1)/2 << endl;
	int n;
	cout << "Please enter a number:";
	cin >> n;
	cout << triangle(n) << endl;

	return 0;
}