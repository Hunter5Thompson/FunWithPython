import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Einstellungen
delay = 0.1  # Verzögerung der ersten Wiederholung (in Sekunden)
length = 0.5  # Länge des gesamten Halls (in Sekunden)
repeats = 10  # Anzahl der Wiederholungen in der Gesamtlänge

# Signal einlesen
fs, signal_in = wavfile.read('input.wav')

# Hall erzeugen
delay_samples = int(fs * delay)
length_samples = int(fs * length)
hall = np.zeros(len(signal_in) + length_samples * repeats)
hall[:len(signal_in)] = signal_in
for i in range(repeats):
    start = delay_samples + i * length_samples
    end = start + len(signal_in)
    hall[start:end] += signal_in * (1 - i/repeats)

# Hall abspeichern
wavfile.write('output.wav', fs, hall.astype(np.int16))

# Signal und Hall visualisieren
t = np.arange(len(signal_in))/fs
plt.plot(t, signal_in, label='Original Signal')
plt.plot(t, hall[:len(signal_in)], label='Signal mit Hall')
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
