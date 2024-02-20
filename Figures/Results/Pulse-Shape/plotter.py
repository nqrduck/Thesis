import matplotlib.pyplot as plt
import csv

plt.rcParams.update({'font.size': 16})

# Initialize lists to store the data
times = []
CH1_voltages = []
CH2_voltages = []

# Read data from CSV file
with open('CSV_202312421465.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header line
    next(csvreader)  # Skip the header line
    for row in csvreader:
        if row:  # Make sure the row is not empty
            times.append(float(row[0]))  # Time data in seconds
            CH1_voltages.append(float(row[1]))  # Channel 1 voltage data
            CH2_voltages.append(float(row[2]))  # Channel 2 voltage data

# Create a plot with two y-axes
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('CH1 Voltage (V)', color=color)
ax1.plot(times, CH1_voltages, label='CH1 Voltage (V)', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')
ax1.grid(True)

# Create a second y-axis for the second channel data
ax2 = ax1.twinx() 
color = 'tab:blue'
ax2.set_ylabel('CH2 Voltage (V)', color=color) 
ax2.plot(times, CH2_voltages, label='CH2 Voltage (V)', color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

fig.tight_layout()  # To ensure the layout fits well within the figure window
plt.title('Oscilloscope Data')
plt.show()
