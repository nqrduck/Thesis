import matplotlib.pyplot as plt
import csv

plt.rcParams.update({'font.size': 16})

# Initialize lists to store the data
frequencies = []
S11_dB = []
S11_magnitude = []

# Read data from CSV file
# 83 to 84 Mhz in 0.1 Mhz stepslots()
plt.ylabel('S11(dB)')
plt.xlabel('Frequency (MHz)')
plt.title('S11 of the mechanically tuned probe coil')
plt.grid(True)

# Only plot magnitude

files = [
    '83.csv', '83,1.csv', '83,2.csv', '83,3.csv', '83,4.csv', '83,5.csv', '83,6.csv', '83,7.csv', '83,8.csv', '83,9.csv',
    '84.csv', '84,1.csv', '84,2.csv', '84,3.csv', '84,4.csv', '84,5.csv', '84,6.csv', '84,7.csv', '84,8.csv', '84,9.csv',
    '85.csv', '85,1.csv', '85,2.csv', '85,3.csv', '85,4.csv', '85,5.csv', '85,6.csv', '85,7.csv', '85,8.csv', '85,9.csv',
    '86.csv', '86,1.csv', '86,2.csv', '86,3.csv', '86,4.csv', '86,5.csv', '86,6.csv', '86,7.csv', '86,8.csv', '86,9.csv',
    '87.csv'
]

S11_data = {}
for file in files:
    frequencies = []
    S11_dB = []
    with open(file, 'r') as csvfile:
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

        label = file.replace('.csv', '').replace(',', '.') + ' MHz'
        plt.plot(frequencies, S11_dB, label=label)
        # Make an x exactly at the desired frequency of the according curve ( so the name of the file without the csv extension)
        # First get the S11 value at the desired frequency
        frequency = float(file.replace('.csv', '').replace(',', '.'))

        # Get the closest index to the desired frequency
        index = min(range(len(frequencies)), key=lambda i: abs(frequencies[i] - frequency))

        # Get the S11 value at the index
        S11_data[frequency] = S11_dB[index]

# Plot S11 dB and S11 Phase on the same figure with two different y-axes
plt.legend()
plt.show()

# Plot the S11_data
plt.ylabel('S11(dB)')
plt.xlabel('Frequency (MHz)')
plt.title('S11 of the electrically tuned probe coil at the desired frequencies')
plt.grid(True)
plt.plot(S11_data.keys(), S11_data.values(), label='S11', marker='X', linestyle='None', color='r')
# Make y axis go from zero to the maximum value of the S11_data
plt.ylim(min(S11_data.values()) - 10,0)
plt.show()
