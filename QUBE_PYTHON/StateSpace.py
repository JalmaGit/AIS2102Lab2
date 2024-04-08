

class StateSpaceController:

    def __init__(self):
        self.k1 = 0.5780
        self.k2 = 0.0268
        self.scaling = 0.5780

    def regulate(self, output_theta, output_omega, setpoint):
        setpoint = setpoint * self.scaling
        input_voltage = setpoint - (output_theta * self.k1 + output_omega * self.k2)

        if input_voltage < -18:
            input_voltage = -18
        elif input_voltage > 18:
            input_voltage = 18

        return input_voltage
    
    def regulateWithObserver():
        pass