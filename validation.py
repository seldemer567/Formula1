# @title

def golden_section(f,x1,x2,**kwargs):

  start_time=time.time()

  # Setting the max number of steps and the accuracy
  NSTEPS = kwargs.get("NSTEPS",1000)
  ACCURACY = kwargs.get("ACCURACY",1e-2)

  '''Part 5'''
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

# constants
DT = 0.001 # Time step
T_MAX = 10.0 # Max time of the simulation
STEPS = int(T_MAX/DT)
g = 9.81
RADIUS = 0.135
area = math.pi*RADIUS**2
MASS = 0.175
rho = 1.23

def acceleration_xy(v_x: float, v_y: float, ALPHA:float) -> tuple[float, float]:
    v = (v_x**2+v_y**2)**0.5
    drag_co = 0.085+3.30*(ALPHA-(-0.052))**2
    lift_co = 0.13 + 3.09*ALPHA


    drag_force = 1/2*rho*area*drag_co*v**2 #calculates drag force in x and y
    drag_force_x = drag_force*v_x/v
    drag_force_y = drag_force*v_y/v

    lift_force = 1/2*rho*area*lift_co*v**2 #calculates lift force in x and y
    lift_force_x = lift_force*v_y/v
    lift_force_y = lift_force*v_x/v


    acceleration_x = (-lift_force_x-drag_force_x)/MASS #calculates acceleration in x and y including lift and drag
    acceleration_y = (-MASS*g + lift_force_y - drag_force_y)/MASS

    return acceleration_x, acceleration_y


def max_range(beta):

  x_0 = 0 # Initial position in x in meters
  y_0 = 1 # Initial position in y in meters
  v_0 = 12 # Initial speed in m/s
  theta = 20

  theta_rad = theta*math.pi/180 # converts the angles in radians
  beta_rad = beta*math.pi/180
  vx_0 = v_0*math.cos(theta_rad) # calculates initial vx
  vy_0 = v_0*math.sin(theta_rad) # calculates initial vy

  alpha_rad = beta_rad - theta_rad #ALPHA is calculated

  t = [0]
  x = [x_0]
  y = [y_0]
  vx = [vx_0]
  vy = [vy_0]
  theta_lst = [theta_rad]
  ax_0, ay_0 = acceleration_xy(vx_0,vy_0,alpha_rad)
  ax = [ax_0]
  ay = [ay_0]

  for i in range(STEPS): # this step creates a list with the values for x and y in order to create the graph
      t.append(t[i]+DT)
      x.append(x[i]+vx[i]*DT)
      y.append(y[i]+vy[i]*DT)
      vx.append(vx[i]+ax[i]*DT)
      vy.append(vy[i]+ay[i]*DT)
      theta_lst.append(math.atan(vy[i]/vx[i]))
      alpha_rad = beta_rad - theta_lst[i]
      ax_i1, ay_i1 = acceleration_xy(vx[i],vy[i],alpha_rad)
      ax.append(ax_i1)
      ay.append(ay_i1)

      if y[-1] <= 0:
          break

  # return the last x value of each projection
  return (x[-1])


x_max = []
angle = np.arange(0,30,0.2) # creating a range of beta angles to be tested

for beta in angle:
  x_max.append(max_range(beta)) # append the last x value of each projection into the list x_max

#calling Golden Section to return the value of beta for the maximum distance
max_beta, max_x = golden_section(max_range, 0, 15)

print(f'The value of beta for the furthest possible distance is: {max_beta} degrees.')
print(f'The furthest distance is {max_x} meters.')


plt.plot(angle, x_max,  label = 'maximum')
plt.scatter(max_beta, max_x, color='red', label='Maximum Distance')
plt.title("Figure 3: Max range for different launch angles")
plt.xlabel("Beta (degree)")
plt.ylabel("Rmax (m)")
