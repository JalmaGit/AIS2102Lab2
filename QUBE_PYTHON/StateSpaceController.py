import numpy as np

class StateSpaceController:

    def __init__(self):

        #K_name = [k1, k2, k3, scaling]
        self.K_angle = [0.5780, 0.0268, 0, 0.5780]
        self.K_speed = [0, -0.00764, 0, 0.0344]
        self.K_angle_wI = [0, 0, 0, 0]
        self.K_speed_wI = [0, 0, 0, 0]
        
        self.prevAngleIntegral = 0
        self.prevSpeedIntegral = 0
 
    def regulateAngleWithoutI(self, output_theta, output_omega, setpoint):
        setpoint = setpoint * self.K_angle[3]
        input_voltage = (setpoint - (output_theta * self.K_angle[0] + output_omega * self.K_angle[1]))

        #Voltage Limiters
        if input_voltage < -24:
            input_voltage = -24
        elif input_voltage > 24:
            input_voltage = 24

        return input_voltage
    
    def regulateSpeedWithoutI(self, output_omega, setpoint):
        setpoint = setpoint * self.K_speed[3]
        input_voltage = (setpoint - output_omega * self.K_angle[1])

        #Voltage Limiters
        if input_voltage < -24:
            input_voltage = -24
        elif input_voltage > 24:
            input_voltage = 24

        return input_voltage
    
    def regulateAngleWithI(self, output_theta, output_omega, setpoint, dt):
        #Integrator
        x_N = self.prevIntegral + (setpoint - output_theta) * dt
        self.prevIntegral = x_N

        #Kp and Kd calc
        kx = output_theta * self.K_angle_wI[0] + output_omega * self.K_angle_wI[1]

        #u(t)
        input_voltage = - kx + self.K_angle_wI[2]*x_N
        
        #Voltage Limiters
        if input_voltage < -24:
            input_voltage = -24
        elif input_voltage > 24:
            input_voltage = 24

        return input_voltage
    
    def regulateSpeedWithI(self, output_omega, setpoint, dt):
        #Integrator
        x_N = self.prevIntegral + (setpoint - output_omega) * dt
        self.prevIntegral = x_N

        #Kp and Kd calc
        kx = output_omega * self.K_angle_wI[1]

        #u(t)
        input_voltage = - kx + self.K_angle_wI[2]*x_N
        
        #Voltage Limiters
        if input_voltage < -24:
            input_voltage = -24
        elif input_voltage > 24:
            input_voltage = 24

        return input_voltage