import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 参数
L = 1.0
nx = 50
ny = 100
nt = 100
c = 1
dx = L / nx
dy = L / ny
dt = 0.005
lam = c * dt / dx

# 初始化
u0 = np.zeros((nx, ny))
for i in range(nx):
    for j in range(ny):
        u0[i][j] = np.sin(np.pi * i * dx) * np.sin(2 * np.pi * j * dy)

# 边界条件
u0[0, :] = 0
u0[-1, :] = 0
u0[:, 0] = 0
u0[:, -1] = 0
u1 = u0.copy()
unew = u1.copy()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize X and Y based on your code
x = np.linspace(0, L, nx)
y = np.linspace(0, L, ny)
X, Y = np.meshgrid(y, x)

time_text = ax.text(0.5, 0.95, '', transform=ax.transAxes, ha='center', s='')

def update(frame):
    global u0, u1, unew
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            unew[i, j] = 2 * u1[i, j] - u0[i, j] + lam ** 2 * (u1[i + 1, j] - 2 * u1[i, j] + u1[i - 1, j]) + lam ** 2 * (u1[i, j + 1] - 2 * u1[i, j] + u1[i, j - 1])
    u0 = u1.copy()
    u1 = unew.copy()
    ax.clear()
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_zlim(-1, 1)
    ax.set_zticks([-1, -0.5, 0, 0.5, 1])
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$u$')
    ax.plot_surface(X, Y, unew, cmap='viridis', shade=False)
    time_text.set_text('Time: {:.2f}'.format(frame * dt))

ani = animation.FuncAnimation(fig, update, frames=nt, interval=100, repeat=False)

# 保存为 GIF
writer = animation.PillowWriter(fps=30)
ani.save('wave_animation.gif', writer=writer)

plt.show()
