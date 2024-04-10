import numpy as np

class StateSpaceController:

    def __init__(self):
        #K_name = [k1, k2, k3, scaling]
        self.K_angle =  [0.2575, -0.0076, 0, 0.2575] #[1.0299, 0.0268, 0, 1.0299]#[0.0644, -0.0248, 0, 0.0644]#[0.5780, 0.0268, 0, 0.5780]
        self.K_speed = [0, -0.00764, 0, 0.0344] 
        self.K_angle_wI = [0.5804, 0.1042, 1.9310]# pole 20 [0.7524, 0.1472, 2.5747, 0] # pole 10 [0.4840, 0.0612, 1.2873, 0] #[1.1283, 0.0612, 4.6228, 0] #[4.706, 0.2848,34.6818, 0] #[1.954, 0.1128, 11.5606, 0]
        self.K_speed_wI = [0, 0.1720, 0.0526, 0]
        
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
        input_voltage = setpoint * self.K_speed[3] - (output_omega - setpoint) * self.K_angle[1]

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