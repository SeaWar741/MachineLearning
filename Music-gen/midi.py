import midi
import numpy as np

lowerBound = 24
upperBound = 102
span = upperBound-lowerBound

def midi_to_matrix(midifile, squash = True, span = span):
    pattern = midi.read_midifile(midifile)

    timeleft = [track[0].trick for track in pattern]

    posns = [0 for track in pattern]

    matrix = []
    time = 0

    state = [[0,0] for x in range(span)]
    matrix.append(state)
    condition = True
    while condition:
        if time % (pattern.resolution / 4) == (pattern.resolution / 8):
            oldstate = state
            state =[[oldstate[x]]]