import pyaudio, struct
import tkinter as tk
import wave
import time
root = tk.Tk()
from math import pi, cos, sin
import numpy as np


def start(scale, entry, label, v):
    '''
    In here we will first take the number of seconds they want to record from the scale and set that to the Duration

    Then we check which voice they want and call that specific voice set up and have the duration set to be that

    The label is a visual indicator and can just show how long the time is left and when its complete

    Then take the file name from entry bxo and save it as a wav file with that file name

    '''

    #The following variables are common across all the 5 different voices selected and so, will only be changed there for space considerations

    CHANNELS = 1
    RATE = 8000
    DURATION = 0
    WIDTH = 2
    BLOCKLEN = 1024

    if len(entry.get()) == 0: #can try and get rid of invalid characters when saving file too but that won't be necessary
        label['text'] = 'File name cannot be empty!'
    else:
        DURATION = scale.get()
        output_wavfile = entry.get()

        label['text'] = 'You will be recording for ' + str(DURATION) + ' seconds'

        if v.get() == 1:
            voice1(output_wavfile, DURATION, BLOCKLEN, RATE, WIDTH, CHANNELS)
            print("1")
        elif v.get()  == 2:
        # voice2(output_wavfile, duration)
            print("2")
        elif v.get()  == 3:
        # voice3(output_wavfile, duration)
            print("3")
        elif v.get()  == 4:
        #voice4(output_wavfile, duration)
            print("4")
        else:
            print("5")

    # after whatever operation we do
        label['text'] = 'Successfully saved ' + output_wavfile + '.wav file'

    pass


# Rohan working on voice1 to be high pitch - not quite done yet
def voice1(output_wavfile, DURATION, BLOCKLEN, RATE, WIDTH, CHANNELS):

    N_BLOCKS = int(RATE / BLOCKLEN * DURATION)
    output_wf = wave.open(output_wavfile + ".wav", 'w')  # wave file
    output_wf.setframerate(RATE)
    output_wf.setsampwidth(WIDTH)
    output_wf.setnchannels(CHANNELS)

    p = pyaudio.PyAudio()

    # Open audio stream
    stream = p.open(
        format=p.get_format_from_width(WIDTH),
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True)

    # This is the actual thing running
    i = 0
    theta = 0

    for i in range(0, N_BLOCKS):
        input_block = stream.read(BLOCKLEN)
        signal_block = struct.unpack('h' * BLOCKLEN, input_block)
        output_block = []
        for j in range(0, BLOCKLEN):
            curr_val = int(signal_block[j])

            #clipping
            if curr_val > 32767:
                curr_val = 32767
            elif curr_val < -32768:
                curr_val = -32768

            output_block.append(curr_val)

        output_string = struct.pack('h' * BLOCKLEN, *output_block)

        stream.write(output_string)
        output_wf.writeframes(output_string)

    stream.close()
    output_wf.close()


def voice2(output_wavfile, duration):
    pass

def voice3(output_wavfile, duration):
    pass

def voice4(output_wavfile, duration):
    pass


v= tk.IntVar()
v.set(1)
root.title("DSP Lab Final Project")
root.geometry('500x500')
welcome_label = tk.Label(root, text="DSP Lab Final Project", font = 50)
welcome_label.place(x=0, y=0)

name_label = tk.Label(root, text="Created By: Alex Him, Jonathan Lin, Rohan Valimbe")
name_label.place(x=0, y=50)

record_length_label = tk.Label(root, text="How many seconds do you want to record for?")
record_length_label.place(x=0, y=100)
record_length_scale = tk.Scale(root, from_ = 1, to_ = 20, orient = tk.HORIZONTAL)
record_length_scale.place(x=0, y = 120)

radio1 = tk.Radiobutton(root, text="High Pitch", variable = v, value = 1)
radio1.place(x=0, y=200)
radio2 = tk.Radiobutton(root, text="Second Voice", variable = v, value = 2)
radio2.place(x=0, y=220)
radio3 = tk.Radiobutton(root, text="Third Voice", variable = v, value = 3)
radio3.place(x=0, y=240)
radio4 = tk.Radiobutton(root, text="Fourth Voice", variable = v, value = 4)
radio4.place(x=0, y=260)
radio5 = tk.Radiobutton(root, text="Manual", variable = v, value = 5)
radio5.place(x=0, y=280)

frequency_label = tk.Label(root, text="Frequency")
frequency_label.place(x= 200, y= 180)
frequency = tk.Scale(root, from_ = 0, to_ = 600, orient = tk.VERTICAL)
frequency.place(x=200, y = 200)

amplitude_label = tk.Label(root, text="Amplitude")
amplitude_label.place(x= 270, y= 180)
amplitude = tk.Scale(root, from_ = 0, to_ = 100, orient = tk.VERTICAL)
amplitude.place(x=270, y = 200)

file_name_label = tk.Label(root, text="What file name would you like to save this wav file as?")
file_name_label.place(x=0, y =320)
file_name_entry = tk.Entry(root)
file_name_entry.place(x=300, y=320)

start_button = tk.Button(root, text="Start Recording", command = lambda:start(record_length_scale, file_name_entry,indicator_label, v))
start_button.place(x=205, y = 340)

indicator_label = tk.Label(root, text = "")
indicator_label.place(x=0, y = 360)
root.mainloop()

