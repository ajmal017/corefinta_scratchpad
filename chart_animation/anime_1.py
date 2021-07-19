from time import sleep
import matplotlib.pyplot as plt
import numpy as np
#import serial

# https://stackoverflow.com/questions/54557530/matplotlib-real-time-plotting-in-python

from time import sleep
import matplotlib.pyplot as plt
import numpy as np
#import serial

# specify how many points to show on the x-axis
xwidth = 10

# use real-time plotting
plt.ion()

# setup each of the subplots
ax = []
fig, ax[0:7] = plt.subplots(7, 1, sharex=False, sharey=False)

# set up each of the lines/curves to be plotted on their respective subplots
lines = {index: Axes_object.plot([],[])[0] for index, Axes_object in enumerate(ax)}

# cache background of each plot for fast re-drawing, AKA Blit
ax_bgs = {index: fig.canvas.copy_from_bbox(Axes_object.bbox)
          for index, Axes_object in enumerate(ax)}

# initial drawing of the canvas
fig.canvas.draw()

# setup variable to contain incoming serial port data
y_data = {index:[0] for index in range(len(ax))}
x_data = [-1]

def update_data(new_byte, ):
    x_data.append(x_data[-1] + 1)
    for i, val in enumerate(new_byte):
        y_data[i].append(val)

def update_graph():
    for i in y_data.keys():
        # update each line object
        lines[i].set_data(x_data, y_data[i])

        # try to set new axes limits
        try:
            ax[i].set_xlim([x_data[-1] - xwidth, x_data[-1]])
            if max(y_data[i][-xwidth:]) > ax[i].get_ylim()[1]:
                new_min = min(y_data[i][-xwidth:])
                new_max = max(y_data[i][-xwidth:])
                ax[i].set_ylim([new_min-abs(new_min)*0.2, new_max+abs(new_max)*0.2])
        except:
            continue

    fig.canvas.draw()

#ser = serial.Serial('COM3', 115200) # Establish the connection on a specific port
#byte=ser.readline() #first line not to be plotted


while x_data[-1] < 30:
    # ser.write(b'9') # send a command to the arduino
    # byte=ser.read(7) #read 7 bytes back
    byte = np.random.rand(7)

    update_data(byte)
    update_graph()

    sleep(.1) # Delay for an arbitrary amount of time


