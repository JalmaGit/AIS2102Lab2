class Observer:

    def __init__(self):
        self.l1 = 0 #Speed
        self.l2 = 0 #Angle

        k_t = 0.042
        k_b = k_t
        J_tot = 2.15 * 10**(-5)
        R_a = 8.4

        #self.A_theta = np.array([[0, 1],[0,-((k_b * k_t)/(J_tot*R_a))]])
        #self.B_theta = np.array([[0, 1],[0,k_t/(R_a*J_tot)]])
        self.A_omega = (k_b * k_t)/(J_tot*R_a)
        self.B_omega = k_t/(R_a*J_tot)

        self.previousIntegralA = 0

        print (f"{self.A_omega=}, {self.B_omega=}")

    
    def observer(self, input_voltage, output_theta, output_omega, dt):

        self.B_omega * input_voltage + self.l1 + self.A_omega * self.previousIntegralA



        angle, speed = 0
        return angle, speed