import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# Abtastfrequenz
fs = 44100

# Zeitvektor
t = np.arange(0, 1, 1/fs)

# Trägersignal (Sinuswelle)
f_c = 1000  # Trägerfrequenz
A_c = 1  # Trägeramplitude
c = A_c * np.sin(2 * np.pi * f_c * t)

# Nutzsignal (Rechteckwelle)
f_m = 200  # Nutzfrequenz
A_m = 0.5  # Nutzamplitude
m = A_m * np.sign(np.sin(2 * np.pi * f_m * t))

# Amplitudenmodulation
modulation_index = 0.5
s = (1 + modulation_index * m) * c

# Wave-Datei schreiben
s = np.int16(s / np.max(np.abs(s)) * 32767)
wavfile.write("am_mod.wav", fs, s)

# Darstellung
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))
ax1.plot(t, c)
ax1.set_ylabel("Amplitude")
ax1.set_title("Trägersignal")
ax2.plot(t, m)
ax2.set_ylabel("Amplitude")
ax2.set_title("Nutzsignal")
ax3.plot(t, s)
ax3.set_ylabel("Amplitude")
ax3.set_title("AM-Signal")
ax3.set_xlabel("Zeit [s]")
plt.tight_layout()
plt.show()
