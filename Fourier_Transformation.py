import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.fft import fft

# Sampling-Frequenz (Hz) und Dauer des Signals (s)
fs = 44100
duration = 1

# Anzahl der Samples im Signal
n_samples = int(fs * duration)

# Erzeugung des Rauschens
noise = np.random.randn(n_samples)

# Berechnung der Fourier-Transformation
freqs = np.linspace(0, fs, n_samples)
spectrum = fft(noise)

# Visualisierung des Signals im Zeitbereich
plt.subplot(2, 1, 1)
plt.plot(np.arange(n_samples) / fs, noise)
plt.xlabel('Zeit (s)')
plt.ylabel('Amplitude')
plt.title('Weißes Rauschen')

# Visualisierung des Signals im Frequenzbereich
plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(spectrum))
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequenzspektrum des weißen Rauschens')

plt.tight_layout()
plt.show()
