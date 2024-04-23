A = -(K_t*K_b)/(J*R_a);
B = K_t/(R_a*J);
C = 1;
D = 0;

angle_sys = tf(K_t/(R_a*J),[1, (K_t*K_b)/(J*R_a), 0]);
tf(angle_sys)
a = 4/0.51;

actual_system = tf(a*(2834*pi/30)/12,[1,a,0])

f1 = figure(1);
hold on
step(angle_sys, 3)
title('Step Response Angle')
step(actual_system,3)
hold off