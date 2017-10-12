"""
This module contains classes designed to automate repetitive
quantitative biology tasks.

Classes:
    PlotSystemWRTTime: Plots 1 to 10 ODEs wrt time
    PhasePlaneTwoByTwoWithCarry: Plots a 2D phase plane

Todo:
    * Forward Euler
    * Break out constructors into discrete methods
"""


import numpy as np
import plotly as py
import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff
from scipy.integrate import odeint


class PlotSystemWRTTime(object):
    """
    Designed to solve and plot NxN systems of the form:

        eqn_1' = f_1(x1, ..., x_N)
        ...
        eqn_N' = f_N(x1, ..., x_N)

        where N <= 10.

    Parameters:  (x_start, x_end, steps, figure_title, x_label,
                    y_label, x1_label, x2_label, eqn1, eqn2, initial_conds[])

                x_start - (int) First value of your domain
                x_end   - (int) Last value of your domain
                steps   - (int) Number of intervals over your domain
                figure_title - (string) Title for the plot
                x_label      - (string) Label for the x-axis
                y_label      - (string) Label for the y-axis
                var_labels - (list) List of dependent variable labels
                eqn_list   - (list) List of equations
                init_conds - (list) List of initial values

    ODEs must be defined as lambda functions with x1,...,x_n as the variables.
    They should be of the form \"eqn1 = lambda x1,x2: f(x1,x2)\"
    """

    def __init__(self, x_start, x_end, steps, figure_title, x_label, y_label,
                 var_labels=[], eqn_list=[], init_conds=[]):

        # Parameter Check - List Lengths Should Agree
        if  len(eqn_list) != len(init_conds):
            raise ValueError( "Number of equations does not equal number of \
                               initial conditions. Equations: {}, Conditions: \
                               {}".format(len(eqn_list), len(init_conds)) )

        elif len(var_labels) != len(init_conds):
            raise ValueError( "Number of variable labels does not equal number \
                               of initial conditions. Labels: {}, Conditions: \
                               {}".format(len(var_labels), len(init_conds)) )

        # Define Domain
        t = np.linspace(x_start, x_end, steps+1)

        # ODE Function
        def f(init_conds, t):
            return [eqn(*init_conds) for eqn in eqn_list]

        # ODE Solutions (Pandas Dataframe)
        pd_solutions = pd.DataFrame( odeint( f,
                                             init_conds,
                                             t,
                                             atol=1.0e-20,
                                             rtol=1.0e-13),
                                     columns=var_labels)

        # Data Structures
        data = [go.Scatter(x=t,
                           y=pd_solutions[label],
                           mode='lines',
                           name=label,
                           line=dict(width=5))
                for label in var_labels]

        # Figure Layout
        layout = go.Layout(
            title=figure_title,
            autosize=True,

            font=dict(
                size=22,
            ),

            xaxis=dict(
                title=x_label,
                showgrid=False,
                titlefont=dict(
                    size=20,
                ),
                tickfont=dict(
                    size=14,
                ),
                zerolinewidth=1,
                ticks='outside',
            ),

            yaxis=dict(
                title=y_label,
                showgrid=False,
                titlefont=dict(
                    size=20,
                ),
                tickfont=dict(
                    size=14,
                ),
                zerolinewidth=1,
                ticks='inside',
            ),

            legend=dict(
                x=1,
                y=1,
                bordercolor='#404040',
                bgcolor="rgba(255, 255, 255, 0.5)",
                borderwidth=1,
                font=dict(size=16),
                xanchor='right',
                yanchor='top',
            ),
        )

        # Create Figure and Plot
        fig = go.Figure(data=data, layout=layout)
        py.plotly.plot(fig, filename=figure_title)

    @classmethod
    def demo1(cls):
        'Creates instance with predefined variables to serve as an example'

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
        figure_title = "Demo: 2x2 Nonlinear ODE System"
        x_label = "time (days)"
        y_label = "population"
        var_labels = ["Population 1", "Population 2"]

        # Equations
        eqn1 = lambda x1, x2: r_1*x1 * (k_1 - x1 - a*x2) / k_1
        eqn2 = lambda x1, x2: r_2*x2 * (k_2 - b*x1 - x2) / k_2
        eqn_list = [eqn1, eqn2]

        # Initial Conditions
        init_conds = [1, 1]

        cls(x_start, x_end, steps, figure_title, x_label, y_label,
            var_labels, eqn_list, init_conds)

    @classmethod
    def demo2(cls):
        'Demo plot using equations and parameters from Dunster et al. (2015)'

        # Constants
        k_1 = 8
        k_m1 = 3.02e-2
        V_e = 3.3e-9
        V_p = 7.4e-18
        A_v = 6.0221409e23
        k_2 = 3.02e-2
        k_3 = 9.55e5
        rho_1 = 5.13e-1
        gamma_1 = 3.53

        # Define Initial Conditions
        L_0 = 3e-2
        g_0 = 5000
        s_0 = 2763
        G_0 = 0
        G_p_0 = 0
        G_b0_0 = 0
        G_b1_0 = 0
        init_conds = [g_0, G_0, G_p_0, G_b0_0, G_b1_0, L_0, s_0]

        # Domain
        x_start = 0
        x_end = 250
        steps = 2500

        # Equations
        # dg / dt
        f0 = lambda x1,x2,x3,x4,x5,x6,x7: ( -1 * k_1 * x1 * x6
                                            + k_m1 * x2 )
        # dG / dt
        f1 = lambda x1,x2,x3,x4,x5,x6,x7: ( k_1 * x1 * x6 - k_m1 * x2
                                            - k_2 * x2 )
        # dG_p / dt
        f2 = lambda x1,x2,x3,x4,x5,x6,x7: ( k_2 * x2 - k_3 / ( V_p * A_v )
                                            * x3 * x7 )
        # dG_b0 / dt
        f3 = lambda x1,x2,x3,x4,x5,x6,x7: ( k_3 / ( V_p * A_v ) * x3 * x7
                                            - rho_1 * x4 + gamma_1 * x5 )
        # dG_b1 / dt                                    
        f4 = lambda x1,x2,x3,x4,x5,x6,x7: rho_1 * x4 - gamma_1 * x5
        # dL / dt
        f5 = lambda x1,x2,x3,x4,x5,x6,x7: ( -1 * k_1 / ( V_e * A_v ) * x1
                                            * x6 + k_m1 / ( V_e * A_v ) * x2 )
        # ds / dt
        f6 = lambda x1,x2,x3,x4,x5,x6,x7: ( -1 * k_3 / ( V_p * A_v )
                                            * x7 * x3 )
        
        eqn_list = [f0, f1, f2, f3, f4, f5, f6] 

        # Figure Title and Labels
        figure_title = "Demo: Model A, Dunster et al. (2015)"
        x_label = "time (seconds)"
        y_label = "molecules"
        var_labels = [
            "GPVI",
            "Ligand-GPVI Complex",
            "Phosphorylated Receptor",
            "Bound Syk",
            "Phosphorylated Syk",
            "Ligand",
            "Cytosolic Syk"
        ]

        cls(x_start, x_end, steps, figure_title, x_label, y_label, 
            var_labels, eqn_list, init_conds)




