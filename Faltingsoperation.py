import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Definition der Signale A und B
A = np.array([1, 2, 3, 4, 5])
B = np.array([0, 0, 1])

# Faltung der beiden Signale
C = np.convolve(A, B)

# Visualisierung des Ergebnisses
plt.subplot(1, 3, 1)
plt.stem(A)
plt.title('Signal A')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(1, 3, 2)
plt.stem(B)
plt.title('Signal B')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(1, 3, 3)
plt.stem(C)
plt.title('Faltung von A und B')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
