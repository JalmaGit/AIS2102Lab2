# ------------------------------------- AVAILABLE FUNCTIONS --------------------------------#
# qube.setRGB(r, g, b) - Sets the LED color of the QUBE. Color values range from [0, 999].
# qube.setMotorSpeed(speed) - Sets the motor speed. Speed ranges from [-999, 999].
# qube.setMotorVoltage(volts) - Applies the given voltage to the motor. Volts range from (-24, 24). Nope, volts range from (-18,18)
# qube.resetMotorEncoder() - Resets the motor encoder in the current position.
# qube.resetPendulumEncoder() - Resets the pendulum encoder in the current position.

# qube.getMotorPosition() - Returns the cumulative angular positon of the motor.
# qube.getPendulumPosition() - Returns the cumulative angular position of the pendulum.
# qube.getMotorRPM() - Returns the newest rpm reading of the motor.
# qube.getMotorCurrent() - Returns the newest reading of the motor's current.
# ------------------------------------- AVAILABLE FUNCTIONS --------------------------------#

from QUBE import *
from logger import *
from com import *
from liveplot import *
from time import time
import threading
import math
import StateSpaceController as SSC
import ObserverStateSpace as OSS
import SystemValidationTest as SVT

# Replace with the Arduino port. Can be found in the Arduino IDE (Tools -> Port:)
port = "/dev/ttyACM0"
baudrate = 115200
qube = QUBE(port, baudrate)

# Resets the encoders in their current position.
qube.resetMotorEncoder()
qube.resetPendulumEncoder()

# Enables logging - comment out to remove
enableLogging()

t_last = time()

def control(data, lock):

    global m_target, p_target, e_speed, e_angle , pid
    m_target = 0
    p_target = 0
    e_speed = 0
    e_angle = 0
    pid = PID()
    volts = 0
    state_space = SSC.StateSpaceController()
    observer = OSS.Observer(60.8140 , 3411.7)
    systemTest = SVT.SystemValidationTest(12, 10)

    print(systemTest.volt)

    estimatedSpeed = 0
    estimatedAngle = 0

    setAngle = 90 #Degrees
    setRPM = 2000 #RPM

    print(f"{setRPM=}")

    #Convert to rad
    setAngle = setAngle /180 * math.pi
    setRPM = setRPM * math.pi/30

    print(f"{setRPM=}")
    
    while True:
        # Updates the qube - Sends and receives data
        qube.update()

        # Gets the logdata and writes it to the log file
        logdata = qube.getLogData(m_target, p_target, e_speed / math.pi * 30, e_angle * 180 / math.pi, setRPM / math.pi * 30, setAngle * 180 / math.pi)
        save_data(logdata)

        # Multithreading stuff that must happen. Dont mind it.
        with lock:
            doMTStuff(data)

        # Get deltatime
        dt = getDT()
        ### Your code goes here
        
        ## System Tests

        #volts = systemTest.stepInput()

        qube.setMotorVoltage(volts)

        angle = qube.getMotorAngle() /180 * math.pi
        speed = qube.getMotorRPM() * math.pi/30

        setRPM = systemTest.alternatingSpeed()

        ## Change Between regulators by commenting and uncommenting

        #volts = pid.regulate(angle, setAngle, dt)

        #volts = state_space.regulateAngleWithoutI(angle, speed, setAngle)
        #volts = state_space.regulateSpeedWithoutI(speed, setRPM)
        volts = state_space.regulateAngleWithI(angle, speed, setAngle, dt)
        #volts = state_space.regulateSpeedWithI(speed, setRPM, dt)

        #volts = state_space.regulateAngleWithoutI(estimatedAngle, estimatedSpeed, setAngle)
        #volts = state_space.regulateSpeedWithoutI(estimatedSpeed, setRPM)
        #volts = state_space.regulateAngleWithI(estimatedAngle, estimatedSpeed, setAngle, dt)
        #volts = state_space.regulateSpeedWithI(estimatedSpeed, setRPM, dt)

        #m_target = setRPM / math.pi * 30
        m_target = setAngle * 180 / math.pi
        
        estimatedSpeed, estimatedAngle = observer.observerFromMatrix(volts, angle, dt)

        e_speed = estimatedSpeed
        e_angle = estimatedAngle

        ####Debugging
        #print(f"RPM={volts}")
        #print(f"Debugging: volts = {round(volts,2)}")
        #print(f'Debugging: volts = {round(volts,2)}, estAngle = {round(estimatedAngle,2)}, error = {round(error,2)}')
        #print(f'Debugging: volts = {round(volts,2)}, estSpeed = {round(estimatedSpeed * 30/math.pi,2)}, estAngle = {estimatedAngle}, deltaTime = {round(dt,10)}') # \n {pid.kp=}, {pid.ki=}, {pid.kd=} ')


def getDT():
    global t_last
    t_now = time()
    dt = t_now - t_last
    t_last += dt
    return dt


def doMTStuff(data):
    packet = data[7]
    pid.copy(packet.pid)
    if packet.resetEncoders:
        qube.resetMotorEncoder()
        qube.resetPendulumEncoder()
        packet.resetEncoders = False

    new_data = qube.getPlotData(m_target, p_target)
    for i, item in enumerate(new_data):
        data[i].append(item)


if __name__ == "__main__":
    _data = [[], [], [], [], [], [], [], Packet()]
    lock = threading.Lock()
    thread1 = threading.Thread(target=startPlot, args=(_data, lock))
    thread2 = threading.Thread(target=control, args=(_data, lock))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
