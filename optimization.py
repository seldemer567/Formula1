import math
import matplotlib.pyplot as plt
import time

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


def golden_section(f,x1,x2,**kwargs):

  start_time=time.time()

  # Setting the max number of steps and the accuracy
  NSTEPS = kwargs.get("NSTEPS",1000)
  ACCURACY = kwargs.get("ACCURACY",1e-2)


  # Defining the constants for the ratios with gr1 < gr2
  gr2 = 2/(1+math.sqrt(5))
  gr1 = 1.0-gr2

  x3 = x1 + (x2 -x1)*gr1
  x4 = x1 + (x2 - x1)*gr2

  f3 = f(x3)
  f4 = f(x4)

  for i in range(NSTEPS):
    if (x2 - x1)/((x1 + x2)/2)< ACCURACY:
      # this will end the loop
      break

    # changed this so it checks if f3 > f4 than the previous (f3 < f4)
    if f3 > f4:
      x2 = x4
      x4 = x3
      f4 = f3
      x3 = x1 + (x2 -x1)*gr1
      f3 = (f(x3))
    else:
      x1 = x3
      x3 = x4
      f3 = f4
      x4 = x1 + (x2 - x1)*gr2
      f4 = f(x4)

  return (x1+x2)/2,f((x1+x2)/2)


Fs = mu_s * mass * g  # Calculate the maximum static friction force

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


# same as f1_trajectory, but modfied to return the last velocity value of each iteration
def last_vx(Fb):

    # Constants
    x_0 = 0
    y_0 = 0
    v_0 = 50 # m/s

    # Adjust the angle to give more horizontal movement
    angle_init = 45  # Change this angle to see different trajectories
    vx_0 = v_0*math.cos(math.radians(89.9))
    vy_0 = v_0*math.sin(math.radians(89.9))

    angle_0 = math.atan(vy_0/vx_0)
    angle_d = math.degrees(angle_0)

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
        degrees.append(math.degrees(angle[i]))

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

    return vx[-1]

braking_force = range(600, 6200, 1)
vx = []
F_b = []

for Fb in braking_force:
  vx.append(last_vx(Fb))
  F_b.append(Fb)

max_F_b, max_vx = golden_section(last_vx,  0, 6200)

print(f'The max Braking Force that gives the highest velocity is {max_F_b:.2f} N.')
print(f'The max Velocity for the given Braking force is {max_vx:.2f} m/s.')

plt.plot(F_b, vx)
plt.scatter(max_F_b, max_vx, color='red', label='Maximum velocity')
plt.title("Graph 2: Final Velocity of Each Interation With it's Given Braking force")
plt.xlabel(" Fb(N)")
plt.ylabel("Final Velocity (m/s)")
plt.show()
