import numpy as np
import pyaudio
import wave
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Konstanten definieren
sampling_rate = 44100
duration = 5  # in Sekunden
frequency = 440  # in Hz
amplitude = 0.5
delay = 0.5  # in Sekunden

# Sinus-Signal erzeugen
time = np.linspace(0, duration, int(duration * sampling_rate), False)
signal = amplitude * np.sin(2 * np.pi * frequency * time)

# Echo erzeugen
delay_samples = int(delay * sampling_rate)
echo_signal = np.zeros_like(signal)
echo_signal[delay_samples:] = signal[:-delay_samples]

# Gesamtsignal erzeugen
result_signal = signal + echo_signal

# PyAudio-Stream erzeugen
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sampling_rate,
                output=True)

# Gesamtsignal abspielen
stream.write(result_signal.astype(np.float32).tobytes())

# PyAudio-Stream und PyAudio-Objekt schließen
stream.stop_stream()
stream.close()
p.terminate()

# Gesamtsignal als WAV-Datei speichern
wave_file = wave.open("echo.wav", "wb")
wave_file.setnchannels(1)
wave_file.setsampwidth(4)
wave_file.setframerate(sampling_rate)
wave_file.writeframes(result_signal.astype(np.float32).tobytes())
wave_file.close()

# Signal visualisieren
plt.plot(result_signal)
plt.show()
