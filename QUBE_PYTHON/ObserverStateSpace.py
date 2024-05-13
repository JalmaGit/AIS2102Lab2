import numpy as np

class Observer:

    def __init__(self, l1, l2):
        #self.l1 = 30  #Speed
        #self.l2 = 280 #Angle

        self.L = np.array([[l1],[l2]])

        k_t = 0.042
        k_b = k_t
        J_tot = 2.15 * 10**(-5)
        R_a = 8.4
        D = 2.025 * 10**(-4)

        self.A = np.array([[0,1],[0, -((k_b * k_t)/(J_tot*R_a)+ D/J_tot)]])
        self.B = np.array([[0],[k_t/(R_a*J_tot)]])
        self.prevX_hat = np.array([[0],[0]])
        
        print(self.A , self.B)

    def observerFromMatrix(self, input_voltage, output_theta, dt):
        x_hat = self.prevX_hat + dt*(self.A @ self.prevX_hat + self.B * input_voltage + self.L * (output_theta - self.prevX_hat[0][0]))
        self.prevX_hat = x_hat

        estimatedSpeed = x_hat[1][0]
        estimatedAngle = x_hat[0][0]

        return estimatedSpeed, estimatedAngle