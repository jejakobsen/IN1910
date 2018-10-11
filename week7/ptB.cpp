#include <iostream>
#include <cmath>

using namespace std;

struct CartPos {
    double x;
    double y;
};

class AffineTransform {
private:
    double a;
    double b;
    double c;
    double d;
    double e;
    double f;

public:
    AffineTransform(double A, double B, double C, double D, double E, double F) {
        a = A;
        b = B;
        c = C;
        d = D;
        e = E;
        f = F;
    }

    AffineTransform(double A, double B, double C, double D) {
        a = A;
        b = B;
        c = C;
        d = D;
        e = 0;
        f = 0;
    }    

    CartPos Transform(CartPos u) {
    	CartPos affined;
    	affined.x = a*u.x + b*u.y + e;
    	affined.y = c*u.x + d*u.y + f;
    	return affined;
    }
};

int main () {
	AffineTransform AT1(1,2,3,4);
	AffineTransform AT(1,2,3,4,5,6);
	CartPos pos{5,4};
    cout << pos.x << " " << pos.y << endl;
    cout << AT1.Transform(pos).x << " " << AT1.Transform(pos).y << endl;
	cout << AT.Transform(pos).x << " " << AT.Transform(pos).y << endl;

    return 0;
}