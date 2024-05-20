import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

def anglePlotwithCurrent(fileName, Title, Start = 100, Stop=10000):

    df = pd.read_csv(fileName)
    df = df.iloc[Start:Stop]  

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(df["time"].to_numpy(), df["motor_angle"].to_numpy(), '-', label='Qube Angle')
    ax1.plot(df["time"].to_numpy(), df["setAngle"].to_numpy(), '-', label='Target Angle')
    ax1.set_xlabel("Time in seconds (s)")
    ax1.set_ylabel("Angle in degrees")
    ax1.set_title("Motor Angle")
    ax1.legend()
    ax2.plot(df["time"].to_numpy(), df["current"].to_numpy(), '-', label='Current')
    ax2.set_xlabel("Time in seconds (s)")
    ax2.set_ylabel("Current in milliAmps (mA) ")
    ax2.set_title("Current Drawn by the Motor")
    ax2.legend()
    fig.suptitle(Title, fontsize=16)
    fig.show()
    plt.show()


def speedPlotwithCurrent(fileName, Title, Start = 100, Stop=10000):

    df = pd.read_csv(fileName)
    df = df.iloc[Start:Stop]  

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(df["time"].to_numpy(), df["rpm"].to_numpy(), '-', label='Qube Speed')
    ax1.plot(df["time"].to_numpy(), df["setSpeed"].to_numpy(), '-', label='Target Speed')
    ax1.set_xlabel("Time in seconds (s)")
    ax1.set_ylabel("Speed (RPM)")
    ax1.set_title("Motor Speed")
    ax1.legend()
    ax2.plot(df["time"].to_numpy(), df["current"].to_numpy(), '-', label='Current')
    ax2.set_xlabel("Time in seconds (s)")
    ax2.set_ylabel("Current in milliAmps (mA) ")
    ax2.set_title("Current Drawn by the Motor")
    ax2.legend()
    fig.suptitle(Title, fontsize=16)
    fig.show()
    plt.show()

def speedPlotwithCurrentObs(fileName, Title, Start = 200, Stop=100000):

    df = pd.read_csv(fileName)
    df = df.iloc[Start:Stop]  

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(df["time"].to_numpy(), df["rpm"].to_numpy(), '-', label='Qube Speed')
    ax1.plot(df["time"].to_numpy(), df["e_speed"].to_numpy(), '-', label='Observer Speed')
    ax1.plot(df["time"].to_numpy(), df["setSpeed"].to_numpy(), '-', label='Target Speed')
    ax1.set_xlabel("Time in seconds (s)")
    ax1.set_ylabel("Speed (RPM)")
    ax1.set_title("Motor Speed")
    ax1.legend()
    ax2.plot(df["time"].to_numpy(), df["current"].to_numpy(), '-', label='Current')
    ax2.set_xlabel("Time in seconds (s)")
    ax2.set_ylabel("Current in milliAmps (mA) ")
    ax2.set_title("Current Drawn by the Motor")
    ax2.legend()
    fig.suptitle(Title, fontsize=16)
    fig.show()
    plt.show()

def anglePlotwithCurrentObs(fileName, Title, Start = 200, Stop=100000):

    df = pd.read_csv(fileName)
    df = df.iloc[Start:Stop]  

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(df["time"].to_numpy(), df["motor_angle"].to_numpy(), '-', label='Qube Angle')
    ax1.plot(df["time"].to_numpy(), df["e_angle"].to_numpy(), '-', label='Observer Angle')
    ax1.plot(df["time"].to_numpy(), df["setAngle"].to_numpy(), '-', label='Target Angle')
    ax1.set_xlabel("Time in seconds (s)")
    ax1.set_ylabel("Angle (Degree)")
    ax1.set_title("Motor Angle")
    ax1.legend()
    ax2.plot(df["time"].to_numpy(), df["current"].to_numpy(), '-', label='Current')
    ax2.set_xlabel("Time in seconds (s)")
    ax2.set_ylabel("Current in milliAmps (mA) ")
    ax2.set_title("Current Drawn by the Motor")
    ax2.legend()
    fig.suptitle(Title, fontsize=16)
    fig.show()
    plt.show()



#fileName = "Gen_Data/WithIntegrator/SpeedControlL.csv"
#title = "Speed Control with Integrator"
#speedPlotwithCurrent(fileName, title, 4000, 20000)

#fileName = "Gen_Data/WithoutIntegrator/SpeedControl.csv"
#title = "Speed Control without Integrator"
#speedPlotwithCurrent(fileName, title, 4000, 10000)

fileName = "Gen_Data/ObserverNoIntegrator/SpeedControl.csv"
title = "Speed Control with Observer and without Integrator"
speedPlotwithCurrentObs(fileName, title)

fileName = "Gen_Data/ObserverWIntegrator/SpeedControl.csv"
title = "Speed Control with Observer and with Integrator"
speedPlotwithCurrentObs(fileName, title)

#fileName = "Gen_Data/WithIntegrator/AngleControl.csv"
#title = "Angle Control with Integrator"
#anglePlotwithCurrent(fileName, title, 1000, 10000)

#fileName = "Gen_Data/WithoutIntegrator/AngleControl.csv"
#title = "Angle Control without Integrator"
#anglePlotwithCurrent(fileName, title, 1000, 10000)

fileName = "Gen_Data/ObserverNoIntegrator/AngleControl.csv"
title = "Angle Control with Observer and without Integrator"
anglePlotwithCurrentObs(fileName, title)

fileName = "Gen_Data/ObserverWIntegrator/AngleControl.csv"
title = "Angle Control with Observer and with Integrator"
anglePlotwithCurrentObs(fileName, title)

