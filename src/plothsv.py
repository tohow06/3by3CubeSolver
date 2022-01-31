import sys
import cv2
from colordetection import ColorDetector
import os
import sys
import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import csv
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
tools.set_credentials_file(username='franklin0404', api_key='hmwl7CsktLwXvRkMeL6c')
"""fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')"""
flag = 0
data = [0, 0, 0, 0, 0, 0]
for color in ['orange', 'red', 'blue', 'green', 'yellow', 'white']:
    i = 0
    h = []
    s = []
    v = []
    pts=np.loadtxt('testcolor_' + color + '.txt')
    h,s,v=zip(*pts)
    size = 1
    
    if color == 'red':
        size = 7
    data[flag] = go.Scatter3d(x = h, y = s, z = v, mode = 'markers', marker = dict(size = size, line = dict(color = color, width = 0.5), opacity = 0.8))
    """with open('testcolor_' + color + '.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            i += 1
            row = np.array(row)
            row = row.astype(np.int)
            h.append(row[0])
            s.append(row[1])
            v.append(row[2])
            #print(row[0])
            data[flag] = go.Scatter3d(x = h, y = s, z = v, mode = 'markers', marker = dict(size = 12, line = dict(color = color, width = 0.5), opacity = 0.8))"""
    flag += 1
    print(flag)
layout = go.Layout(
                   margin=dict(
                               l=0,
                               r=0,
                               b=0,
                               t=0
                               )
                   )
"""ax.set_xlabel('h')
ax.set_ylabel('s')
ax.set_zlabel('v')"""
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='simple-3d-scatter')
