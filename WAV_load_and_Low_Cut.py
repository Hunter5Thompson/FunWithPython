import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.io import wavfile
from scipy import signal

# Load input file
sample_rate, signal_orig = wavfile.read('schwebung_3.wav')

# Create high-pass filter
cutoff_freq = 500 # in Hz
nyquist_freq = 0.5 * sample_rate
cutoff_norm = cutoff_freq / nyquist_freq
b, a = signal.butter(4, cutoff_norm, btype='highpass')

# Define window size
window_size = len(signal_orig) // 4

# Filter the signal
signal_filtered = signal.filtfilt(b, a, signal_orig, padtype='odd', padlen=3*(window_size-1))

# Plot the spectrum of the filtered signal
fft = np.fft.fft(signal_filtered)
freqs = np.fft.fftfreq(len(signal_filtered), 1/sample_rate)
plt.plot(freqs, np.abs(fft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
