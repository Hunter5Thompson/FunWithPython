import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Eigenschaften der Schwingungen
amp1, freq1, phase1 = 1, 5, 0
amp2, freq2, phase2 = 2, 12, np.pi/2
amp3, freq3, phase3 = 0.5, 23, np.pi

# Zeitintervall
t = np.linspace(0, 2*np.pi, 1000)

# Schwingungen erstellen
s1 = amp1 * np.cos(freq1*t + phase1)
s2 = amp2 * np.sin(freq2*t + phase2)
s3 = amp3 * np.sin(freq3*t + phase3)

# Schwingungen plotten
plt.plot(t, s1)
plt.title('Schwingung s1')
plt.show()

plt.plot(t, s2)
plt.title('Schwingung s2')
plt.show()

plt.plot(t, s3)
plt.title('Schwingung s3')
plt.show()

# Superposition aller Schwingungen
s4 = s1 + s2 + s3

# Superposition plotten
plt.plot(t, s4)
plt.title('Superposition aller Schwingungen')
plt.show()
