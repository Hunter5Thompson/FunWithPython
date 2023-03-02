import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.io import wavfile
from scipy import signal

# Load input file
sample_rate, signal_orig = wavfile.read('schwebung_3.wav')

# High-pass filter
cutoff_freq = 500 # in Hz
nyquist_freq = 0.5 * sample_rate
cutoff_norm = cutoff_freq / nyquist_freq
b, a = signal.butter(4, cutoff_norm, btype='highpass')
signal_filtered = signal.filtfilt(b, a, signal_orig)

# Band-pass filter
freqs = [2000, 4000] # in Hz
cutoff_norm = [freq / nyquist_freq for freq in freqs]
b, a = signal.butter(4, cutoff_norm, btype='bandpass')
signal_filtered2 = signal.filtfilt(b, a, signal_orig)

# Plot the spectra of the original and filtered signals
fig, axs = plt.subplots(3, 1, figsize=(10, 6))
axs[0].plot(signal_orig)
axs[0].set_title('Original Signal')
axs[0].set_xlabel('Time (samples)')
axs[0].set_ylabel('Amplitude')
axs[1].plot(signal_filtered)
axs[1].set_title('High-Pass Filtered Signal')
axs[1].set_xlabel('Time (samples)')
axs[1].set_ylabel('Amplitude')
axs[2].plot(signal_filtered2)
axs[2].set_title('Band-Pass Filtered Signal')
axs[2].set_xlabel('Time (samples)')
axs[2].set_ylabel('Amplitude')
fig.tight_layout()
plt.show()
