#include <iostream>
#include <cmath>
#include <map>

using namespace std;

class Polynomial {
private: 
	map<int,double> coefficients;

public:
    Polynomial(map<int,double> c) {
    	coefficients = c;
    }	

    double evaluate(double x) {
    	double s = 0.0;
	for (pair<int, double> element:coefficients) {
         s += element.second*pow(x,element.first);
    }
        
        return s;    	
    }
    void print() {
	    int max_key = 0;
	    for (pair<int, double> element:coefficients) {
	    	int test_key = element.first;
	    	if (test_key>max_key) {
	    		max_key = test_key;
	    	}
	    }
	    cout << "P(x)=";	
		for (pair<int, double> element:coefficients) {
			if (element.first==0) {
			    cout << element.second << "+";
			}
	        else if(element.first==1) {
	        	cout << element.second << "x+";
	        }
	        else if(element.first<max_key) {
	            cout << element.second << "x^(" << element.first << ")+";
	        }
	        else if(element.first==max_key) {
	        	cout << element.second << "x^(" << element.first << ")";
	        }
	    }   
	        cout << endl; 	
        return;
    };
};

int main () {
	map<int,double> c;
	c[10] = 1;
	c[5] = -5;
	c[0] = 1;
	Polynomial poly{c};
	cout << poly.evaluate(-2) << endl;
	cout << poly.evaluate(0) << endl;
	cout << poly.evaluate(2) << endl;
    poly.print();
    
	return 0;
}