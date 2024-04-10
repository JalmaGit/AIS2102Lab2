A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;

ang_vel_state_sys = ss(A,B,C,D);
tf(ang_vel_state_sys)
a = 4/0.51;

actual_system = tf(a*(2834*pi/30)/12,[1,a,0])

f1 = figure(1);
hold on
step(ang_vel_state_sys, 3)
title('Step Response Angle')
step(actual_system,3)
hold off