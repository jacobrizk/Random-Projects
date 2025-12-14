#Jacob Rizk
#Sine Wave Generator

import math
import matplotlib.pyplot as plt

#inputs
runtime = 0.00005 #seconds
amp = 1 #unitless
freq = 20000 #hz

#deriv
ang_freq = freq * 2 * math.pi #sin(x) frequnecy is 2pi, adjusts value for freq of time for f(x)
x_step = runtime/freq
n_sample = int((1/x_step) * runtime)

#making lists
x_axis = []
y_axis = []

#wave loop
for i in range(n_sample + 1):
    #finding x and f(x)
    x = x_step * i
    y = amp * math.sin(x * ang_freq) # f(x) = A*sin(t*f)

    #adding to list for each sample
    x_axis.append(x)
    y_axis.append(y)

    #print("(",x,",",y,")") #numbered plot

#making plot
plt.plot(x_axis,y_axis)
plt.grid()
plt.show()