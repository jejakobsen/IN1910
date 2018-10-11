#include <iostream>
#include <vector>

using namespace std;

vector<double> linspace(double a, double b) {
    // Need to implement if-statement.
    int n = 50;
    double delta = (b-a)/n; 
    vector<double> ls;
    for (int i=0; i<n;i++) {
        ls.push_back(a+(i*delta));
    }    
    return ls;    
}


vector<double> linspace(double a, double b, int n) {
	// Need to implement if-statement.
	double delta = (b-a)/n; 
	vector<double> ls;
	for (int i=0; i<n;i++) {
        ls.push_back(a+(i*delta));
    }    
    return ls;    
}

int main(){
    vector<double> U = linspace(0.0,50.0);
    vector<double> L = linspace(0.0,50.0, 30);
    for (double l:L) {
    	cout << l << endl;

    }
    for (double u:U) {
        cout << u << endl;
    }
    cout << size(U) << endl;
    cout << size(L) << endl;
    return 0;
}