# Formula1
Formula 1 car trajectory in a 90 degree curve.
# Introduction
Formula One is not as simple as most may think; these professional drivers’ goal isn’t simply to get in the car and drive as fast as possible until the checkered flag is thrown; 
there is a science behind F1. The shape of the car is one of the most important aspects of Formula One driving; it affects the way air flows around the car, and as simple as it sounds, it isn’t.  
The car can go around curves at extremely high speeds with this specific shape. However, the driver must start breaking at the ideal spot to obtain the perfect trajectory. 
The physics behind measuring the ideal trajectory includes many complicated mathematical concepts in physics that may be too much to go over in one simple project. 
Therefore, below will be a simplified version of determining which trajectory with a certain breaking force will return the biggest final velocity.   
Therefore, below will be a simplified version of determining the breaking force that will provide the highest final velocity, which will then show how these components affect a Formula One car's trajectory.

For this project, we’ve decided only to consider the applied braking force, the turning force, the static friction, velocity, and acceleration of the car. 
The braking force determines how much the car will decelerate. The maximum braking force applied without skidding is limited to the coefficient of static friction and the normal force. 
If the braking force is ever greater than the coefficient of static friction and the normal force, this will result in the car skidding and going off track. 
The coefficient of static friction is the ratio of the force of friction between two surfaces and the force pressing them together. 
As the coefficient of static friction gets smaller, we will require a smaller force for the two surfaces to slip, leaving the driver to apply lower pressure on the braking pads in ideal conditions. 
Naturally, in Formula One, the coefficient of static friction is determined by the Fédération International de l’Automobile (FIA); 
they’ve set a range for the coefficient of friction between the tires and the road surface to be between 0.7 and 1.0. For this project, we set it to 0.8. 
Now, for the maximum static friction, the amount of force that must be applied to get the object in movement can be found by adding the braking and turning forces. 
In this case, we also would like to determine the maximum static friction by turning the car as much as possible with a set braking force. 
The turning force can be calculated using the following formula, $\sqrt{F_s^2 - F_b^2}$. Where Fb is the braking force, and Fs is the force of static friction, $F_s = \mu_s \cdot m \cdot g$. 
The minimum mass of a Formula One car for the 2024 season is 798 kilograms with no fuel. We’ve decided to stick with this mass for our project.

# Model and Numerical Method.
In our model, the trajectory of an F1 car is influenced by the braking force applied and the resulting forces such as the turning force on the car. The key parameters and forces involved are as follows:

## Model Description

### Forces and Angles
The primary forces acting on an F1 car are the braking force $F_b$ and the maximum static friction force $F_s$. The maximum static friction force is calculated using:


$F_s = \mu_s \cdot m \cdot g$


where $\mu_s$ is the coefficient of static friction, $(m)$ is the mass of the car, and $(g)$ is the acceleration due to gravity.

The turning force $(F_t)$ is derived from $(F_s)$ and $(F_b)$ using the equation:


 $F_t = \sqrt{F_s^2 - F_b^2}$


The acceleration components in the x and y directions are determined by the combined effect of $(F_t)$ and $(F_b)$ at a given angle $(\theta)$:

 $a_x = \frac{F_t \sin(\theta) - F_b \cos(\theta)}{m}$

 $a_y = \frac{-F_t \cos(\theta) - F_b \sin(\theta)}{m}$


## Numerical Model
The trajectory of the car is simulated using numerical integration. The initial conditions include the initial position \($x_0$, $y_0$\) and initial velocity $v_0$ with components:

 $v_{x0} = v_0 \cos(\theta)$

  $v_{y0} = v_0 \sin(\theta)$


### Equations of Motion
The equations of motion are updated at each time step $\Delta$ using:
$ x_{i+1} = x_i + v_{xi} \Delta t$
 $y_{i+1} = y_i + v_{yi} \Delta t$
 $v_{xi+1} = v_{xi} + a_{xi} \Delta t$
 $v_{yi+1} = v_{yi} + a_{yi} \Delta t$

