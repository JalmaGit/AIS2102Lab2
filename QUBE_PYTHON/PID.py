import sys


class PID:
    def __init__(self):
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.windup = 0
        self.lastIntegral = 0
        self.lastError = 0
        self.useWindup = False

    def regulate(self, currentAngle, setPoint, dt):
        # Implement controller using this function
        error = setPoint - currentAngle

        P = self.kp * error
        I = self.lastIntegral + self.ki * error * dt
        D = self.kd * ((error - self.lastError )/ dt)

        self.lastIntegral = I
        self.lastError = error

        return P + I + D

    def copy(self, pid):
        self.kp = pid.kp
        self.ki = pid.ki
        self.kd = pid.kd
        self.windup = pid.windup
        self.useWindup = pid.useWindup