class PhasePlaneTwoByTwoWithCarry(object):
    """ Designed to solve and plot the phase plane for 2x2 systems
        of the form:

            eqn1 = r_1*x1 * (k_1 - x1 - a*x_2) / k_1
            eqn2 = r_2*x2 * (k_2 - b*x1 - x_2) / k_2

        Parameters:  (x_start, x_end, x_steps, y_start, y_end, y_steps, figure_title,
                      x_label, y_label, carry1, carry2, a, b, eqn1, eqn2, initial_conds[])

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
                      
        ODEs must be written as lambda functions with x1,...,x_n as the variables.
        They should be of the form \"eqn1 = lambda x1,x2: f(x1,x2)\"

    """

    def __init__(self, x_start, x_end, x_steps, y_start, y_end, y_steps, figure_title, 
                 x_label, y_label, carry1, carry2, a, b, eqn1, eqn2):
        'Constructor for PhasePlaneTwoByTwoWithCarry'

        e1 = [ ( (carry1-a*carry2)/(1-a*b) ), 
               ( (carry2-b*carry1)/(1-a*b) ) ]
        e2 = [ 0, carry2 ]
        e3 = [ carry1, 0 ] 
        e4 = [ 0, 0 ]

        if (x_start == 0) : x_start = 0.01
        if (y_start == 0) : y_start = 0.01

        x_coords = np.linspace(x_star, x_end, x_steps)
        y_coords = np.linspace(y_start, y_end, y_steps) 

        x_mesh, y_mesh = np.meshgrid(x_coords, y_coords)

        u = eqn1(x_mesh, y_mesh)
        v = eqn2(x_mesh, y_mesh)

        fig = ff.create_streamline(x_coords, y_coords, u, v, 
                                    arrow_scale=( (x_end - x_start)/60 ), 
                                    density=1.1,
                                    name='Streamline')

        p1 = go.Scatter(x=[e1[0]], y=[e1[1]],
                        mode='markers',
                        marker=go.Marker(size=14),
                        name='Equilibrium 1')
        p2 = go.Scatter(x=[e2[0]], y=[e2[1]],
                        mode='markers',
                        marker=go.Marker(size=14),
                        name='Equilibrium 2')
        p3 = go.Scatter(x=[e3[0]], y=[e3[1]],
                        mode='markers',
                        marker=go.Marker(size=14),
                        name='Equilibrium 3')
        p4 = go.Scatter(x=[e4[0]], y=[e4[1]],
                        mode='markers',
                        marker=go.Marker(size=14),
                        name='Equilibrium 4')
        
        fig['data'].append(p1)
        fig['data'].append(p2)
        fig['data'].append(p3)
        fig['data'].append(p4)

        fig['layout'] = go.Layout(
            title = figure_title,
            autosize = True,

            font = dict(
                size = 22,
            ),

            xaxis = dict(
                title = x_label,
                showgrid = False,
                titlefont=dict(
                    size=20,
                ),
                tickfont=dict(
                    size=14,
                ),
                zerolinewidth=1,
                ticks = 'outside',
            ),

            yaxis = dict(
                title = y_label,
                showgrid = False,
                titlefont=dict(
                    size=20,
                ),
                tickfont=dict(
                    size=14,
                ),
                zerolinewidth=1,
                ticks = 'inside',
            ),
        )

        py.plotly.plot(fig, filename=figure_title)

    @classmethod
    def demo(cls):
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
        figure_title = "Demo: 2x2 Phase Plane with Carry Capacity"
        x_label = "$N_1$"
        y_label = "$N_2$"       

        # Equations
        eqn1 = lambda x1,x2: r_1*x1 * (k_1 - x1 - a*x2) / k_1
        eqn2 = lambda x1,x2: r_2*x2 * (k_2 - b*x1 - x2) / k_2

        cls(x_start, x_end, x_steps, y_start, y_end, y_steps, figure_title, 
            x_label, y_label, k_1, k_2, a, b, eqn1, eqn2)
