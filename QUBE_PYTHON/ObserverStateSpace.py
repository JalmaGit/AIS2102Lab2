class Observer:

    def __init__(self):
        self.l1 = 150 #Speed
        self.l2 = 1197 #Angle

        k_t = 0.042
        k_b = k_t
        J_tot = 2.15 * 10**(-5)
        R_a = 8.4

        self.A_omega = (k_b * k_t)/(J_tot*R_a)
        self.B_omega = k_t/(R_a*J_tot)

        self.C_omega = 1
        self.C_theta = 1

        self.previousIntegralA = 0
        self.previousDoubleIntegral = 0

        self.errorInAngle = 0
        self.errorInSpeed = 0

        print (f"{self.A_omega=}, {self.B_omega=}")

    
    def observer(self, input_voltage, output_theta, output_omega, dt):

        x_dot = self.B_omega * input_voltage + self.l1 * self.errorInSpeed + self.A_omega * self.previousIntegralA

        integrator = self.previousIntegralA + x_dot * dt
        self.previousIntegralA = integrator

        self.errorInSpeed = output_omega - integrator

        doubleIntegrator = self.previousDoubleIntegral + (integrator + self.errorInAngle) * dt
        self.previousDoubleIntegral = doubleIntegrator

        self.errorInAngle = output_theta - doubleIntegrator

        EstimatedSpeed, EstimatedAngle = integrator, doubleIntegrator

        return EstimatedSpeed, EstimatedAngle