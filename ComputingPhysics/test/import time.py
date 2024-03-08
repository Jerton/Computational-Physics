import numpy as np
import matplotlib.pyplot as plt

nstep = 50
xfinal = 1.0
xini = 0.0

#降阶法
y1 = np.zeros(50)
dy1 = np.zeros(50)
y1[0] = 1.0
dy1[0] = 0.0
xstep = (xfinal - xini) / nstep

file_name_out = 'plot1.1.dat'

with open(file_name_out, 'w') as file_out:
    for i in range(1, nstep):
        dy1[i] = dy1[i - 1] + xstep * (-y1[i - 1])
        y1[i] = y1[i - 1] + xstep * dy1[i - 1]

        output_line = f"{(i - 1) * xstep:.7e} {y1[i]:.7e} {dy1[i]:.7e}{np.cos((i - 1) * xstep):.7e} \n"
        file_out.write(output_line)

#二阶差分法
y2 = np.zeros(50)
dy2 = np.zeros(50)
xstep = (xfinal - xini) / nstep
y2[0] = 1.0
y2[1] = y2[0] + 0.0 * xstep
dy2[0] = 0

file_name_out = 'plot1.2.dat'

with open(file_name_out, 'w') as file_out:
    for i in range(1,nstep-1):
        y2[i + 1] = ( 2.0 - xstep**2 ) * y2[i] -  y2[i-1]

        dy2[i + 1] = (y2[i+1] - y2[i-1])/2/xstep

        output_line = f"{(i - 1) * xstep:.7e} {y2[i]:.7e} {dy2[i]:.7e}{np.cos((i - 1) * xstep):.7e} \n"
        file_out.write(output_line)

#RK4方法
def fa(m, n1, n0):
    return n1

def fb(m, n1, n0):
    return -n0

out = "plot1.3.dat"
data = []
u = []
du = []

y11 = 1.0
y21 = 0.0
xstep = (xfinal - xini) / nstep

r = xini
a = y11
b = y21

for i in range(nstep + 1):
    data.append([r, a, b])
    u.append(a)
    du.append(b)
    k1 = fa(r, b, a)
    l1 = fb(r, b, a)
    k2 = fa(r + xstep / 2., b + xstep * l1 / 2., a + xstep * k1 / 2.)
    l2 = fb(r + xstep / 2., b + xstep * l1 / 2., a + xstep * k1 / 2.)
    k3 = fa(r + xstep / 2., b + xstep * l2 / 2., a + xstep * k2 / 2.)
    l3 = fb(r + xstep / 2., b + xstep * l2 / 2., a + xstep * k2 / 2.)
    k4 = fa(r + xstep, b + xstep * l3, a + xstep * k3)
    l4 = fb(r + xstep, b + xstep * l3, a + xstep * k3)

    k = xstep * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    l = xstep * (l1 + 2 * l2 + 2 * l3 + l4) / 6.0

    r = r + xstep
    a = a + k
    b = b + l

data = np.array(data)
    
np.savetxt(out, data, fmt='%15.7f')
    
plt.plot(y1, dy1, label="Reduction of order")
plt.plot(y2, dy2, label="Second order difference method")
plt.plot(u, du, label="RK4")
xr = []
yr = []#真实值
for i in range(50):
    xr.append(np.cos(i/50))
    yr.append(-np.sin(i/50))

plt.plot(xr, yr, label="Real")
plt.legend()
plt.xlabel('$u$')
plt.ylabel('$u^\prime$')
plt.title('Plot of $u^\prime$ vs $u$')
plt.show()
