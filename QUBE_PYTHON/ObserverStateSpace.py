class Observer:

    def __init__(self):
        self.l1 = 150 #Speed
        self.l2 = 1197 #Angle

        k_t = 0.042
        k_b = k_t
        J_tot = 2.15 * 10**(-5)
        R_a = 8.4

        self.A_omega = -(k_b * k_t)/(J_tot*R_a)
        self.B_omega = k_t/(R_a*J_tot)

        self.C_omega = 1
        self.C_theta = 1

        self.previousIntegral = 0
        self.previousDoubleIntegral = 0
        self.afterAdder = 0

        self.errorInAngle = 0
        self.errorInSpeed = 0

        print (f"{self.A_omega=}, {self.B_omega=}")

    
    def observer(self, input_voltage, output_theta, dt):

        input_B = input_voltage * self.B_omega
        feedback_l2 = self.errorInAngle * self.l2
        feedback_A = self.afterAdder * self.A_omega

        theta_ddot = input_B + feedback_l2 + feedback_A

        theta_dot = self.previousIntegral + theta_ddot * dt 
        self.previousIntegral = theta_dot

        feedback_l1 = self.errorInAngle * self.l1
        self.afterAdder = feedback_l1 + theta_dot

        theta = self.previousDoubleIntegral + self.afterAdder * dt
        self.previousDoubleIntegral = theta

        self.errorInAngle = output_theta - theta

        estimatedSpeed = theta_dot

        return estimatedSpeed
    
"""
        self.errorInAngle = output_theta - doubleIntegrator
        
        x_dot = self.B_omega * input_voltage + self.l1 * self.errorInSpeed + self.A_omega * self.previousIntegralA

        integrator = self.previousIntegralA + x_dot * dt
        self.previousIntegralA = integrator

        self.errorInSpeed = output_omega - integrator

        doubleIntegrator = self.previousDoubleIntegral + (integrator + self.errorInAngle * self.l2) * dt
        self.previousDoubleIntegral = doubleIntegrator
"""