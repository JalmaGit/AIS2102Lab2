K_t = 0.042;        % Torque Coefficient
K_b = 0.042;        % Back Emf Constant
R_a = 8.4;          % Resistance

J_r = 4.9e-6;       % Inertia of rotor
J_m = 0.6e-6;       % Inertia of attachment module
J_d = 1.6e-5;       % Inertia of disc attachment

J = J_r+J_m+J_d;    % Total inertia

A = [0 1 ; 0 -(D_m*R_a+K_t*K_b)/(J*R_a)]
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;

OS = 15;
Ts = 3;

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2);
wd = (4/Ts)*tan(acos(zeta));
poles = [-4/Ts+wd*1i, -4/Ts-wd*1i];
Second_Order_K = acker(A,B,poles)

new_poles = 10*poles;
L = place(A',C',new_poles)'

L(1)
L(2)


%% -- TEST --

A=[-8,1,0;
   -17,0,1;
   -10,0,0]

C=[1,0,0]

OS = 20.788;
Ts = 4;

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2);
wd = (4/Ts)*tan(acos(zeta));
poles = [-4/Ts+wd*1i, -4/Ts-wd*1i]

new_poles = 10*[poles 10*real(poles(1))];
L = place(A',C',new_poles)'

L(1)
L(2)
L(3)