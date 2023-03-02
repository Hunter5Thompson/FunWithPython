import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Frequenzen für die Noten der natürlichen Moll-Tonleiter
freqs = [220, 246.94, 261.63, 293.66, 329.63, 349.23, 392]

# Länge einer Note in Sekunden
note_len = 1

# Anzahl der Samples pro Sekunde
sample_rate = 44100

# Erstelle ein leeres Array für das Signal
signal = np.array([])

# Erzeuge für jede Note ein Sinussignal mit der entsprechenden Frequenz und füge es zum Signal hinzu
for freq in freqs:
    t = np.linspace(0, note_len, int(note_len * sample_rate), endpoint=False)
    note = np.sin(2*np.pi*freq*t)
    signal = np.concatenate([signal, note])

# Skaliere das Signal auf den Wertebereich -32768 bis 32767
scaled = np.int16(signal * 32767)

# Schreibe das Signal in eine Wav-Datei
wavfile.write('moll_tonleiter.wav', sample_rate, scaled)



# Lade das Signal aus der Wav-Datei
sample_rate, signal = wavfile.read('moll_tonleiter.wav')

# Berechne das Amplitudenspektrum des Signals
fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/sample_rate)
amplitudes = np.abs(fft)

# Plotte das Amplitudenspektrum
plt.plot(freqs, amplitudes)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
