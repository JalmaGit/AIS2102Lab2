A = [0 1 ; 0 -(K_t*K_b)/(J*R_a)]
B = [0 ; K_t/(R_a*J)];
C = [1 0];
D = 0;

zeta = -log(OS/100)/sqrt(pi^2+log(OS/100)^2);
wd = 8*tan(acos(zeta));
poles = [-4/Ts+wd*1i, -4/Ts-wd*1i];
Second_Order_K = acker(A,B,poles)

L = place(A',C',poles*10)'
error_thing = A-L*C

error = ss(error_thing, B,C,D)
step(error)

L(1)
L(2)