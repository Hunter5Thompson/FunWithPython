import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# Sampling rate (samples per second)
sample_rate = 44100

# Duration of the signal (seconds)
duration = 5

# Frequency of the sinus signal (Hz)
freq = 440

# Time axis
time = np.linspace(0, duration, sample_rate*duration)

# Sinus signal
signal = np.sin(2*np.pi*freq*time)

# Echo parameters
delay = 0.5 # in seconds
attenuation = 0.5

# Echo signal
echo = np.zeros(len(signal))
echo[int(delay*sample_rate):] = attenuation * signal[:len(signal)-int(delay*sample_rate)]

# Add the original signal and the echo
signal_with_echo = signal + echo

# Normalize the signal
signal_with_echo /= np.max(np.abs(signal_with_echo))

# Save the signal as a Wav file
wavfile.write('sinus_with_echo.wav', sample_rate, signal_with_echo)

# Plot the spectrum of the signal with echo
fft = np.fft.fft(signal_with_echo)
freqs = np.fft.fftfreq(len(signal_with_echo), 1/sample_rate)
plt.plot(freqs, np.abs(fft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
