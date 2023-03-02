import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')




# Sägezahn-Signal
def sawtooth_wave(a, T, k, duration, fs):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    return (2*a/T) * (t - k*T/2 - np.floor((t - k*T/2)/T)*T)

# Rechteck-Signal
def square_wave(a, T, duty_cycle, duration, fs):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    return np.where((t - T/2) % T < T*duty_cycle, a, -a)

# Dreieck-Signal
def triangle_wave(a, T, k, duration, fs):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    return (4*a/T) * np.abs((t - k*T/2) - T/2) - a

# Signal-Parameter
a = 1.0
T = 1.0
duration = 5.0
fs = 44100

# Generiere Signale
sawtooth = sawtooth_wave(a, T, 1, duration, fs)
square = square_wave(a, T, 0.5, duration, fs)
triangle = triangle_wave(a, T, 1, duration, fs)

# Plotte Signale
fig, ax = plt.subplots(3, 1, figsize=(6, 8))

ax[0].plot(sawtooth)
ax[0].set_title('Sägezahn-Signal')

ax[1].plot(square)
ax[1].set_title('Rechteck-Signal')

ax[2].plot(triangle)
ax[2].set_title('Dreieck-Signal')

plt.tight_layout()
plt.show()

# Erzeuge WAV-Dateien
wavfile.write('sawtooth.wav', fs, sawtooth)
wavfile.write('square.wav', fs, square)
wavfile.write('triangle.wav', fs, triangle)