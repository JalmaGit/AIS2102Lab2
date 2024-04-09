% State space for angle
A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)];
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;

angle_state_sys = ss(A, B, C, D);

poles=[-8+8.392j, -8-8.392j];
K = acker(A,B,poles);


A_cl = A - B*K;
cl_sys = ss(A_cl,B,C,D);
f1 = figure(1)
step(cl_sys);

[b, a]=ss2tf(A_cl,B,C,D);

error = 1+C*inv(A_cl)*B

poles=[-20, -8+8.392j, -8-8.392j];

Ai=[A zeros(2,1);-C 0]
Bt = [B; 0];
Br = [zeros(2,1);1];
Ci = [C 0];

K = acker(Ai,Bt,poles)
Ai_cl = Ai-Bt*K

placed = eig(Ai_cl)

integrated = ss(Ai_cl,Br,Ci,D);
error2 = 1+[1 0 0]*inv(Ai_cl)*[0;0;1]

f8=figure(8)
step(integrated)