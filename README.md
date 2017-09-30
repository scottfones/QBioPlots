# QBioPlots #

A collection of classes that solve common quantitative biology problems.

### Required Packages ###
* numpy
* [plotly](https://plot.ly/) 
* scipy

All of the classes assume online plotting, which requires [initialization](https://plot.ly/python/getting-started/). To switch to offline plotting use a find and replace on QBioPlots.py: py.plotly.plot -> py.offline.plot

## Classes ##

- [PlotODETwoByTwo](https://github.com/scottfones/QBioPlots#plotodetwobytwo---2x2-ode-system)
    - [Overview](https://github.com/scottfones/QBioPlots#overview) 
    - [Demo](https://github.com/scottfones/QBioPlots#demo) 
    - [Demo Model](https://github.com/scottfones/QBioPlots#demo-model)
    - [Demo Parameters](https://github.com/scottfones/QBioPlots#demo-parameters) 
    - [Usage](https://github.com/scottfones/QBioPlots#usage) 
- [PhasePlaneTwoByTwoWithCarry](https://github.com/scottfones/QBioPlots#phaseplanetwobytwowithcarry---phase-plane-of-2x2-ode-system-with-carry-capacities)
    - [Overview](https://github.com/scottfones/QBioPlots#overview-1) 
    - [Demo](https://github.com/scottfones/QBioPlots#demo-1) 
    - [Demo Model](https://github.com/scottfones/QBioPlots#demo-mode-1)
    - [Demo Parameters](https://github.com/scottfones/QBioPlots#demo-parameters-1) 
    - [Usage](https://github.com/scottfones/QBioPlots#usage-1) 

## PlotODETwoByTwo - 2x2 ODE System

### Overview ###
This class can be used to solve and plot a 2x2 system of IVP ODEs. 

### Demo ###
An example can be viewed with:

```
from QBioPlots import PlotODETwoByTwo as ode22

ode22.demo()
```

The example solves a competition model with the following parameters:

### Demo Model ###

![y_1 = r_1*x_1(k_1 - x_1 - a*x_2) / k_1](http://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20y_1%20%3D%20r_1x_1%5Cleft%20%28%20k_1%20-%20x_1%20-ax_2%20%5Cright%20%29/%20k_1)

![y_2 = r_2*x_2(k_2 - b*x_1 - x_2) / k_2](http://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20y_2%20%3D%20r_2x_2%5Cleft%20%28%20k_2%20-%20bx_1%20-%20x_2%20%5Cright%20%29%20/%20k_2)

### Demo Parameters ###
```
r_1 = 0.15      r_2 = 0.3
k_1 = 50        k_2 = 60
a = 0.2         b = 0.6
```
### Demo Output ###
![https://plot.ly/~scottfones/93.svg](/demo_plots/PlotODETwoByTwo.svg)

[**Interactive Plot**](https://plot.ly/~scottfones/93.embed)

### Usage ###

To solve a 2x2 system, the following parameters are necessary
```
x_start - First value of your domain
x_end   - Last value of your domain
steps   - Number of intervals over your domain
figure_title - (string) Title for the plot
x_label      - (string) Label for the x-axis
y_label      - (string) Label for the y-axis
x1_label     - (string) Label for the first dependent variable
x2_label     - (string) Label for the second dependent variable
eqn1 - (lambda) First equation of the system
eqn2 - (lambda) Second equation of the system
init_conds - (list) List containing the initial values for x1 and x2
```

Example:
```
from QBioPlots import PlotODETwoByTwo as ode22

# Solution Parameters
x_start = 0
x_end = 100
steps = 200

# y_1
r_1 = 0.15
k_1 = 50
a = 0.2

# y_2 
r_2 = 0.3
k_2 = 60
b = 0.6

# Plot Labels
figure_title = "2x2 Nonlinear ODE System"
x_label = "time (days)"
y_label = "population"
x1_label = "Population 1"
x2_label = "Population 2"

# Equations
eqn1 = lambda x1,x2: r_1*x1 * (k_1 - x1 - a*x2) / k_1
eqn2 = lambda x1,x2: r_2*x2 * (k_2 - b*x1 - x2) / k_2

# Initial Conditions
init_conds = [1,1]

ode22(x_start, x_end, steps, figure_title, x_label, y_label, x1_label, x2_label, eqn1, eqn2, init_conds)
```
**NOTE**: Equations one and two must defined using `lambda x1, x2: ` before your expression. The lambda functions are required to pass the expressions as parameters.



<hr>



## PhasePlaneTwoByTwoWithCarry - Phase Plane of 2x2 ODE System with Carry Capacities

### Overview ###
This class can be used to plot the phase plane of a 2x2 ODE system with carry capacities. These equations should be of the form:

![y_1 = r_1*x_1(k_1 - x_1 - a*x_2) / k_1](http://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20y_1%20%3D%20r_1x_1%5Cleft%20%28%20k_1%20-%20x_1%20-ax_2%20%5Cright%20%29/%20k_1)

![y_2 = r_2*x_2(k_2 - b*x_1 - x_2) / k_2](http://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20y_2%20%3D%20r_2x_2%5Cleft%20%28%20k_2%20-%20bx_1%20-%20x_2%20%5Cright%20%29%20/%20k_2)

### Demo ###
An example can be viewed with:

```
from QBioPlots import PhasePlaneTwoByTwoWithCarry as phase

phase.demo()
```

The example plots a phase plane with the following parameters:

### Demo Model ###

![y_1 = r_1*x_1(k_1 - x_1 - a*x_2) / k_1](http://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20y_1%20%3D%20r_1x_1%5Cleft%20%28%20k_1%20-%20x_1%20-ax_2%20%5Cright%20%29/%20k_1)

![y_2 = r_2*x_2(k_2 - b*x_1 - x_2) / k_2](http://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cfn_cm%20y_2%20%3D%20r_2x_2%5Cleft%20%28%20k_2%20-%20bx_1%20-%20x_2%20%5Cright%20%29%20/%20k_2)

### Demo Parameters ###
```
r_1 = 0.15      r_2 = 0.3
k_1 = 50        k_2 = 60
a = 0.2         b = 0.6
```
### Demo Output ###
![https://plot.ly/~scottfones/98.svg](/demo_plots/PhasePlaneTwoByTwoWithCarry.svg)

[**Interactive Plot**](https://plot.ly/~scottfones/98.embed)

### Usage ###

To solve a 2x2 system, the following parameters are necessary
```
x_start - First value for x-axis
x_end   - Last value for x-axis
x_steps - Number of intervals for x-axis
y_start - First value for y-axis
y_end   - Last value for y-axis
y_steps - Number of intervals for y-axis
figure_title - (string) Title for the plot
x_label      - (string) Label for the x-axis
y_label      - (string) Label for the y-axis
carry1 - Carry capacity for the first equation
carry2 - Carry capacity for the second equation
a - Interaction coefficient for the first equation
b - Interaction coefficient for the second equation
eqn1 - (lambda) First equation of the system
eqn2 - (lambda) Second equation of the system
init_conds - (list) List of initial values for x1 and x2
```

Example:
```
from QBioPlots import PhasePlaneTwoByTwoWithCarry as phase

# Solution Parameters
x_start = 0
x_end = 100
x_steps = 200
y_start = 0
y_end = 100
y_steps = 200

# y_1
r_1 = 0.15
k_1 = 50
a = 0.2

# y_2 
r_2 = 0.3
k_2 = 60
b = 0.6

# Plot Labels
figure_title = "2x2 Phase Plane with Carry Capacity"
x_label = "population size, N1"
y_label = "population size, N2"

# Equation Parameters
carry1 = 50
carry2 = 60
a = 0.15
b = 0.6

# Equations
eqn1 = lambda x1,x2: r_1*x1 * (k_1 - x1 - a*x2) / k_1
eqn2 = lambda x1,x2: r_2*x2 * (k_2 - b*x1 - x2) / k_2

# Initial Conditions
init_conds = [1,1]

phase(x_start, x_end, x_steps, y_start, y_end, y_steps, figure_title, 
      x_label, y_label, carry1, carry2, a, b, eqn1, eqn2, init_conds)
```
**NOTE**: Equations one and two must defined using `lambda x1, x2: ` before your expression. The lambda functions are required to pass the expressions as parameters.