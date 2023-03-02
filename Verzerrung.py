import numpy as np
import scipy.io.wavfile as wav

# Lade ein beliebiges Audiosignal
rate, data = wav.read('input.wav')

# Definiere den Schwellenwert für das Clipping
threshold = 0.8 * np.max(np.abs(data))

# Wende das Clipping an
clipped_data = np.copy(data)
clipped_data[clipped_data > threshold] = threshold
clipped_data[clipped_data < -threshold] = -threshold

# Normalisiere das Signal auf volle Amplitude
#clipped_data *= 1.0 / np.max(np.abs(clipped_data))
clipped_data = np.array(data * 10000, dtype=np.float64)
clipped_data = np.array(clipped_data, dtype=np.int16)

# Speichere das manipulierte Signal als Wav-Datei ab
wav.write('outputVerz.wav', rate, clipped_data)
