
import sympy as sy

f_1 =[]
f_2 = []
t,r,m,l,w = sy.symbols('t r m l w')
base_v = (0.5,1,1,1)
A = w**2*r*2*m
B = w**2*r**2 * 1.5*m/l
C = w**2*r/2*m
for i in range(3):
    th = w*t + 2*sy.pi/3 * i
    f1 = A*sy.cos(th)+B*sy.cos(2*th)
    f2 = A * sy.sin(th)
    f_1.append(f1)
    f_2.append(f2)
    print(i+1)
    print(f1)
    print(f2)

F1 = sum(f_1)
F2 = sum(f_2)
print(F1)
print(F2)
for i,j in zip((r,l,w,m), base_v):
    F1 = F1.subs(i,j)
    F2 = F2.subs(i,j)
print('F1')
print(F1)
print('F2')
print(F2)
sy.plot_parametric((-F2, F1), (t,0,1))