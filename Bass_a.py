import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# Set parameters
duration = 10 # in seconds
bpm = 140
freq = 50 # in Hz

# Calculate number of samples
sample_rate = 44100
num_samples = sample_rate * duration

# Calculate time and frequency arrays
time = np.arange(num_samples) / sample_rate
beat_time = 60 / bpm
beat_samples = int(sample_rate * beat_time)
freq_array = np.zeros(num_samples)
freq_array[::beat_samples] = freq

# Generate sine wave
signal = np.sin(2 * np.pi * np.cumsum(freq_array) / sample_rate)

# Scale the signal to the maximum amplitude of a 16-bit PCM signal
signal *= 2**15 - 1
signal = signal.astype(np.int16)

# Write signal to file
wavfile.write('bass.wav', sample_rate, signal)

# Calculate FFT
fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/sample_rate)

# Plot the spectrum
plt.plot(freqs[:len(freqs)//2], np.abs(fft)[:len(freqs)//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
