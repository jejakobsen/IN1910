import nose.tools as nt
from pendulum import Pendulum, DampenedPendulum
from math import pi, sqrt
import numpy as np

def test_call():
    """Tests call method"""
    p = Pendulum(L=2.2)
    theta1, omega1 = p(0.0,[pi/4,0.1])
    nt.assert_equal(theta1,0.1)
    nt.assert_equal(omega1,-9.81/(2.2*sqrt(2)))
    theta2, omega2 = p(0.0,[0.0,0.0])
    nt.assert_equal(theta2,0.0)
    nt.assert_equal(omega2,0.0)

def test_solve():
    """Tests solve method"""
    p = Pendulum(L=2.2)
    T = 10.0; dt = 0.01; y = [0,0]
    p.solve(y,T,dt,angles="rad")
    theta = p.theta; omega = p.omega; t = p.t
    t_test = np.linspace(0,T,T/dt)
    for i in range(len(list(t_test))):
        nt.assert_equal(t[i],t_test[i])
        nt.assert_equal(theta[i],0)
        nt.assert_equal(omega[i],0)

@nt.raises(AttributeError)
def test_raise_theta():
    """Tests if AttributeError is raised when property theta is called without solve"""
    p = Pendulum(L=2.2)
    p.theta

@nt.raises(AttributeError)
def test_raise_omega():
    """Tests if AttributeError is raised when property omega is called without solve"""
    p = Pendulum(L=2.2)
    p.omega

@nt.raises(AttributeError)
def test_raise_t():
    """Tests if AttributeError is raised when property t is called without solve"""
    p = Pendulum(L=2.2)
    p.t    

def test_xy():
    """Tests if the length of the vector from (0,0) to pos (x,y) is equal to radius (L), at all times"""
    p = Pendulum(L=2.2)
    T = 10.0; dt = 0.01; y = [pi/4,0.1]
    p.solve(y,T,dt,angles="rad")
    r_squared = p.x**2 + p.y**2
    for i in range(len(list(r_squared))):
        nt.assert_almost_equal(r_squared[i],2.2**2)        

test_call()
test_solve()
test_raise_theta()
test_raise_omega()
test_raise_t()
test_xy()

if __name__ == "__main__":
    import nose
    nose.run()
