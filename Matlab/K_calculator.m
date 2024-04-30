%% Important: remember to run first to set up coefficients

K_t = 0.042;        % Torque Coefficient
K_b = 0.042;        % Back Emf Constant
R_a = 8.4;          % Resistance

J_r = 4.9e-6;       % Inertia of rotor
J_m = 0.6e-6;       % Inertia of attachment module
J_d = 1.6e-5;       % Inertia of disc attachment

J = J_r+J_m+J_d;    % Total inertia

D_m2 = (8.333*R_a*J+K_t*K_b)/R_a;
D_m = 2.025e-4;

OS = 15;
Ts = 2;

%% First order System

A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;

pole = -4/Ts
First_Order_K = acker(A,B,pole)

A_cl = A-B*First_Order_K;
cl_sys = ss(A_cl,B,C,D);

Kr = 1/dcgain(cl_sys)

%% Second order system

A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)];
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2);
wd = (4/Ts)*tan(acos(zeta));
poles = [-4/Ts+wd*1i, -4/Ts-wd*1i];
Second_Order_K = acker(A,B,poles)
s=tf('s');
test = (s-poles(1))*(s-poles(2));
A_cl = A-B*Second_Order_K;

cl_sys = ss(A_cl, B,C,D);
error = 1+C*inv(A_cl)*B

Kr = 1/dcgain(cl_sys)
B_cl = Kr*B;
error = 1+C*inv(A_cl)*B_cl

f1 = figure(2);
step(cl_sys)
f2 = figure(2);
step(ss(A_cl,B_cl,C,D))
%% Second order with integrator

A = [0 1 ; 0 -(D_m*R_a+K_t*K_b)/(J*R_a)];
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;

Ai=[A zeros(2,1);-C 0]
Bt = [B; 0]
Br = [zeros(2,1);1]
Ci = [C 0];

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2)
wd = (4/Ts)*tan(acos(zeta));

%Set poles
poles = [-(4/Ts)*25, -4/Ts+wd*1i, -4/Ts-wd*1i];

K = acker(Ai,Bt,poles)
Ai_cl = Ai-Bt*K;

f3 = figure(3);
step(ss(Ai_cl, Br, Ci, 0))

%% First order with integrator

A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;

Ai=[A zeros(1);-C 0];
Bt = [B; 0];
Br = [zeros(1,1);1];
Ci = [C 0];

poles = [-(4/Ts)*10 -4/Ts]
First_Order_K = acker(Ai,Bt,poles)
Ai_cl = Ai-Bt*First_Order_K;

f4 = figure(4); 
step(ss(Ai_cl,Br,Ci,D));
