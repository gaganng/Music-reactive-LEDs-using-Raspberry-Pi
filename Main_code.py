import numpy as np
import pyaudio
import wave
import math
import RPi.GPIO as GPIO
import scipy.io.wavfile

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

pins=[2,3,17,27,22,5,6,23,24,25,8,7]

def setup_pins():
    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)

def audio_levels(wave):
    frames=np.around((np.absolute(wave)/1000), decimals = 5)
    multiplier=np.around(frames.max(),2)/12

    audio_level = [np.around(multiplier*i,2) for i in range(1,12)]
    return audio_level

def calc_audio_level(frames,audio_level):
    frames=np.around((np.absolute(frames)/1000), decimals = 5)

    avg=np.around(np.max(frames),0)

    leds_on=0

    if avg<audio_level[0]:
        leds_on=1
    elif avg<audio_level[1]:
        leds_on=2
    elif avg<audio_level[2]:
        leds_on=3
    elif avg<audio_level[3]:
        leds_on=4
    elif avg<audio_level[4]:
        leds_on=5
    elif avg<audio_level[5]:
        leds_on=6
    elif avg<audio_level[6]:
        leds_on=7
    elif avg<audio_level[7]:
        leds_on=8
    elif avg<audio_level[8]:
        leds_on=9
    elif avg<audio_level[9]:
        leds_on=10
    elif avg<audio_level[10]:
        leds_on=11
    else:
        leds_on=12

    lights_on(leds_on)


def lights_on(leds_on):
    lights='000000000000'
    lights='1'*leds_on+lights[leds_on:]
    status={'1':GPIO.HIGH,'0':GPIO.LOW}
    for i,pin in list(zip(lights,pins)):
        print(leds_on)
        GPIO.output(pin,status[i])

if __name__ == '__main__':

    setup_pins()

    filename=input('Enter Music File name (eg. song_name.wav) - ')

    p = pyaudio.PyAudio()

    wf = wave.open(filename, 'rb')
    fs, wave = scipy.io.wavfile.read(filename)
    wave = wave[:, 0]

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    CHUNK = math.floor(wf.getframerate()/10)
    audio_level = audio_levels(wave)

    frames=wf.readframes(CHUNK)
    start=0;end=CHUNK;
    while 1:
        calc_audio_level(wave[start:end],audio_level)
        stream.write(frames)
        frames = wf.readframes(CHUNK)
        start=end;end=end+CHUNK;
        if frames == '':break

    stream.stop_stream()
    stream.close()

    p.terminate()
