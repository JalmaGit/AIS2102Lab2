OS = 5;
Ts = .5;


A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;

ang_vel_state_sys = ss(A, B, C, D);
pole = -4/Ts
First_Order_K = acker(A,B,pole)

A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)];
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;
angle_state_sys = ss(A, B, C, D);

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2);
wd = 8*tan(acos(zeta));
poles = [-4/Ts+wd*1i, -4/Ts-wd*1i];
Second_Order_K = acker(A,B,poles)

