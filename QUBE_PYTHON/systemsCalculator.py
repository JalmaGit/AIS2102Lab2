import math

def calibrate (raw_input):
    calibrated = [0]
    calibrated.append(raw_input[1] - raw_input[0])
    calibrated.append(raw_input[2] - raw_input[0])
    return calibrated

def calc_zeta (calibrated_input):
    return math.sqrt(1/(1+(math.pi**2 * calibrated_input[1]**2 * calibrated_input[2]**2)/16))

def calc_wn (calibrated_input,zeta):
    return 4/(zeta*calibrated_input[2])

def calc_characteristic_eq(zeta, wn):
    return f" {zeta=} \n {wn=} \n \n {round(wn**2,3)}k \n --------------------------- \n s^2 + {round(zeta*2*wn,3)}s + {round(wn**2,3)} \n"

def full_calc(raw_input):
    raw_input = calibrate(raw_input)
    zeta = calc_zeta(raw_input)
    wn = calc_wn(raw_input,zeta)

    print(f" {raw_input}")
    print(calc_characteristic_eq(zeta,wn))

# Variable = [T_0, T_p, T_s]
step_input = [28.92,29.72,29.4]
"""
ramp_input6 = [24.49,27.38,27.06]
ramp_input5 = [24.47,27.8,27.53]
parabolic2 = [24.78,27.59,27.33]
parabolic1_47 = [24.82,27.99,27.79]
sin_wave = [22.72,25.72,25.47]
"""

full_calc(step_input)

"""
full_calc(ramp_input6)
full_calc(ramp_input5)
full_calc(parabolic2)
full_calc(parabolic1_47)
full_calc(sin_wave)
"""