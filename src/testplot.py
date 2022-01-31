import sys
import cv2
from colordetection import ColorDetector
import os
import sys
import numpy as np
import plotly.plotly as py
from plotly import tools
import plotly.graph_objs as go
tools.set_credentials_file(username='franklin0404', api_key='hmwl7CsktLwXvRkMeL6c')
x, y, z = np.array(1), np.array(2), np.array(3)
print(x)
trace1 = go.Scatter3d(
                      x=x,
                      y=y,
                      z=z,
                      mode='markers',
                      marker=dict(
                                  size=12,
                                  line=dict(
                                            color='red',
                                            width=0.5
                                            ),
                                  opacity=0.8
                                  )
                      )
layout = go.Layout(
                   margin=dict(
                               l=0,
                               r=0,
                               b=0,
                               t=0
                               )
                   )
data = [trace1]
fig = go.Figure(data=data, layout=layout)
x, y, z = np.array(2), np.array(3), np.array(4)
print(x)
trace1 = go.Scatter3d(
                      x=x,
                      y=y,
                      z=z,
                      mode='markers',
                      marker=dict(
                                  size=12,
                                  line=dict(
                                            color='rgba(217, 217, 217, 0.14)',
                                            width=0.5
                                            ),
                                  opacity=0.8
                                  )
                      )
layout = go.Layout(
                   margin=dict(
                               l=0,
                               r=0,
                               b=0,
                               t=0
                               )
                   )
data = [trace1]
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='simple-3d-scatter')
