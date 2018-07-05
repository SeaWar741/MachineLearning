import numpy as np
import pandas as pd
import tensorflow as tf 
from tqdm import tqdm
import midi_manipulation

#Paso 1 Parametros
lowest_note = midi_manipulation.lowerBound
highest_note = midi_manipulation.upperBound
note_range = highest_note-lowest_note
