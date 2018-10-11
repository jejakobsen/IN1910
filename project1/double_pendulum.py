from math import pi, sin, cos
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.animation as animation

g = 9.81

class DoublePendulum:
    def __init__(self, M1=1.0, L1=1.0, M2=1.0, L2=1.0):
        """
        Stores the values M1, L1, M2 and L2

        M1 -- mass of pendulums first joint
        L1 -- length of the pendulums string to first joint
        M2 -- mass of pendulums end joint
        L2 -- length of the pendulums string to end joint
        """
        self.M1, self.L1, self.M2, self.L2 = M1, L1, M2, L2

    def __call__(self, t, y):
        """
        Returns the values of the derivatives of
        theta1, omega1, theta2 and omega2 as tuple.
        """
        M1, L1, M2, L2 = self.M1, self.L1, self.M2, self.L2
        theta1, omega1, theta2, omega2 = y[0], y[1], y[2], y[3]
        abs_theta = (theta2 - theta1)
        alpha1 = ((M2*L1*(omega1**2)*sin(abs_theta)*cos(abs_theta)
                 + M2*g*sin(theta2)*cos(abs_theta)
                 + M2*L2*(omega2**2)*sin(abs_theta)
                 - (M1 + M2)*g*sin(theta1))
                 / ((M1 + M2)*L1 - M2*L1*cos(abs_theta)**2))
        alpha2 = ((-M2*L2*omega2**2*sin(abs_theta)*cos(abs_theta)
                 + (M1 + M2)*g*sin(theta1)*cos(abs_theta)
                 - (M1 + M2)*L1*omega1**2*sin(abs_theta)
                 - (M1+M2)*g*sin(theta2))
                 / ((M1 + M2)*L2 - M2*L2*cos(abs_theta)**2))
        return(omega1, alpha1, omega2, alpha2)


    def solve(self, y0, T, dt, angles):
        """
        Solves differential equations and stores the arrays
        theta1, omega1, theta2 and omega2. Also stores the input value dt.

        y0     -- initial values of the differential equations
        T      -- end time
        dt     -- increment in time
        angles -- radians or degrees
        """
        if angles == "deg":
            y[0], y[1], y[2], y[3] = y[0]*pi/180, y[1]*pi/180, y[2]*pi/180, y[3]*pi/180
        diff = self.__call__
        time_points = list(np.linspace(0.0, T, T/dt))
        sol = solve_ivp(diff, (0.0,T), y0, t_eval=time_points, method="Radau")
        self._theta1 = sol.y[0]; self._omega1 = sol.y[1]
        self._theta2 = sol.y[2]; self._omega2 = sol.y[3]
        self._t = sol.t; self.dt = dt

    @property
    def theta1(self):
        """Returns theta1 as array"""
        try:
            return self._theta1
        except AttributeError:
            print('Method solve has to be called first.')
            raise        

    @property
    def theta2(self):
        """Returns theta2 as array"""
        try:
            return self._theta2
        except AttributeError:
            print('Method solve has to be called first.')
            raise  

    @property
    def t(self):
        """Returns t as array"""
        try:
            return self._t
        except AttributeError:
            print('Method solve has to be called first.')
            raise  

    @property
    def x1(self):
        """Converts theta1 to x-coordinates and returns array x1"""
        return self.L1*np.sin(self.theta1)

    @property
    def y1(self):
        """Converts theta1 to y-coordinates and returns array y1"""
        return -self.L1*np.cos(self.theta1)

    @property
    def x2(self):
        """Converts theta2 to x-coordinates and returns array x2"""
        return self.x1 + self.L2*np.sin(self.theta2)

    @property
    def y2(self):
        """Converts theta2 to y-coordinates and returns array y2"""
        return self.y1 - self.L2*np.cos(self.theta2)

    @property
    def potential(self):
        """
        Calculates the potential energy of the system and return it as an array
        """
        return (self.M1*g*(self.y1 + self.L1)
                + self.M2*g*(self.y2 + self.L1 + self.L2))

    @property
    def vx1(self):
        """Calculates and returns the velocity (vx1) as an array."""
        return np.gradient(self.x1, self.t)

    @property
    def vx2(self):
        """Calculates and returns the velocity (vx2) as an array."""
        return np.gradient(self.x2, self.t)

    @property
    def vy1(self):
        """Calculates and returns the velocity (vy1) as an array."""
        return np.gradient(self.y1, self.t)

    @property
    def vy2(self):
        """Calculates and returns the velocity (vy2) as an array."""
        return np.gradient(self.y2, self.t)

    @property
    def kinetic(self):
        """
        Calculate the kinetic energy and return it as an array.
        """
        return (0.5*self.M1*(self.vx1**2 + self.vy1**2)
                + 0.5*self.M2*(self.vx2**2 + self.vy2**2))

    def create_animation(self):
        """Plots the animation"""
        # Create empty figure
        fig = plt.figure()

        # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-10, 10, -10, 10))

        # Make an "empty" plot object to be updated throughout the animation
        self.pendulums, = plt.plot([], [], 'o-g', lw=2)

        # Call FuncAnimation
        self.animation = animation.FuncAnimation(fig,
                                                 self._next_frame,
                                                 frames=range(len(self.x1)),
                                                 repeat=None,
                                                 interval=1000*self.dt,
                                                 blit=True)

    def _next_frame(self, i):
        """Returns coordinates to be plotted."""
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums,

    def show_animation(self):
        """Shows the animation"""
        self.create_animation()
        plt.show()

    def save_animation(self,filename):
        """Saves the animation as mp4-file"""
        self.create_animation()
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=60)
        self.animation.save('{}.mp4'.format(filename), writer = writer)

if __name__ == '__main__':
    y = [pi, 0.0, pi/2, -2.0]
    dp = DoublePendulum(M1=4.0, L1=4.0, M2=1.1, L2=2.5)
    T = 10.0; dt = 1/60
    dp.solve(y, T, dt, angles="rad")

    # Plotting the energies with respect to time. 
    plt.plot(dp.t, dp.potential, dp.t, dp.kinetic, dp.t,
             dp.potential + dp.kinetic)
    plt.xlabel('time [s]')
    plt.ylabel('energy [J]')
    plt.title('Energies v. time')
    plt.legend(['Potential', 'Kinetic', 'Total'])
    plt.show()
    
    dp.show_animation()
    dp.save_animation('example_simulation')
