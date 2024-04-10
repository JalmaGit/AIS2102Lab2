K_t = 0.042;        % Torque Coefficient
K_b = 0.042;        % Back Emf Constant
R_a = 8.4;          % Resistance

J_r = 4.9e-6;       % Inertia of rotor
J_m = 0.6e-6;       % Inertia of attachment module
J_d = 1.6e-5;       % Inertia of disc attachment

J = J_r+J_m+J_d;    % Total inertia

A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;

pole = -8;

K = acker(A,B,pole)

A_cl = A - B*K;
cl_sys = ss(A_cl,B,C,D);

% Forward gain to reduce state space error
Kr = 1/dcgain(cl_sys)
B_cl = Kr*B;

cl_c_sys = ss(A_cl,B_cl,C,D);
step(cl_c_sys)
