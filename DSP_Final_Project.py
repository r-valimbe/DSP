import pyaudio, struct
import tkinter as tk
import wave
import time
root = tk.Tk()
def start(scale, entry, label, v):
    '''
    In here we will first take the number of seconds they want to record from the scale and set that to the Duration

    Then we check which voice they want and call that specific voice set up and have the duration set to be that

    The label is a visual indicator and can just show how long the time is left and when its complete

    Then take the file name from entry bxo and save it as a wav file with that file name

    '''

    if len(entry.get()) == 0: #can try and get rid of invalid characters when saving file too but that won't be necessary
        label['text'] = 'File name cannot be empty'
    else:
        duration = scale.get()
        output_wavfile = entry.get()

        label['text'] = 'You will be recording for ' + str(duration) + ' seconds'

        if v.get() == 1:
        # voice1(output_wavfile, duration)
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

        #after whatever operation we do
        label['text'] = 'Successfully saved ' + output_wavfile + '.wav file'


    pass

def voice1(output_wavfile, duration):
    '''
    Do the pyaudio stuff, set the duration as the duration variable passed in

    '''
    CHANNELS = 1
    RATE = 8000
    WIDTH = 2
    DURATION = duration
    N_FRAMES = DURATION * RATE
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
    pass

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

radio1 = tk.Radiobutton(root, text="First Voice", variable = v, value = 1)
radio1.place(x=0, y=200)
radio2= tk.Radiobutton(root, text="Second Voice", variable = v, value = 2)
radio2.place(x=0, y=220)
radio3= tk.Radiobutton(root, text="Third Voice", variable = v, value = 3)
radio3.place(x=0, y=240)
radio4= tk.Radiobutton(root, text="Fourth Voice", variable = v, value = 4)
radio4.place(x=0, y=260)

file_name_label = tk.Label(root, text="What file name would you like to save this wav file as?")
file_name_label.place(x=0, y =300)
file_name_entry = tk.Entry(root)
file_name_entry.place(x=300, y=300)

start_button = tk.Button(root, text="Start Recording", command = lambda:start(record_length_scale, file_name_entry,indicator_label, v))
start_button.place(x=0, y = 330)

indicator_label = tk.Label(root, text = "")
indicator_label.place(x=0, y = 360)
root.mainloop()