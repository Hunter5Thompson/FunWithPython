import numpy as np
from scipy.io import wavfile
from scipy import signal

# Define some parameters for the waves
sampling_freq = 44100
duration = 5
freq1 = 440
freq2 = 880

# Generate the signals
t = np.linspace(0, duration, int(duration * sampling_freq), endpoint=False)
square_wave = np.sign(np.sin(2 * np.pi * freq1 * t))
sawtooth_wave = signal.sawtooth(2 * np.pi * freq2 * t)
combined_signal = square_wave + sawtooth_wave

# Scale the signal to fit in the -1 to 1 range
combined_signal *= 0.5 / np.max(np.abs(combined_signal))

# Save the combined signal to a WAV file
wavfile.write("combined_signal.wav", sampling_freq, np.int16(combined_signal * 32767))
