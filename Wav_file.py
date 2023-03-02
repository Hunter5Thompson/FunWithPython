import numpy as np
from scipy.io import wavfile
import argparse

# Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--duration', type=float, default=5.0, help='Dauer des Signals in Sekunden')
parser.add_argument('--frequency', type=float, default=440.0, help='Frequenz in Hertz')
args = parser.parse_args()

# Sampling rate
sampling_rate = 44100

# Time points
time = np.linspace(0, args.duration, int(sampling_rate * args.duration), endpoint=False)

# Sinus signal
signal = np.sin(2 * np.pi * args.frequency * time)

# Convert to int16 for 16-bit resolution
signal = np.int16(signal * 32767)

# Save to WAV file
wavfile.write('sinus_signal.wav', sampling_rate, signal)