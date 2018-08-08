import numpy as np
import pandas as pd
import msgpack
import glob
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
		
