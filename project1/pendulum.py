from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi
g = 9.81

class Pendulum:
    def __init__(self, L=1.0, M=1.0):
        """We're giving L(length) and M(mass) values."""
        self.L = L
        self.M = M

    def __call__(self, t, y):
        """
        Calculates and returns the derative of theta and omega as tuple.
        """
        L = self.L
        theta = y[0]; omega = y[1]
        return (omega, -(g/L)*sin(theta))

    def solve(self, y0, T, dt, angles):
        """
        Solves a differential equation and stores t, omega, theta as arrays
        """
        if angles == "deg":
            y[0] = y[0]*pi/180
            y[1] = y[1]*pi/180
        diff = self.__call__
        time_points = list(np.linspace(0,T,T/dt))
        sol = solve_ivp(diff, (0,T), y0, t_eval=time_points)
        self._theta = sol.y[0]; self._omega = sol.y[1]; self._t = sol.t

    @property
    def theta(self):
        """Returns theta as an array."""
        try:
            return self._theta
        except AttributeError:
            print('Method solve has to be called first.')
            raise

    @property
    def omega(self):
        """Returns omega as an array."""
        try:
            return self._omega
        except AttributeError:
            print('Method solve has to be called first.')
            raise

    @property
    def t(self):
        """Returns t as an array."""
        try:
            return self._t
        except AttributeError:
            print('Method solve has to be called first.')
            raise

    @property
    def x(self):
        """Calculates and returns position, x, as an array."""
        return np.sin(self._theta)*self.L

    @property
    def y(self):
        """Calculates and returns position, y, as an array."""
        return -np.cos(self._theta)*self.L

    @property
    def potential(self):
        """Calculates and returns potential energy as an array."""
        return self.M*g*(self.y + self.L)

    @property
    def vx(self):
        """Calculates and returns velocity, vx, as an array."""
        return np.gradient(self.x, self.t)

    @property
    def vy(self):
        """Calculates and returns velocity, vy, as an array."""
        return np.gradient(self.y, self.t)

    @property
    def kinetic(self):
        """Calculates and returns kinetic energy as an array."""
        return 0.5*self.M*(self.vy**2 + self.vx**2)

class DampenedPendulum(Pendulum):
    def __init__(self, L, M, B):
        """
        Extends __init__ with dampening parameter B.
        """
        super().__init__(L, M)
        self.B = B

    def __call__(self, t, y):
        """
        Override __call__, and returns the derivative of omega and theta as tuple.  
        """
        L, M, B = self.L, self.M, self.B
        theta = y[0]; omega = y[1]
        return (omega, -(g/L)*sin(theta) - (B/M)*omega)

if __name__ == '__main__':
    L = 2.2; M = 1.0; y = [pi/4, 0.1]
    p = Pendulum(L, M)
    T = 10.0; dt = 0.001
    p.solve(y, T, dt, angles="rad")

    # Plot of theta(t)
    plt.plot(p.t, p.theta)
    plt.xlabel('time [s]')
    plt.ylabel('theta [rad]')
    plt.title('theta(t)')
    plt.show()

    # Plot of energy
    plt.plot(p.t, p.potential, '-y', p.t, p.kinetic, '-g', p.t,
             p.potential + p.kinetic, '-b')
    plt.legend(['Potential', 'Kinetic', 'Total'])
    plt.title('E_p(t), E_k(t) and E_t(t)')
    plt.ylabel('energy [J]')
    plt.xlabel('time [s]')
    plt.show()

    # Plot of the energy of the Dampened Pendulum
    o = DampenedPendulum(L, M, 0.5)
    o.solve(y, T, dt, angles="rad")
    plt.plot(o.t, o.potential + o.kinetic)
    plt.xlabel('time [s]')
    plt.ylabel('energy [J]')
    plt.title('Dampended Pendulum, E_t(t)')
    plt.show()
