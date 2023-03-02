import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Sampling-Frequenz in Hz
fs = 44100

# Länge des Signals in Sekunden
duration = 5

# Anzahl der Samples
n_samples = fs * duration

# Erzeugung des Rauschens
white_noise = np.random.normal(0, 1, n_samples)

# Skalierung des Rauschens auf den Bereich [-1, 1]
scaled_noise = white_noise / np.max(np.abs(white_noise))

# Schreibzugriff auf Wave-Datei
wavfile.write('white_noise.wav', fs, scaled_noise)

# Visualisierung des Signals
plt.plot(scaled_noise)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('White Noise Signal')
plt.show()
