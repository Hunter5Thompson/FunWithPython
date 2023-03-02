import numpy as np
import scipy.io.wavfile as wav
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Frequenzen der Töne in der D-Dur Tonleiter
freqs = [293.665, 329.628, 369.994, 293.665, 349.228, 392.00, 440.00]

# Länge des Signals in Sekunden
length = 5

# Abtastrate in Hz
sample_rate = 44100

# Generiere das Signal
t = np.linspace(0, length, int(length * sample_rate), endpoint=False)
signal = np.zeros_like(t)
for freq in freqs:
    signal += np.sin(2 * np.pi * freq * t)

# Skaliere das Signal auf den Wertebereich von 16-Bit Wav-Dateien
signal *= 32767 / np.max(np.abs(signal))

# Konvertiere das Signal in eine 16-Bit Wav-Datei und speichere sie
signal = np.asarray(signal, dtype=np.int16)
wav.write('D_major_scale.wav', sample_rate, signal)

# Plot des Signals im Frequenzbereich
fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/sample_rate)
plt.plot(freqs, np.abs(fft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
