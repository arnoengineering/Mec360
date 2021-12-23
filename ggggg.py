import numpy as np
import sympy as sy

import matplotlib.pyplot as plt
#
# import collections

def sym_n(sim, r=5):
    ls = []
    for i in range(2,r):
        ls.append(sy.symbols(sim+str(i)))
    return ls

t = sy.symbols('t')
t1 = 50*t+sy.pi/3
om=t1.diff(t)

theta = [0, t1]
# alpha = [sy.symbols(f'a_{ri}') for ri in range(8)]
F = []
M = sy.symbols('M')
# for ii in collections.combinations(list(range(1,5))):
#     st = ','.join(ii)
#     st_f =  f'F_({st},y)'
#     st_fx = f'F_({st},x)'
#     F.append(sy.symbols(st_fx))
#     F.append(sy.symbols(st_f))
# np.zeros((1, 8))

r_mat = np.array([0.5, 2.0, 9, 0])
b_mat=np.array([0.5, 2.0, 9, 0])
m_mat = np.array([0, 2.5, 10.0, 15])
phi_mat = np.array([0, 0, 5, 0])
ma_mat = np.array([m_mat[1], m_mat[1], 0, m_mat[3], m_mat[2], 80, m_mat[3], 0])

t2 =sy.asin((r_mat[1]*sy.sin(t1)-r_mat[0])/r_mat[2])
al=t2.diff(t)
theta.append(t2)
A33 = -(r_mat[1]*sy.sin(theta[1]))
A34=r_mat[1]*sy.cos(theta[1])
A63 = sy.sin(theta[2])-b_mat[2]*sy.sin(theta[2]+phi_mat[2])
A64 = sy.cos(theta[2])-b_mat[2]*sy.cos(theta[2]+phi_mat[2])
A65 = sy.sin(theta[2]+phi_mat[2])
A66 = -sy.cos(theta[2]+phi_mat[2])

co=sy.zeros(8,8)
co[5,2] = A63
co[5,3] = A64
co[5,4] = A65
co[5,5] = A66
co[2,3] = A34
co[2,2] = A33
co[2,7] = 1
def rep_np(m,li,ji=1):
    for i in li:
        m[i[0],i[1]] = ji
rep_np(co,[[0,0],[0,2],[1,1], [1,3],[3,4],[7,6],[7,5]])
rep_np(co,[[3,2],[4,3],[4,5],[6,4]],-1)

r1x = b_mat[1]*sy.cos(theta[1]+phi_mat[1])
r1y = b_mat[1]*sy.sin(theta[1]+phi_mat[1])
r1_x = r_mat[1]*sy.cos(theta[1])
r1_y = r_mat[1]*sy.sin(theta[1])

r2y = sy.sin(theta[2])-b_mat[2]*sy.sin(theta[2]+phi_mat[2])+r1_y
r2x = sy.cos(theta[2])-b_mat[2]*sy.cos(theta[2]+phi_mat[2])+r1_x
r2_x = sy.cos(theta[2])+r1_x
r2_y = sy.sin(theta[2])+r1_y

alpha = [sy.diff(x,t) for x in [r1x, r1y, r2x, r2y, r2_x]]
alpha.insert(2,0)
alpha.insert(5,al)
alpha.insert(7,0)
ma=sy.Matrix(np.multiply(ma_mat,np.array(alpha)).transpose())

si = co.LUsolve(ma)

ti = np.linspace(0,1,100)
F_sx = []
F_sy = []
for tii in ti:
    F_sx.append(float(sy.N(si[0].subs(t,tii))))
    f_sy = si[6]+si[1]
    F_sy.append(float(sy.N(f_sy.subs(t,tii))))
F_sx = np.array(F_sx)
F_sy = np.array(F_sy)
F_s = np.sqrt(F_sx**2+F_sy**2)
aii = np.arctan(np.divide(F_sx, F_sy))
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(aii, F_s)
#plt.plot(F_sx, F_sy)
plt.show()