import matplotlib.pyplot as plt
import csv

plt.rcParams.update({'font.size': 16})

# Initialize lists to store the data
frequencies = []
S11_dB = []
S11_magnitude = []

# Read data from CSV file
with open('s11-ele-83,56.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader)  # Skip the header line
    for row in csvreader:
        if row and not row[0].startswith('#'):  # Skip lines starting with # and empty rows
            try:
                frequencies.append(float(row[0]) * 1e-6)  # Convert frequency to MHz
                S11_dB.append(float(row[1]))  # S11 dB
                S11_magnitude.append(float(row[2]))  # S11 Magnitude (Phase)
            except ValueError as e:
                print(f"Error reading line: {row}. Error: {e}")
                continue  # Skip lines where conversion to float fails

# Plot S11 dB and S11 Phase on the same figure with two different y-axes
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Frequency (MHz)')
ax1.set_ylabel('S11(dB)', color=color)
ax1.plot(frequencies, S11_dB, label='S11(dB)', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')
ax1.grid(True)

# Instantiate a second y-axis that shares the same x-axis
ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('S11 (Phase)', color=color)  # We already handled the x-label with ax1
ax2.plot(frequencies, S11_magnitude, label='S11 Magnitude (Phase)', color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

fig.tight_layout()  # To ensure the subplots do not overlap
plt.title('S11 of the electrically tuned probe coil')
plt.show()
