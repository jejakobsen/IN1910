import nose.tools as nt
from double_pendulum import DoublePendulum
from math import pi
import numpy as np

def test_call():
    """Tests the call method"""
    dp = DoublePendulum()
    theta1, omega1, theta2, omega2 = dp(0.0,[0.0,0.0,0.0,0.0])
    nt.assert_equal(theta1,0.0)
    nt.assert_equal(omega1,0.0)
    nt.assert_equal(theta2,0.0)
    nt.assert_equal(omega2,0.0)    

def test_solve():
    """Tests the solve method"""
    dp = DoublePendulum()
    T = 10.0; dt = 0.01; y = [0.0,0.0,0.0,0.0]
    dp.solve(y,T,dt,angles="rad")
    theta1 = dp.theta1; theta2 = dp.theta2; t = dp.t
    t_test = np.linspace(0,T,T/dt)
    for i in range(len(list(t_test))):
        nt.assert_equal(t[i],t_test[i])
        nt.assert_equal(theta1[i],0.0)
        nt.assert_equal(theta2[i],0.0)  

@nt.raises(AttributeError)
def test_raise_theta1():
    """Tests if AttributeError is raised when property theta1 is called without solve"""
    dp = DoublePendulum()
    dp.theta1

@nt.raises(AttributeError)
def test_raise_theta2():
    """Tests if AttributeError is raised when property theta2 is called without solve"""
    dp = DoublePendulum()
    dp.theta2

@nt.raises(AttributeError)
def test_raise_t():
    """Tests if AttributeError is raised when property t is called without solve"""
    dp = DoublePendulum()
    dp.t    

def test_total_energy():
    """Tests if the initial total energy is equal to the total energy at the endtime"""
    dp = DoublePendulum()
    T = 10.0; dt = 0.01; y = [pi/4,0.2,pi/2,-0.5]
    dp.solve(y,T,dt,angles='rad')
    nt.assert_almost_equal(dp.kinetic[0]+dp.potential[0],dp.kinetic[-2]+dp.potential[-2],1)

test_call()    
test_solve()
test_raise_theta1()
test_raise_theta2()
test_raise_t()
test_total_energy()

if __name__ == "__main__":
    import nose
    nose.run()