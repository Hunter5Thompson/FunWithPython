import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Sampling frequency (samples per second)
samplerate = 44100

# Time points
t = np.linspace(0, 5, 5 * samplerate, False)

# Two signals
freq1 = 400
freq2 = 410
signal1 = np.sin(2 * np.pi * freq1 * t)
signal2 = np.sin(2 * np.pi * freq2 * t)

# Combined signal
signal = signal1 + signal2

# Save signal to wave file
wavfile.write("schwebung.wav", samplerate, signal)

# Plot signal
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
