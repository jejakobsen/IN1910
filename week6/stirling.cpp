#include <iostream>
#include <math.h> 
#include <cmath>
#include <vector>
using namespace std;

double stirling(int x) {
      return x*log(x)-x ;
}

int main () {
	vector<int> X{2,5,10,50,100,1000};
	cout << "Stirling approx.   " << "Exact value" << endl;
	for (int x: X){
        cout << stirling(x) <<"              " <<  lgamma(x+1) << endl;
	}
	return 0;
}