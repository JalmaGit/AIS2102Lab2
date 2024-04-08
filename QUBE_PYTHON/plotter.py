import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def find_markers(data):
    markers_on_finder = []
    x = 0
    r = 0
    for i in data["rpm"]:
        r += 1
        if i > 3560 and not(x == -1):
            x += 1

        if x == 20:
            markers_on_finder.append(r)
            x = -1

        if i <= 0 and (x == -1):
            x = 0
    return markers_on_finder

def check_in_range(i):
    if (i - 1000) < 0:
        return 0
    else:
        return (i - 400)

def find_specific_mark(data, i, mark):
    for y in range (i, check_in_range(i),-1):
        print(y)
        if data["rpm"][y] <= mark:
            return y

def find_other_markers(data, markers_on_100, percentage_to_find):
    marker = []

    for i in markers_on_100:
        f = data["rpm"][i]
        f = f * percentage_to_find
        marker.append(find_specific_mark(data, i, f))
    return marker
    
filename = 'Gen_Data/StepInput.csv'
dataframe = pd.read_csv(filename)

markers_on = find_markers(dataframe)
markers_on_98 = find_other_markers(dataframe,markers_on,0.98)
markers_on_0 = find_other_markers(dataframe,markers_on,0.0)

print(markers_on_0)

fig, ax = plt.subplots()
ax.plot(dataframe["time"], dataframe["rpm"], '-', label='System Response')
ax.plot(dataframe["time"], dataframe["rpm"], 'bo',markevery=markers_on, label=f'Max Speed = {dataframe["rpm"][markers_on[3]]}rpm, T_p = {round(dataframe["time"][markers_on[3]],2)}sec')
ax.plot(dataframe["time"], dataframe["rpm"], 'ro',markevery=markers_on_98, label=f'98% Speed = {dataframe["rpm"][markers_on_98[3]]}rpm, T_s = {round(dataframe["time"][markers_on_98[3]],2)}sec')
ax.plot(dataframe["time"], dataframe["rpm"], 'go',markevery=markers_on_0, label=f'0% Speed = {dataframe["rpm"][markers_on_0[3]]}rpm, T_0 {round(dataframe["time"][markers_on_0[3]],2)}sec')
ax.set_xlabel("time in seconds")
ax.set_ylabel("revoultions per minute")
ax.set_title("Sine wave input plot with a function v(t) = 8sin(PI/4 * t) + 8", loc='left')
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1fs'))
ax.grid(True)
fig.autofmt_xdate()
fig.legend(loc='center right')
fig.show()
plt.show()

#Parabolic input plot with a quadractic function v(t) = 2t^2