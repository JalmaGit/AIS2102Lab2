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
import StateSpace

# Replace with the Arduino port. Can be found in the Arduino IDE (Tools -> Port:)
port = "COM5"
baudrate = 115200
qube = QUBE(port, baudrate)

# Resets the encoders in their current position.
qube.resetMotorEncoder()
qube.resetPendulumEncoder()

# Enables logging - comment out to remove
enableLogging()

t_last = time()

def control(data, lock):

    global m_target, p_target, pid
    m_target = 0
    p_target = 0
    pid = PID()
    lastTime = time()
    delay = 4.0
    volts = 18
    state_space = StateSpace.StateSpaceController()
    

    while True:
        # Updates the qube - Sends and receives data
        qube.update()

        # Gets the logdata and writes it to the log file
        logdata = qube.getLogData(m_target, p_target)
        save_data(logdata)

        # Multithreading stuff that must happen. Dont mind it.
        with lock:
            doMTStuff(data)

        # Get deltatime
        dt = getDT()
        ### Your code goes here

        angle = qube.getMotorAngle()
        speed = qube.getMotorRPM() * math.pi/30
        #volts = pid.regulate(angle, 90, dt)
        volts = state_space.regulate(angle, speed, 90)

        qube.setMotorVoltage(volts)

        ####Debugging
        print(f'Debugging: volts = {round(volts,2)} and Time = {round(time() - lastTime,2)} and Angle = {angle}') # \n {pid.kp=}, {pid.ki=}, {pid.kd=} ')


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
