import os
import sys
textf = 'Note_off_c'
textr = ''
sourcepath = os.listdir(r'D:\Ubuntu\MachineLearning\MusicGenerator\MIDI_Data')
for file in sourcepath:
    filename = os.fsdecode(file)
    print("conversion para el archivo: "+filename)
    filedata = filename.read()
    freq = 0
    freq = filedata.count(textf)
    print()