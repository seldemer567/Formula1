import math
import matplotlib.pyplot as plt
import numpy as np

plt.figure().set_figwidth(25)

# Constants
mu_s = 0.8  # Coefficient of static friction
mass = 798  # Mass of the car in kg
g = 9.81  # Acceleration due to gravity (m/s^2)
DT = 0.01 # Time step
T_MAX = 10.0 # Max time of the simulation
STEPS = int(T_MAX/DT)
x_0 = 0
y_0 = 0
v_0 = 50  # m/s

# Calculate the maximum static friction force
Fs = mu_s * mass * g

# Calculate the Turning force Ft = sqrt(Fs**2 - Fb**2)
def Ft(Fb):
    return math.sqrt(Fs**2 - Fb**2)

def ac_x(Fb, angle):
    Fx = (Ft(Fb) * math.sin(angle)) + ((-Fb) * math.cos(angle))  # All the forces on x-axis
    ax = Fx / mass
    return ax

def ac_y(Fb, angle):
    Fy = (-(Ft(Fb)) * math.cos(angle)) + ((-Fb) * math.sin(angle))  # All the forces on y-axis
    ay = Fy / mass
    return ay

def f1_trajectory(x_0, y_0, v_0, Fb):
    # Adjust the angle to give more horizontal movement
    angle_init = 45  # Change this angle to see different trajectories
    vx_0 = v_0*math.cos(math.radians(89.9))
    vy_0 = v_0*math.sin(math.radians(89.9))

    angle_0 = math.atan(vy_0/vx_0) # calcuate the angle of the velocity vector
    angle_d = math.degrees(angle_0) # convert the angle from radians to degrees

    ax_0 = 0
    ay_0 = 0

    t = [0]
    x = [x_0]
    y = [y_0]
    vx = [vx_0]
    vy = [vy_0]
    angle = [angle_0]
    degrees = [angle_d]
    ax = [ax_0]
    ay = [ay_0]

    # Main loop
    for i in range(STEPS):
        if math.hypot(vx[i], vy[i]) < 0.01:  # Break if velocity is close to zero
            break

        t.append(t[i] + DT)
        x.append(x[i] + vx[i] * DT)
        y.append(y[i] + vy[i] * DT)
        vx.append(vx[i] + ax[i] * DT)
        vy.append(vy[i] + ay[i] * DT)

        angle.append(math.atan2(vy[i], vx[i]))  # Use atan2 to handle full range of angles
        degrees.append(math.degrees(angle[i])) # converting each angle into degrees

        ax.append(ac_x(Fb, angle[i]))
        ay.append(ac_y(Fb, angle[i]))

        if y[-1] >= 200:
          vx[-1] = 0
          vy[-1] = 0
          break
        if y[-1] <= 150 and x[-1] >= 50:
          vx[-1] = 0
          vy[-1] = 0
          break

        if angle[i] <= 0:
          break

    return x, y, vx, vy



braking_force = range(500, 6200, 200)

for Fb in braking_force:
    x, y, vx, vy = f1_trajectory(x_0, y_0, v_0, Fb)
    plt.plot(x, y, label=f"{Fb}N")
    v_final = math.hypot(vx[-1], vy[-1])
    if v_final == 0:
      print(f'final velocity = {v_final}, force = {Fb}, crashed')
    else:
      print(f'final velocity = {v_final}, force = {Fb}')

plt.axvline(x=-2.5, ymin=0, ymax=0.667, color='black')
plt.axvline(x=50, ymin=0, ymax=0.4999, color='black')

plt.axhline(y=200, xmin=0.017, xmax=0.9, color='black')
plt.axhline(y=150, xmin=0.12, xmax=0.80, color='black')


plt.legend()
plt.title("Graph 1: Trajectory of F1 car with different braking forces")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.xlim((-10,500))
plt.ylim((0,300)) #setting a limit for the graph so that it stays in the first quadrant
ax = plt.gca()
ax.set_aspect('equal')
plt.show()
