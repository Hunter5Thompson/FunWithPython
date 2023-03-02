import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.fft import fft, fftfreq, fftshift

# Anzahl der Abtastwerte
n_samples = 1024

# Abtastfrequenz
sample_rate = 44100

# Generiere weißes Rauschen
signal = np.random.normal(0, 1, n_samples)

# Zeitachse in Sekunden
time = np.arange(n_samples) / sample_rate

# Plot des Signals im Zeitbereich
fig, ax = plt.subplots()
ax.plot(time, signal)
ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Amplitude')
plt.show()

# Fensterung des Signals
window = np.hanning(n_samples)
signal_windowed = signal * window

# Fourier-Transformation des Signals
signal_fft = fft(signal_windowed)
freq = fftfreq(n_samples, 1/sample_rate)
signal_fft_shifted = fftshift(signal_fft)

# Plot des Signals im Frequenzbereich
fig, ax = plt.subplots()
ax.plot(freq, np.abs(signal_fft_shifted))
ax.set_xlabel('Frequenz (Hz)')
ax.set_ylabel('Amplitude')
plt.show()
