import numpy as np
import pandas as pd
import msgpack
import glob
import midi_manipulation
import os
import tensorflow as tf
from tensorflow.python.ops import control_flow_ops
from tensorflow.contrib import rnn
from tensorflow.contrib import legacy_seq2seq
from tqdm import tqdm


class Model():
	def selection(args, self,training = True):
		self.args = args
		if not training:
			args.batch_size = 1
			args.seq_length = 1

			#Selecting the model
			print(
				'Seleccionar Modelo:')
			if args.model = 'rnn':
				cell_fn = rnn.RNNCell
			elif args.model 'gru':
				cell_fn = rnn.GruCell
			elif args.model = 'lstm':
				cell_fn = rnn.LSTMCell
			elif args.model = 'nas':
				cell_fn = rnn.NASCell
			else:
				print('Modelo no soportado')
				raise Exception("Modelo no soportado {}".format(args.model))
			
			cells = []
			for _ in range(args.num_layers):
				cell = cell_fn(args.rnn_size)
				if training and (args.output_keep_prob < 1.0 or ags.input_keep_prob < 1.0):
					cell = rnn.DropoutWrapper(cell,
											  input_keep_prob=args.input_keep_prob,
											  output_keep_prob=args.output_keep_prob)
				cells.append(cell)
			self.cell = cell = rnn.MultiRNNCell(cells, state_is_tuple = True)

			self.input_data = 


	os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

	def get_songs(path):
	    files = glob.glob('{}/*.mid*'.format(path))
	    songs = []
	    for f in tqdm(files):
	        try:
	            song = np.array(midi_manipulation.midiToNoteStateMatrix(f))
	            if np.array(song).shape[0] > 50:
	                songs.append(song)
	        except Exception as e:
	            raise e
	    return songs


	songs = get_songs('Pop_Music_Midi')  # These songs have already been converted from midi to msgpack
	print("{} songs processed".format(len(songs)))
	###################################################

