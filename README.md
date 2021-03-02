# Music-reactive-LEDs-using-Raspberry-Pi
A bunch of LEDs programmed using Raspberry to light up according to music tones and beats. 

<img src="https://raw.githubusercontent.com/gaganng/Music-reactive-LEDs-using-Raspberry-Pi/main/Final%20Project%20Image.jpeg" width="330" height="250">

Follow the steps below to do the project yourself.
  1) Connect the circuit as shown below

<img src="https://raw.githubusercontent.com/gaganng/Music-reactive-LEDs-using-Raspberry-Pi/main/Raspberry_Circuit.jpg" width="400" height="250">

  2) Make you have the following Python dependencies - numpy, pyaudio, wave, math, Rpi, scipy
  3) Save the music file in WAVE format in the same folder as the main code.
  4) Connect your earphone/speaker to the raspberry pi.
  5) Now run the main code.
  
Here is a demo of the project

[![Demo Video](https://img.youtube.com/vi/VCkoSit8LK0/0.jpg)](https://youtu.be/VCkoSit8LK0)

The project is implemented using python. It essentially works by sensing the audio amplitude from wave file and lighting up LEDs proportionate to the audio level.
  
Electrical Components required - Raspberry Pi Board, Female to Male Connectors, Bread board, Speaker/Audio Output Device, 12 x LEDs, 12 x 330 Ohm Resistors
