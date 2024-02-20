import numpy as np
import matplotlib.pyplot as plt

# Define T1 relaxation time in seconds
T1 = 1.0

# Define initial magnetization
M0 = 1.0

# Define starting point
t0 = 0.5

# Create time array from 0 to 3*T1 with 1000 points
t = np.linspace(0, 3*T1, 1000)

# Calculate magnetization at each time point with condition: before t0, value is M0; after t0, it follows the T1 relaxation function.
Mz = np.piecewise(t, [t < t0, t >= t0], [M0, lambda x: M0*(1 - np.exp(-(x-t0)/T1))])

# Plot
# Make all the text in the plot bigger
plt.rcParams.update({'font.size': 30})
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(t, Mz, label='Magnetization')
ax.set_xlabel('Time (s)')
# Move x-axis label to the right
ax.xaxis.set_label_coords(0.95, -0.025)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
# Add  arrow for the time  direction
ax.arrow(0, 0, 3*T1, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
# Add  arrow for the magnetization direction
ax.arrow(0, 0, 0, M0, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.set_ylabel('Magnetization')
ax.set_title('T1 Relaxation')
ax.grid(True)

# Add T1 vertical line but only until it intersects with the curve
ax.plot([T1+t0, T1+t0], [0, 0.63*M0], color='red', linestyle='dashed')
# Indicate T1 on the  x-axis
ax.text(T1+t0, -0.1*M0, 'T1', color='red', ha='center')

# Add t0 vertical line going up to the M0
ax.plot([t0, t0], [0, M0], color='green', linestyle='dashed')
# Indicate t0 on the x-axis
ax.text(t0, -0.1*M0, 't0', color='green', ha='center')

# Add horizontal equilibrium magnetization indicator but make it start a little bit to the  right
ax.hlines(M0, t0+0.1*T1, 3*T1, color='blue', linestyle='dashed')
# Indicate M0 on the  y-axis move it to  the left a bit
ax.text(-0.3*T1, M0, 'Mz', color='blue', va='center')

# Remove the outside grid lines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.legend()
plt.show()
