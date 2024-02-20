import numpy as np
import matplotlib.pyplot as plt

# Define the solution space range and the global minimum position
solution_space_range = (0, 5)
global_min = (2.5, 2.5)  # Example global minimum positions

# Solution quality function (Gaussian centered at the global minimum)
def solution_quality(tuning_voltage, matching_voltage):
    return np.exp(-((tuning_voltage - global_min[0])**2 + (matching_voltage - global_min[1])**2) / 1.0)

# Create the grid for the heatmap
tuning_voltages = np.linspace(solution_space_range[0], solution_space_range[1], 100)
matching_voltages = np.linspace(solution_space_range[0], solution_space_range[1], 100)
tuning_grid, matching_grid = np.meshgrid(tuning_voltages, matching_voltages)
quality_grid = solution_quality(tuning_grid, matching_grid)

# Plot the heatmap
plt.figure(figsize=(10, 8))
plt.imshow(quality_grid, cmap='Greys', extent=solution_space_range*2, origin='lower')

# Coarse Search (Search 1)
for t_volt in np.linspace(0, 5, 6):
    for m_volt in np.linspace(0, 5, 6):
        plt.scatter(t_volt, m_volt, c='red', label='Coarse Search (1V Steps)' if (t_volt, m_volt) == (0, 0) else "", marker='x')

# Precise Tuning Search (Search 2)
tuning_voltage = global_min[0]  # Replace with actual found voltage after first search
for t_volt in np.linspace(tuning_voltage - 0.5, tuning_voltage + 0.5, int((1) / 0.05)+1):
    for m_volt in np.linspace(0, 5, int((5) / 0.05)+1):
        plt.scatter(t_volt, m_volt, c='green', label='Precise Tuning Search (0.05V Steps)' if (t_volt, m_volt) == (tuning_voltage - 0.5, 0) else "", marker='x')

# Very Precise Search (Search 3)
matching_voltage = global_min[1]  # Replace with actual found voltage once determined
for t_volt in np.linspace(tuning_voltage - 0.1, tuning_voltage + 0.1, int((0.2) / 0.01)+1):
    for m_volt in np.linspace(matching_voltage - 0.1, matching_voltage + 0.1, int((0.2) / 0.01)+1):
        plt.scatter(t_volt, m_volt, c='blue', label='Very Precise Search (0.01V Steps)' if (t_volt, m_volt) == (tuning_voltage - 0.1, matching_voltage - 0.1) else "", marker='x')

# Labels, title, and legend for Search 1 only (to avoid duplicate labels)
plt.xlabel('Tuning Voltage (V)')
plt.ylabel('Matching Voltage (V)')
plt.title('Search Progression in Solution Space')
plt.legend()

# Show the plot
plt.show()
