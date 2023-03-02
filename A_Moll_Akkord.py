import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Define the parameters
sample_rate = 44100
duration = 3.0
notes = [261.63, 311.13, 349.23, 392.00, 466.16, 523.25] # Frequencies of the notes in a A minor chord

# Create the waveform
time_array = np.linspace(0, duration, int(sample_rate * duration), False)
signal = np.sin(2 * np.pi * notes[0] * time_array) + \
         np.sin(2 * np.pi * notes[2] * time_array) + \
         np.sin(2 * np.pi * notes[4] * time_array)

# Scale the signal to avoid clipping
signal /= np.max(np.abs(signal))

# Save the waveform to a Wav file
wavfile.write('A_minor_chord.wav', sample_rate, np.int16(signal * 32767))

# Convert signal to frequency domain using FFT
fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/sample_rate)

# Plot the spectrum
plt.plot(freqs[:len(freqs)//2], np.abs(fft)[:len(freqs)//2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()