The angle $(\theta)$ of the velocity vector is updated using:
$\theta = \tan^{-1}\left(\frac{v_y}{v_x}\right)$

### Numerical Integration Method
We employ Euler's method to solve the equations of motion. Euler's method updates the position and velocity iteratively:
$x_{i+1} = x_i + v_{xi} \Delta t$
$y_{i+1} = y_i + v_{yi} \Delta t$
$v_{xi+1} = v_{xi} + a_{xi} \Delta t$
$v_{yi+1} = v_{yi} + a_{yi} \Delta t$
The simulation runs until the car's velocity is close to zero or predefined conditions are met (e.g., specific $x$ and $y$ positions).

## Simulation and Results
The simulation iterates over a range of braking forces to determine the trajectory for each force. The results are plotted to visualize the trajectories and determine the impact of different braking forces on the car's final position and velocity.

### Overall
To achieve our goal of determining the ideal trajectory that maximizes the final velocity of the F1 car under different braking forces, we implemented a numerical model using Euler's method for solving the equations of motion. This model incorporated the braking force, turning force, static friction, velocity, and acceleration of the car. By varying the braking force within a specified range, we simulated the car's trajectory and analyzed the results to identify the braking force that results in the highest final velocity. This approach allowed us to visualize and understand the car's behavior under different braking conditions, providing insights into optimizing braking strategies in Formula One racing.

# Code Testing and Validation

There will be two aspects that will need to be validated for this project. The first one would be to validate the Golden Section Search used to insure it will properly detected the maximum. The second one would be to validate the correct time step needed get the highest final velocity for a given braking force.
### Validation of Golden Section

When using the Golden section to find the minimum or the maximum it is important to test it and make sure it does in fact work. Therefore, the golden section search was tested on a previous code for the maximum value.

The code below is from our frisbee model where we needed to find the maximum distance obtained for a given beta. The graph produced by this code does indeed show the maximum distance, therefore the golden section in this case is the appropriate version to use.

### Choosing the correct time step

Another aspect that needs to be considered is the time step which if not chosen correctly can have a different outcome. In our case it will have a difference when looking for the maximum final velocity for a given braking force. Therefore the code below tests for various time step on the golden section search. The results are then displayed on the graph with the optimal maximum velocity. As we can see the highest final velocity for a given braking force would be 16.95 m/s for a braking force of 3571.54 N using the a DT of 0.01. This confirms that the ideal DT to use for this project is 0.01.

##Results and Discussion

Our initial question: Which braking force provides the highest final velocity for an F1 car, and how does this force affect the car's trajectory? We set the coefficient of static friction to 0.8 and the mass of the car to 798 kg to match the minimum requirements for the 2024 season. It simplifies our calculations while remaining realistic.

To find the ideal braking force, we varied the braking force in increments of 200 N from 500 N to 6200 N. For each braking force, we simulated the car's trajectory using Euler's method to solve the equations of motion. The final velocity was calculated based on the car's velocity components at the end of the simulation.

The maximum static friction force $F_s$ is calculated as $F_s = \mu_s \cdot m \cdot g$, where $\mu _s$ = 0.8 , m = 798kg, and g = 9.81 m/s². The turning force $F_t$ is given by $F_t$ = $\sqrt{F_s^2 - F_b^2}$, where $F_b$ is the braking force.

The results show that the car's final velocity decreases as the braking force increases. This trend is expected because higher braking forces cause greater deceleration, reducing the car's speed more significantly. However, there is a range of braking forces where the car's final velocity approaches zero, indicating that the car has come to a stop or crashed. Specifically, for braking forces between 500 N and 3500 N, the final velocity is zero, and the car crashes.

