import pyaudio

# Define audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open audio stream
try:
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
except OSError as e:
    print(f"Error opening audio stream: {e}")
    exit(1)

# Read audio data from stream
try:
    while True:
        data = stream.read(CHUNK)
        # Do something with audio data
except KeyboardInterrupt:
    # Stop audio stream when user interrupts program
    stream.stop_stream()
    stream.close()
    audio.terminate()
    exit(0)