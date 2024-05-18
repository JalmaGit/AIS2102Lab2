import pandas as pd

filename = "Gen_Data/StepInput12volt.csv"

df = pd.read_csv(filename)

newDf = df.drop(columns=["motor_setpoint","pendulum_angle","pendulum_setpoint","rpm","current"])

print(newDf)

newFilename = "Gen_Data/PIDTuningDataReal.csv"

newDf.to_csv(newFilename, index=False)