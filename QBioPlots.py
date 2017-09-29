import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from scipy.integrate import odeint

class PlotODETwoByTwo (object):
    'Uses Plot.ly to plot solutions to a 2x2 system of ODEs. The input equations must be written with x1 and x2 as the variables'

    def __init__(self, steps, x_start, x_end, figure_title, x_label,
                 y_label, x1_label, x2_label, eqn1, eqn2, init_conds = []):
        """Solves and Plots 2x2 Systems of ODEs

           Parameters:  (steps, x_start, x_end, figure_title, x_label, 
                         y_label, x1_label, x2_label, eqn1, eqn2, initial_conds[])

                        steps - The number of values on which the ODEs should be evaluated

        """
        
        t = np.linspace(x_start, x_end, steps+1)

        def f(init_conds, t):
            'Function that defines system of equations and takes aninitial condition'
            x1 = init_conds[0]
            x2 = init_conds[1]

            f0 = eqn1(x1,x2)
            f1 = eqn2(x1,x2)

            return [f0, f1]

        A = odeint(f, init_conds, t, atol=1.0e-20,rtol=1.0e-13)

        print("{}".format(A))

        y1 = A[:,0]
        y2 = A[:,1]

        trace0 = go.Scatter(
            x = t,
            y = y1,
            mode = 'lines',
            name = x1_label,
            line = dict(
                width = 5
            )
        )

        trace1 = go.Scatter(
            x = t,
            y = y2,
            mode = 'lines',
            name = x2_label,
            line = dict(
                width = 5
            )   
        )

        data = [trace0, trace1]

        layout = go.Layout(
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

        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='2x2 Nonlinear ODEs')

    @classmethod
    def demo(cls):
        'Creates instance with predefined variables to serve as an example'

        # Solution Parameters
        steps = 200
        x_start = 0
        x_end = 100

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
        x1_label = "Population 1"
        x2_label = "Population 2"

        # Equations
        eqn1 = lambda x1,x2: r_1*x1 * (k_1 - x1 - a*x2) / k_1
        eqn2 = lambda x1,x2: r_2*x2 * (k_2 - b*x1 - x2) / k_2

        # Initial Conditions
        init_conds = [1,1]

        cls(steps, x_start, x_end, figure_title, x_label, y_label, x1_label, x2_label, eqn1, eqn2, init_conds)


'''
class PhasePlanePrinter():
    'Uses Plot.ly to print phase plane diagrams for given input systems.'

    def __init__(self, e1, e2, n, xs, xe, ys, ye):
        # Update parameters
        eqn1 = e1
        eqn2 = e2
        steps = n
        x_start = xs
        x_end = xe
        y_start = ys
        y_end = ye    

        x_vals = np.linspace(x_start, x_end, steps)
        y_vals = np.linspace(y_start, y_end, steps)
        y_mesh, x_mesh =  np.meshgrid(x_vals, y_vals)    
        
        eqn1 = 0.1*x_mesh*(50-x_mesh-0.1*y_mesh)/50
        eqn2 = 0.3*y_mesh*(60-0.6*x_mesh-y_mesh)/60

        print("{}".format(eqn1))
        print("{}".format(eqn2))

        fig = ff.create_streamline(x_vals, y_vals, eqn1, eqn2, arrow_scale=.1)
        print("{}".format(fig))
        py.plot(fig, filename='Streamline Plot Example')

    @classmethod
    def demo(self):
        steps = 10000    
    
        x_start = 0
        x_end = 100
        y_start = 0
        y_end = 50

        x_vals = np.linspace(x_start, x_end, steps)
        y_vals = np.linspace(y_start, y_end, steps)

        eqn1 = 0.1*x_vals*(50-x_vals-0.1*y_vals)/50
        eqn2 = 0.3*y_vals*(60-0.6*x_vals-y_vals)/60
        PhasePlanePrinter(eqn1, eqn2, steps, x_start, x_end, y_start, y_end)
'''
