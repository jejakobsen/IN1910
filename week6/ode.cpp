#include <iostream>

using namespace std;

int main () {
	double u[10001] ={15.7};
	double t[10001] = {0.0};
	double a = 4.3;
	double dt = 0.001;
	int N = 10001;
	for (int i=0; i<N; i++) {
       t[i+1] = t[i] + dt;
       u[i+1] = u[i] - a*u[i]*dt;
       cout << u[i] << endl;  
   }
}