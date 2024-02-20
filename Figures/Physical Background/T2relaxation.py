import numpy as np
import matplotlib.pyplot as plt

# Define T2 relaxation time in seconds
T2 = 1.0

# Define initial magnetization
M0 = 1.0

# Define starting point
t0 = 0.5

# Create time array from 0 to 3*T2 with 1000 points
t = np.linspace(0, 3*T2, 1000)

# Calculate magnetization at each time point with condition: before t0, value is 0; after t0, it follows the T2 relaxation function.
Mxy = np.piecewise(t, [t < t0, t >= t0], [0, lambda x: M0*np.exp(-(x-t0)/T2)])

# Plot
# Make all the text in the plot bigger
plt.rcParams.update({'font.size': 30})
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(t, Mxy, label='Magnetization')
ax.set_xlabel('Time (s)')
# Move x-axis label to the right
ax.xaxis.set_label_coords(0.95, -0.025)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
# Add  arrow for the time  direction
ax.arrow(0, 0, 3*T2, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
# Add  arrow for the magnetization direction
ax.arrow(0, 0, 0, M0, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.set_ylabel('Magnetization')
ax.set_title('T2 Relaxation')
ax.grid(True)

# Add T2 vertical line but only until it intersects with the curve
ax.plot([T2+t0, T2+t0], [0, 0.37*M0], color='red', linestyle='dashed')
# Indicate T2 on the  x-axis
ax.text(T2+t0, -0.1*M0, 'T2', color='red', ha='center')

# Add t0 vertical line going up to the M0
ax.plot([t0, t0], [0, M0], color='green', linestyle='dashed')
# Indicate t0 on the x-axis
ax.text(t0, -0.1*M0, 't0', color='green', ha='center')

# Add horizontal equilibrium magnetization indicator but make it start a little bit to right
ax.hlines(M0, t0+0.1*T2, 3*T2, color='blue', linestyle='dashed')
# Indicate M0 on the  y-axis move it to  the left a bit
ax.text(-0.5*T2, M0, 'Mxy(t=t0)', color='blue', va='center')

# Remove the outside grid lines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.legend()
plt.show()
