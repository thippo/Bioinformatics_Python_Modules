import wave, pyaudio
import numpy

class WaveSteam():

    def __init__(self, CHUNK=1, FORMAT=pyaudio.paFloat32, RATE=8000, CHANNELS=1):
        self.CHUNK = CHUNK
        self.CHANNELS = CHANNELS
        self.FORMAT = FORMAT
        self.RATE = RATE
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    def realtime(self):
        audio_data = self.stream.read(self.CHUNK, exception_on_overflow=False)
        return numpy.fromstring(audio_data, 'Float32')

    def record(self, RECORD_SECONDS=5, file='record.wav'):
        buffer = []
        i=1
        print ('Recording...')
        while 1:
            audio_data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            buffer.append(audio_data)
            i+=1
            if i == RECORD_SECONDS*8000+1:
                break
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        wf = wave.open(file, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(buffer))
        wf.close()
        print ('Record Done')

if __name__ == '__main__':
    a=WaveSteam()
    a.record()
    #while 1:
    #    print(a.realtime())
