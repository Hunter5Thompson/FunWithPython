import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Initialisiere Parameter mit Standardwerten
delay = 0.1
duration = 0.5
repetitions = 10

# Benutzerabfrage für neue Parameterwerte
print("Aktuelle Parameter:")
print(f"Verzögerung der ersten Wiederholung: {delay:.3f}s")
print(f"Länge des gesamten Halls: {duration:.3f}s")
print(f"Anzahl der Wiederholungen in der Gesamtlänge: {repetitions}")
print("")

while True:
    user_input = input("Neue Parameterwerte eingeben (in der Form 'delay duration repetitions'): ")
    try:
        new_delay, new_duration, new_repetitions = map(float, user_input.split())
        if new_delay >= 0 and new_duration >= 0 and new_repetitions >= 0:
            delay = new_delay
            duration = new_duration
            repetitions = int(new_repetitions)
            break
        else:
            print("Fehler: Alle Parameterwerte müssen positiv sein!")
    except:
        print("Fehler: Ungültiges Eingabeformat!")

# Signal einlesen
fs, signal_in = wavfile.read('input.wav')

# Hall erzeugen
delay_samples = int(fs * delay)
length_samples = int(fs * duration)
hall = np.zeros(len(signal_in) + length_samples * repetitions)
hall[:len(signal_in)] = signal_in
for i in range(repetitions):
    start = delay_samples + i * length_samples
    end = start + len(signal_in)
    hall[start:end] += signal_in * (1 - i/repetitions)

# Hall abspeichern
wavfile.write('output.wav', fs, hall.astype(np.int16))

# Signal und Hall visualisieren
t = np.arange(len(signal_in))/fs
plt.plot(t, signal_in, label='Original Signal')
plt.plot(t, hall[:len(signal_in)], label='Signal mit Hall')
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
