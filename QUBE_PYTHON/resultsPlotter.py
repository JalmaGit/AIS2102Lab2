import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

def anglePlot():

    fileName = "Gen_Data/ObserverNoIntegrator/AngleControl.csv"

    df = pd.read_csv(fileName)

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, ax = plt.subplots()
    ax.plot(df["time"].to_numpy(), df["motor_angle"].to_numpy(), '-', label='System Response')
    ax.plot(df["time"].to_numpy(), df["setAngle"].to_numpy(), '-', label='System Response')
    ax.plot(df["time"].to_numpy(), df["e_angle"].to_numpy(), '-', label='System Response')
    fig.show()
    plt.show()

def speedPlot(fileName, Title):
    
    fileName = "Gen_Data/WithoutIntegrator/SpeedControl.csv"

    df = pd.read_csv(fileName)
    df = df.iloc[100:]  

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, ax = plt.subplots()
    ax.plot(df["time"].to_numpy(), df["rpm"].to_numpy(), '-', label='Qube Speed')
    ax.plot(df["time"].to_numpy(), df["setSpeed"].to_numpy(), '-', label='Target Speed')
    ax.set_xlabel("Time in seconds (s)")
    ax.set_ylabel("Speed (RPM)")
    ax.set_title(Title)
    #ax.plot(df["time"].to_numpy(), df["e_angle"].to_numpy(), '-', label='System Response')
    fig.show()
    plt.legend()
    plt.show()

def speedPlotwithCurrent(fileName, Title):

    df = pd.read_csv(fileName)
    df = df.iloc[8000:]  

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.plot(df["time"].to_numpy(), df["rpm"].to_numpy(), '-', label='Qube Speed')
    ax1.plot(df["time"].to_numpy(), df["setSpeed"].to_numpy(), '-', label='Target Speed')
    ax1.set_xlabel("Time in seconds (s)")
    ax1.set_ylabel("Speed (RPM)")
    ax1.legend()
    ax2.plot(df["time"].to_numpy(), df["current"].to_numpy(), '-', label='Current')
    ax2.set_xlabel("Time in seconds (s)")
    ax2.set_ylabel("Current in milliAmps (mA) ")
    ax2.legend()
    fig.suptitle(Title, fontsize=16)
    fig.show()
    plt.show()



def ObsVsAct():
    fileName = "Gen_Data/ObservVSreal.csv"

    df = pd.read_csv(fileName)

    columnsNeeded = ["time", "motor_angle", "rpm","voltage", "current", "e_speed", "e_angle", "setSpeed","setAngle"]

    df = df[columnsNeeded]

    df = df.iloc[500:]

    fig, ax = plt.subplots()
    ax.plot(df["time"].to_numpy(), df["rpm"].to_numpy(), '-', label='System Response')
    ax.plot(df["time"].to_numpy(), df["e_speed"].to_numpy(), '-', label='System Response')
    fig.show()
    plt.show()


fileName = "Gen_Data/WithIntegrator/SpeedControlM.csv"
speedPlotwithCurrent(fileName)

fileName = "Gen_Data/WithoutIntegrator/SpeedControl.csv"
speedPlotwithCurrent(fileName)

fileName = "Gen_Data/ObserverNoIntegrator/SpeedControl.csv"
speedPlotwithCurrent(fileName)

fileName = "Gen_Data/ObserverWIntegrator/SpeedControl.csv"
speedPlotwithCurrent(fileName)