#!/Users/edelsonc/anaconda/bin/python
"""
This script contains the functions necessary to perform the physics needed for
the web application.

author: edelsonc
"""
import sys
import os
import math
import numpy
from scipy.constants import mu_0
from matplotlib import pyplot


class SquareCoil(object):
    """This class creates instances of square coils

    Methods
    -------
    self.__init__(self, zc, l, I, N) -> creates instance of class
    self.find_magnetic_field(self, z) -> find the magnetig field along z-axis
    """

    def __init__(self, zc, l, I, N):
        """initiates an instance of the SquareCoil

        Arguments
        ---------
        zc -- z-coordinate of the coil
        l -- length of coil side
        I -- coil current
        N -- number of wraps in the coil
        """
        self.position = zc
        self.side = l
        self.current = I
        self.wraps = N

    def find_magnetic_field(self, z):
        """Finds the magnetic field of the coil along the z-axis

        Arguments
        ---------
        z -- linspace
        """
        B = (4 * mu_0 * self.current * self.side**2 * self.wraps) / (math.pi *
            (self.side**2 + 4 * (z - self.position)**2) * numpy.sqrt(2 *
            self.side**2 + 4 * (z - self.position)**2))
        return B


def root_secant(f, a, b, tolerance=1.0e-6):
    """Uses the Secant method to find a value of x that is a solution near the
    initial guesses. Function is used as follows:
    
    def f(x):
        return x**2 - 1
        
    print(root_secant(f, 0, 1))  # returns 1
    print(root_secant(f, 0, -1)  # returns -1

    Argument
    --------
    f -- function to have roots found
    a, b -- initial guesses. Do not need to bracket the solution
    tolerance -- default of 1.0e-6 if no tolerance is specified
    """
    dx = abs(b-a)
    i = 0
    while dx > tolerance:
        # caclulating the slope in order to find the x_intercept (x_zero)
        m = (f(b) - f(a)) / (b - a)
        x_zero = b - f(b)/m

        # find if a of b is closer to intercept
        if abs(b - x_zero) < abs(a - x_zero):
            b, a = x_zero, b
        else:
            b = x_zero
        
        dx = abs(b-a)

    return x_zero


def calculate_current(B):
    """This function calculated the current required in the coils in order to
    get the specified magnetic field strength

    Arguments
    ---------
    B -- magnetic field strength
    """
    def fn(s):
        l = 1.8
        N = 10
        coils = [0, 0.7847046, 1.0152954, 1.8]
        z = [0.9 - pos for pos in coils]
        I=0
        return (((4*l**2*mu_0*s)/(math.pi*math.sqrt(2*l**2+4*z[0]**2)*(l**2+
            4*z[0]**2)) + (4*l**2*mu_0*s*0.423514)/(math.pi*math.sqrt(2*l**2+4*
            z[1]**2)*(l**2+4*z[1]**2)) + (4*l**2*mu_0*s*0.423514)/(math.pi*
            math.sqrt(2*l**2+4*z[2]**2)*(l**2+4*z[2]**2)) + (4*l**2*mu_0*s)/
            (math.pi*math.sqrt(2*l**2+4*z[3]**2)*(l**2+4*z[3]**2)))*N - B)

    I = root_secant(fn, 0, 8)
    return I, I*0.423514


def plot_central_field(I, static):
    """Plots the magnetic field along the central axis of the square four coil
    helmholtz array.

    Argument
    --------
    I -- current in Amps
    static -- location of the static file for flask
    """
    N = 100  # number of points in each dimension
    z_start, z_end = -1.8, 3.6  # dimensions of array in meters
    z = numpy.linspace(z_start, z_end, N)  # 1D z array

    coil_pos = numpy.array([0, 0.7847046, 1.0152954, 1.8])
    N_coils = 10
    
    # create four coils
    I_in = I*0.423514
    coil_1 = SquareCoil(coil_pos[0], 1.8, I, N_coils)
    coil_2 = SquareCoil(coil_pos[1], 1.8, I_in, N_coils)
    coil_3 = SquareCoil(coil_pos[2], 1.8, I_in, N_coils)
    coil_4 = SquareCoil(coil_pos[3], 1.8, I, N_coils)

    # calculate magnetic fields
    B1 = coil_1.find_magnetic_field(z)
    B2 = coil_2.find_magnetic_field(z)
    B3 = coil_3.find_magnetic_field(z)
    B4 = coil_4.find_magnetic_field(z)

    # super impose field
    B = B1 + B2 + B3 + B4
    B *= 10**4 # converts Telsa to Guass

    # plot magnetic field along z-axis
    size = 5
    pyplot.figure(figsize=(size, size))
    pyplot.xlabel("z-axis (m)")
    pyplot.ylabel("Magnetic Field Strength (Gauss)")
    pyplot.xlim(z_start, z_end)
    pyplot.ylim(0.0, 0.8)
    pyplot.plot(z, B)
    pyplot.axvline(x=coil_pos[0], color='k', linewidth=1, linestyle='--',
                       label='Coil Location')
    pyplot.axvline(x=coil_pos[1], color='k', linestyle='--')
    pyplot.axvline(x=coil_pos[2], color='k', linestyle='--')
    pyplot.axvline(x=coil_pos[3], color='k', linestyle='--')
    pyplot.legend(loc=0)
    
    # save the figure
    pyplot.savefig('{}/images/temp_coil.png'.format(static))

    return None
