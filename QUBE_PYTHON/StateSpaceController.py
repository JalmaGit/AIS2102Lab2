import numpy as np

class StateSpaceController:

    def __init__(self):

        #Peters values = [1.9985, 0.2033, 6.1629]
        #KrohnOgMagnus values = [0.09, 0.007, 0.9471, 0]

        #K_name = [k1, k2, k3, scaling]
        self.K_angle = [0.5780, 0.0268, 0, 0.5780]
        self.K_speed = [0, -0.00764, 0, 0.0344]
        self.K_angle_wI = [0.4059, 0.033, 1.5993, 0] #[1.1283, 0.0612, 4.6228, 0] #[4.706, 0.2848,34.6818, 0] #[1.954, 0.1128, 11.5606, 0]
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
        x_N = self.prevAngleIntegral + (setpoint - output_theta) * dt
        self.prevAngleIntegral = x_N

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
        x_N = self.prevSpeedIntegral + (setpoint - output_omega) * dt
        self.prevSpeedIntegral = x_N

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