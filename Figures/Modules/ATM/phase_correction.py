import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Function to generate a triangle wave over the frequency range with 4 cycles
def generate_triangle_wave(frequency_data, cycles=4):
    # Generate phase data in degrees as a triangle wave
    phase_data = np.linspace(0, cycles * 2 * np.pi, frequency_data.size)
    triangle_phase = (np.arcsin(np.sin(phase_data)) / np.pi + 0.5) * 180

    # Adding small noise to the phase
    noise = np.random.normal(0, 5, size=triangle_phase.shape)  # small noise level
    triangle_phase_noisy = triangle_phase + noise

    return np.abs(triangle_phase_noisy)  # Returns absolute phase mimicking AD8302 behavior


# Generate frequency and phase data using previously defined function
frequency_data = np.linspace(80, 100, 1000)  # Frequency in MHz
phase_data = generate_triangle_wave(frequency_data, cycles=4)

def phase_correction_visual(frequency_data: np.array, phase_data: np.array) -> np.array:
    # Apply a moving average filter to the phase data
    WINDOW_SIZE = 5
    phase_data_filtered = np.convolve(phase_data, np.ones(WINDOW_SIZE)/WINDOW_SIZE, mode='same')

    # Fix transient response
    phase_data_filtered[:WINDOW_SIZE//2] = phase_data[:WINDOW_SIZE//2]
    phase_data_filtered[-WINDOW_SIZE//2:] = phase_data[-WINDOW_SIZE//2:]

    # Visualize the filtered phase data
    plt.figure(figsize=(14, 14))  # Adjusted the figure size for a 2x2 grid
    plt.subplot(2, 2, 1)
    plt.plot(frequency_data, phase_data, label="Original Phase Data")
    plt.plot(frequency_data, phase_data_filtered, label="Filtered Phase Data", color='orange')
    plt.title("Apply Moving Average Filter")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Phase (degrees)")
    plt.legend()

    # Find peaks and valleys
    distance = len(phase_data_filtered) / 10
    peaks, _ = find_peaks(phase_data_filtered, distance=distance, height=100)
    valleys, _ = find_peaks(
            180 - phase_data_filtered, distance=distance, height=100
        )

    # Determine if the first point is a peak or a valley
    if phase_data_filtered[0] > phase_data_filtered[1]:
        peaks = np.insert(peaks, 0, 0)
    else:
        valleys = np.insert(valleys, 0, 0)

    # Determine if the last point is a peak or a valley
    if phase_data_filtered[-1] > phase_data_filtered[-2]:
        peaks = np.append(peaks, len(phase_data_filtered) - 1)
    else:
        valleys = np.append(valleys, len(phase_data_filtered) - 1)

    # Visualize peaks and valleys
    plt.subplot(2, 2, 2)
    plt.plot(frequency_data, phase_data_filtered, label="Filtered Phase Data", color='orange')
    plt.plot(frequency_data[peaks], phase_data_filtered[peaks], "x", label="Peaks", color='red')
    plt.plot(frequency_data[valleys], phase_data_filtered[valleys], "x", label="Valleys", color='green')
    plt.title("Peaks and Valleys")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Phase (degrees)")
    plt.legend()

    # Combine peaks and valleys and sort
    peaks_valleys = np.sort(np.concatenate((peaks, valleys)))

    # Calculate the phase slope
    phase_slope = np.diff(phase_data_filtered[peaks_valleys])
    phase_sign = np.sign(phase_slope) * -1

    # Visualize phase slope
    plt.subplot(2, 2, 3)
    phase_slope = np.diff(phase_data_filtered[peaks_valleys])
    phase_sign = np.sign(phase_slope) * -1
    # Use green for positive slopes and red for negative slopes
    for i in range(len(peaks_valleys) - 1):
        color = 'green' if phase_slope[i] >= 0 else 'red'
        plt.plot(frequency_data[peaks_valleys[i]:peaks_valleys[i+1]],
                 phase_data_filtered[peaks_valleys[i]:peaks_valleys[i+1]],
                 color=color)
    plt.title("Phase Slope")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Phase (degrees)")

    # Apply the phase sign correction
    phase_data_corrected = np.zeros(len(phase_data))
    for i in range(len(peaks_valleys) - 1):
        start, end = peaks_valleys[i], peaks_valleys[i+1]
        phase_data_corrected[start:end] = phase_data_filtered[start:end] * phase_sign[i]

    # Final visualization before return
    plt.subplot(2, 2, 4)
    plt.plot(frequency_data, phase_data_corrected, label="Corrected Phase Data", color='purple')
    plt.title("Final Phase Correction")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Phase (degrees)")
    plt.legend()

    return phase_data_corrected

# Run the phase correction with visualization
frequency_data = np.linspace(80, 100, 1000)  # Frequency in MHz
phase_data = generate_triangle_wave(frequency_data, cycles=4)
corrected_phase_data = phase_correction_visual(frequency_data, phase_data)

plt.tight_layout(pad=2.0)
plt.show()
