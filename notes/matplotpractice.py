###**** playing with matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

###***standard functional plot
#plt.plot(x)
#plt.plot(y)

###***labels/title
# plt.xlabel('DUDE')
# plt.ylabel('SUH')
# plt.title('AHHHH')

###***2 plots in 1 canvas
# plt.subplot(1,2,1)
# plt.plot(x,y,'r')

# plt.subplot(1,2,2)
# plt.plot(y,x,'b')

###*** OBJECT ORIENTED

# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

# axes.plot(x,y)
# axes2.plot(y,x)

# axes.set_xlabel('DUDE')
# axes.set_ylabel('AHH SUH')
# axes.set_title('CARNE')

# axes2.set_xlabel('DUDE')
# axes2.set_ylabel('AHH SUH')
# axes2.set_title('CARNE')

###*** subplots vs figure & legend
# fig,axes = plt.subplots(nrows=1,ncols=2)

# axes[0].plot(x,x**2,label='lin')
# axes[0].set_title('UNO')

# axes[1].plot(y,x,label='squ')
# axes[1].set_title('DOS')

# axes[0].legend()
# axes[1].legend()

# plt.tight_layout()

###*** colors and line types
# fig = plt.figure()
# ax = fig.add_axes([0.1,0.1,.8,.8])

# ax.plot(x,y,color='purple',linewidth=5,
#         linestyle='-', marker='o',
#         markersize=50)

###set limits on axes
# ax.set_xlim([0,100])
# ax.set_ylim([0,500])

###*** ALWAYS NEED plt.show()
# plt.show()