Below are some of the final velocities for different braking forces:
- For \( $F_b$ = 500 \) N, the final velocity is 0 (crashed).
- For \( $F_b$ = 4100 \) N, the final velocity is approximately 12.93 m/s.
- For \( $F_b$ = 4300 \) N, the final velocity is approximately 11.42 m/s.
- For \( $F_b$ = 5300 \) N, the final velocity is approximately 4.20 m/s.
- For \( $F_b$ = 5500 \) N, the final velocity is approximately 2.86 m/s.
- For \( $F_b$ = 5900 \) N, the final velocity is approximately 0.64 m/s.
- For \( $F_b$ = 6100 \) N, the final velocity is approximately 0.079 m/s

(see graph 1 for more values)

From these results, we observe that the final velocity is highest at the lowest braking force of 3571 N, and decreases with increasing braking force. When the braking force is lower than approximately 3571 N, the car's velocity becomes zero, indicating a crash.

Our model simplifies real-life conditions by assuming constant coefficients and forces. In reality, factors such as tire wear, changing road conditions, and aerodynamic effects would also play significant roles. These simplifications limit the accuracy of our model when compared to actual F1 racing scenarios. However, despite these limitations, our model provides a useful framework for understanding the relationship between braking force and the car's trajectory and final velocity.

It would be interesting to further investigate how varying other parameters, such as the coefficient of static friction and initial velocity, affects the results. Allowing for different turning forces or adjusting the braking force dynamically during the simulation might provide additional insights into optimizing the trajectory and final velocity around a curve.

## Conclusion

Figure one shows the trajectory of a Formula One car under different braking forces. The trajectory provided shows the changes with the different braking forces while considering the friction and turning forces. For this plot, we’ve added contour lines to simulate turn 1, a 90-degree turn, in the Azerbaijan Grand Prix track. With this we were able to determine which trajectories go off track. Each car started at the same point, x = 0 and y = 0, each with the same mass, 798kg, their only difference is their braking force. For the braking force, we’ve set a range from 500 N to 6200 N with increments of 200. Our results show that the cars with a braking force between 500 N and 3500 N crashed into the upper horizontal line (200 m y-axis). Figure two shows how the final velocities change with different braking forces. This part of the program calculates the final velocity of a Formula One car for the different braking forces and determines which braking force results in the highest final velocity. As it was determined in the previous graph, those with braking forces between 500 N and 3500 N resulted in a final velocity of 0 m/s. Once the braking force reached around 4000 N, the car’s final velocity started to decrease, leading the cars to not pass over the apex of the turn, those with breaking forces of 5300 N and lower. With this program, we were able to find out which breaking force gives the highest velocity, which is 3571.54 N with a final velocity of 16.95 m/s.

**CITATIONS**

"Breaking Literature", *Dixecel Advanced Brake Technology*, https://www.dixcel.co.jp/en/literature/lid-2235/#:~:text=The%20higher%20the%20coefficient%20of%20friction%2C%20the%20less%20fluid%20pressure,it%20very%20difficult%20to%20brake.

Abdel-Rahim, Ahmed. "Road Vehicle Performance: Braking", *University of Idaho*,9 April 2009, https://www.webpages.uidaho.edu/ahmed/ce322/class%20notes/Class-6%20the%20vehicle%20-%20Braking.pdf.

Toet, William. "Aerodynamic of F1", *Technical F1 Dictionary*, https://www.formula1-dictionary.net/aerodynamics_of_f1.html.

"2024 Formula 1 Techinical Regulation", *FIA*, 25 April 2023, https://www.fia.com/sites/default/files/fia_2024_formula_1_technical_regulations_-_issue_1_-_2023-04-25.pdf.

D, Bob. "Why is the coefficient of static friction used in the formula for the stopping distance when there is no relative motion between tyres and road?", *Physics Stack Exchange*, 10 September 2023, https://physics.stackexchange.com/questions/779681/why-is-the-coefficient-of-static-friction-used-in-the-formula-for-the-stopping-d#:~:text=That%20friction%20force%20causes%20the,kinetic%20and%20the%20wheels%20skid.
