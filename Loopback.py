import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

# Öffnen Sie einen Audio-Stream zum Lesen vom Eingabegerät
stream_in = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# Öffnen Sie einen Audio-Stream zum Schreiben auf das Ausgabegerät
stream_out = p.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     output=True,
                     frames_per_buffer=CHUNK)

# Lesen Sie Audio-Daten vom Eingabegerät und schreiben Sie sie auf das Ausgabegerät
while True:
    data = stream_in.read(CHUNK)
    stream_out.write(data)

# Schließen Sie die Audio-Streams und PyAudio
stream_in.stop_stream()
stream_out.stop_stream()
stream_in.close()
stream_out.close()
p.terminate()
