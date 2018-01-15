import numpy as np
from scipy.integrate import ode


class DCMotor(object):
    def __init__(self):
        self.J = 0.01    # moment of inertia of the rotor [kg m^2]
        self.b = 0.1     # motor viscous friction constant [N m s]
        self.Ke = 0.01   # electromotive force constant [V/rad/sec]
        self.Kt = 0.01   # motor torque constant [N m/A]
        self.R = 1       # electric resistance [Ohm]
        self.L = 0.5     # electric inductance [H]

    def motorTorque(Kt, I):
        '''
        Calculate the torque of a DC motor with constant magnetic field
        
        Args:
        Kt: Motor torque constant
        I: Current of the motor
        
        Returns the torque of the motor
        '''
        return Kt * I
        
    def backEMF(Ke, thp):
        '''
        Calculate the back emf of a DC motor
        
        Args:
        Ke: Back emf constant of the motor
        thp: Velocity of the motor
        
        Returns the back emf torque
        '''
        return Ke * thp

# def mechanicalEoM(Kt, b, J, I, th0, thp0, thpp0):
#     '''
#     Mechanical equations of motion of the DC motor

#     Args:
#     Kt: Torque constant of the motor
#     b: Damping of the motor
#     J: Inertia of the motor
#     I: Current going into the motor
#     th0, thp0, thpp0: Initial conditions for motor angle, velocity and acculeration
    
#     Returns the motor angle and angular velocity

#     th_pp = Kt * I - 
#     '''
    
if __name__ == '__main__':
    # Parameters of the system
    M = DCMotor()
