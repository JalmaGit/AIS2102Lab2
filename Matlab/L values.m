K_t = 0.042;        % Torque Coefficient
K_b = 0.042;        % Back Emf Constant
R_a = 8.4;          % Resistance

J_r = 4.9e-6;       % Inertia of rotor
J_m = 0.6e-6;       % Inertia of attachment module
J_d = 1.6e-5;       % Inertia of disc attachment

J = J_r+J_m+J_d;    % Total inertia

A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)]
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;

OS = 25;
Ts = 1;

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2);
wd = 8*tan(acos(zeta));
poles = [-4/Ts+wd*1i, -4/Ts-wd*1i];
Second_Order_K = acker(A,B,poles)

new_poles = [-(4/Ts)*10+wd*1i, -(4/Ts)*10-wd*1i];
L = place(A',C',new_poles)'
error_thing = A-L*C

error = ss(error_thing, B,C,D)
step(error)
L(1)
L(2)