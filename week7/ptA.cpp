#include <iostream>
#include <cmath>

using namespace std;

struct CartPos {
    double x;
    double y;
};

struct PolarPos {
    double r;
    double theta;
};

PolarPos cart2polar(CartPos u) {
    PolarPos pol;
    pol.r = sqrt(u.x*u.x + u.y*u.y);
    pol.theta = atan(u.y/u.x);
    return pol;
}

CartPos polar2cart(PolarPos u) {
    CartPos cart;
    cart.x = u.r*cos(u.theta);
    cart.y = u.r*sin(u.theta);
    return cart;
}

PolarPos scale(PolarPos u, double s) {
	PolarPos scaled;
	scaled.r = u.r*s;
	scaled.theta = u.theta;
	return scaled;
}

CartPos scale(CartPos u, double s) {
	CartPos scaled;
	scaled.x = u.x*s;
	scaled.y = u.y*s;
	return scaled;
}

PolarPos rotate(PolarPos u, double omega) {
	PolarPos rotated;
	rotated.r = u.r;
	rotated.theta = u.theta + omega;
	return rotated; 
}

CartPos rotate(CartPos u, double omega) {
	CartPos rotated;
	rotated.x = u.x*cos(omega) + u.y*sin(omega);
	rotated.y = -u.y*sin(omega) + u.y*cos(omega);
	return rotated; 
}

int main () {
	CartPos u{5.0,4.0};
	PolarPos v{5.0,3.141592/6.0};
	double s = 2;
	double omega = 3.141592/4.0;
	cout << polar2cart(cart2polar(u)).x << polar2cart(cart2polar(u)).y << endl;
	cout << scale(v, s).r << endl;
	cout << scale(u, s).y << endl;
	cout << rotate(u, omega).x << rotate(u, omega).y << endl;
	cout << rotate(v, omega).r << rotate(v, omega).theta << endl;

	return 0;
}


