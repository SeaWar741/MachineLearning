#Import MNIST data
import input_data
mnist = input_data.read_data_sets("/tmp", one_hot=True)

import tensorflow as tf

#Set parameters
learning_rate = 0.01
training_iteration = 30
batch_size = 100
display_step = 2

#TF graph input
x = tf.placeholder("float", [None, 784]) #mnist data image of shape 28*28=784
y = tf.placeholder("float", [None, 10]) #0-9 digits recognition =>10 classes

#Create a model

#Set model Weights
w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

with tf.name_scope("Wx_b") as scope: #Organizar nodos
	#construc a linear model
	model = tf.nn.softmax(tf.matmul(x, w) +b)

#Add summary ops to collect data
w_h = tf.histogram_summary("Weights", W)
b_h = tf.histogram_summary("biases", b)

#Mas scopes limpian la representacion grafica
with tf.name_scope("cost_function") as scope:
	#minimizar el error usando cross entropy
	#cross entropy
	cost_function = -tf.reduce_sum(y*tf.log(model))
	#create a summary to monitor the cost function
	tf.scalar_summary("cost_function", cost_function)

with tf.name_scope("train") as scope:
	#pendiente de decrecimiento --> funcion de optimizacion para encontrar el vertice en la grafica
	optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)

#Inicializar las variables
int = tf.initialize_all_variables()

#Merge all summaries into a single operator
merged_summary_op = tf.merge_all_summaries()

#Inicializar grafica
with tf.Session() as sess:
	sess.run(init)

	#Set the logs writer to the folder /tmp/tensorflow_logs
	summary_writer = tf.train.SummaryWriter('/home/SeaWar/work/logs', graph_def = sess.graph_def)

	#Ciclo de entrenamiento
	for iteration in range(training_iteration):
		avg_cost = 0.
		total_batch = int(mnist.train.num_examples/batch_size)
		#loop over all batches
		for i in range(total_batch):
			batch_xs, batch_ys = mnist.train.next_batch(batch_size)
			#Fit training using batch data
			sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
			#compute the average loss
			avg_cost += sess.run(cost_function, feed_dict={x: batch_xs, y: batch_ys})/total_batch
			#write Logs for each iteration
			summary_str = sess.run(merged_summary_op, feed_dict={x: batch_xs, y: batch_ys})
			summary_writer.add_summary(summary_str, iteration*total_batch + i)
		#Display logs per iteration
		if iteration % display_step == 0:
			print("Iteration:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(avg_cost))
			#print("error")
	print ("Tuning Completed!")

	#Prueba del modelo
	preductions = tf.equal(tf.argmax(model, 1), tf.argmax(y,1))
	#Precision del calculo
	accuracy = tg.reduce_mean(tf.cast(preductions, "float"))
	print("Accuracy: ", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))
