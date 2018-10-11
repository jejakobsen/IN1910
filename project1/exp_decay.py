from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay:
    def __init__(self, a):
        """
        a -- decay constant
        """
        self.a = a

    def __call__(self, t, u):
        """Return the derivative of u."""
        return np.round(-self.a*u, 6)

    def solve(self, u0, T, dt):
        """
        Solves differential equation, and returns the time and velocity as arrays.
        """
        diff = self.__call__
        t_points = list(np.linspace(0.0, T, T/dt))
        sol = solve_ivp(diff, (0.0, T), u0, t_eval = t_points)
        t = sol.t; u = sol.y[0]
        return t, u

if __name__ == '__main__':
    # Example run with some different values of a, u0, T and dt. Plotting values.
    a = 0.4
    u0 = [[1.1],[2.2],[3.3]]
    T = 10.0
    dt = 0.1
    decay_model = ExponentialDecay(a)
    for elem in u0:
        t,u = decay_model.solve(elem,T,dt)
        plt.plot(t, u)
    plt.show()
