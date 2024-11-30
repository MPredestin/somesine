import numpy as np
import matplotlib.pyplot as plt


def plot_sine_wave(frequency=1, amplitude=1, duration=2, sampling_rate=1000):

    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)  # Time array
    y = amplitude * np.sin(2 * np.pi * frequency * t)  # Sine wave formula

    plt.figure(figsize=(10, 4))
    plt.plot(t, y, label=f'{frequency} Hz Sine Wave')
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()


# Example usage:
if __name__ == "__main__":
    plot_sine_wave(frequency=2, amplitude=1, duration=2, sampling_rate=1000)
