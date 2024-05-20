class StateSpaceController:

    def __init__(self):
        #K_name = [k1, k2, k3, scaling]
        self.K_angle =  [0.1969, -0.0076, 0, 0.1969]
        self.K_speed = [0, -0.0248, 0, 0.0172] 
        self.K_angle_wI = [1.5729, 0.1644, 7.8749] # New with Damping [1.5729, 0.1659, 7.8749]
        self.K_speed_wI = [0,0.0612,0.3440]# Mid: [0, 0.1472, 0.6880, 0] # Low: [0,0.0612,0.3440] # High: [0,0.2332,1.032]
        
        self.prevAngleIntegral = 0
        self.prevSpeedIntegral = 0
        self.windupGuard = 0
 
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
        input_voltage = setpoint * self.K_speed[3] - output_omega * self.K_speed[1]
        #input_voltage = setpoint * self.K_speed[3] - (output_omega - setpoint) * self.K_angle[1]
    
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
        
        kx = - output_theta * self.K_angle_wI[0] - output_omega * self.K_angle_wI[1]

        #u(t)
        input_voltage = kx + self.K_angle_wI[2]*x_N
        
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

        kx = output_omega * self.K_angle_wI[1]

        #u(t)
        input_voltage = - kx + self.K_angle_wI[2]*x_N
        
        #Voltage Limiters
        if input_voltage < -24:
            input_voltage = -24
        elif input_voltage > 24:
            input_voltage = 24

        return input_voltage