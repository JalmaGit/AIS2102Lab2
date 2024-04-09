K_t = 0.042;        % Torque Coefficient
K_b = 0.042;        % Back Emf Constant
R_a = 8.4;          % Resistance

J_r = 4.9e-6;       % Inertia of rotor
J_m = 0.6e-6;       % Inertia of attachment module
J_d = 1.6e-5;       % Inertia of disc attachment

J = J_r+J_m+J_d;    % Total inertia

% Transfer function for angle
angle_sys = tf(K_t/(R_a*J),[1, (K_t*K_b)/(J*R_a), 0]);

% Transfer function for angular velocity
ang_vel_sys = tf(K_t/(R_a*J), [1, (K_t*K_b)/(J*R_a)]);

% State space for angle
A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)];
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;
angle_state_sys = ss(A, B, C, D);

% State space for angular velocity
A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;
ang_vel_state_sys = ss(A, B, C, D);

% STEP PLOTS
Config = RespConfig('Amplitude',18);

actual_system = tf(75.829*370,[1,16.667,75.829])

f1 = figure(1);
subplot(2,1,1)
step(angle_state_sys, 3, Config)
title('Step Response Angle')
subplot(2,1,2)
hold on
step(ang_vel_state_sys,3, Config)
title('Step Response Angular Velocity')
step(actual_system, 3, Config)
hold off

% RAMP PLOTS
t=0:0.01:3;
u = t*18/3;

f2 = figure(2);
subplot(2,1,1)
lsim(angle_state_sys,u,t)
title('Ramp Response Angle')
subplot(2,1,2)
lsim(ang_vel_state_sys,u,t)
title('Ramp Response Angular Velocity')

% PARABOLIC PLOTS
t=0:0.01:3;
u = t.^2*2;

f3 = figure(3);
subplot(2,1,1)
lsim(angle_state_sys,u,t)
title('Parabolic Response Angle')
subplot(2,1,2)
lsim(ang_vel_state_sys,u,t)
title('Parabolic Response Angular Velocity')

% Position Windows
f1.Position = [50,100,400,600];
f2.Position = [500,100,400,600];
f3.Position = [950,100,400,600];


% CONTROLLERS!!!!!!!!!

% Pole Placement Controller
Config = RespConfig('Amplitude',18);

A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)]
B = [0 ; K_t/(R_a*J)]
C = [1 0];
D = 0;

poles=[-8+8.392j, -8-8.392j];
K = acker(A,B,poles)

A_cl = A - B*K;
cl_sys = ss(A_cl,B,C,D);

% Forward gain to reduce state space error
Kr = 1/dcgain(cl_sys)
B_cl = Kr*B;

cl_c_sys = ss(A_cl,B_cl,C,D);

f4 = figure(4);
step(cl_c_sys,3)
title('Step Response Closed Loop')

% PID
Kp = 1.296; % 0.04
Ki = 2.736; % 0.014
Kd = 0.08723; % 0.002

pid_controller = pid(Kp,Ki,Kd);
Pid_controlled = feedback(angle_state_sys*pid_controller,1);
f9 = figure(9);
step(Pid_controlled)

% OBSERVER!!!!!!!!!
t = 0:0.01:2;
x0 = [0.1 0];

L = place(A',C',poles*10)'

At = [A-B*K             B*K
      zeros(size(A))    A-L*C];
Bt = [B*Kr
      zeros(size(B))];
Ct = [C zeros(size(C))];

test = ss(At, Bt, Ct, 0);

f5 = figure(5);
lsim(test,zeros(size(t)),t,[x0 x0]);
title('(with observer)')