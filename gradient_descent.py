from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

# Modificar (df['semana'], df['kwh'] de acuerdo a los headers de su archivo

def graph(formula, x_range, df):
	x = array(x_range)
	y = eval(formula)
	plt.plot(x, y)
	plt.plot(df['semana'], df['kwh'], 'o')
	plt.show()

def compute_error_for_line_given_points(b,m,points):
	totalError = 0 	
	for i in points:
		x = i[0]
		y = i[1]
		totalError += (y-(m*x + b)) ** 2
	return totalError/ float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
	#gradient descent
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in points:
		x = i[0]
		y = i[1]
		b_gradient += -(2/N) * (y - (m_current * x + b_current))
		m_gradient += -(2/N) * x * (y - (m_current * x + b_current))
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)
	return [new_b,new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteartions):
	b = starting_b
	m = starting_m
	for i in range(num_iteartions):
		b,m = step_gradient(b, m, array(points), learning_rate)
	return [b,m]

def run():
	#Cargando los datos
	df = pd.read_csv('archivo.csv')
	X = df['semana']
	Y = df['kwh']
	points = []
	for i, j in zip(X, Y):
		points.append([i, j])
	learning_rate = 0.005
	#y=mx+b (formula)
	initial_b = 10
	initial_m = 5
	num_iterations = 5000
	print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    	print("Running...")
    	[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    	print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))
	graph("{0} * x + {1}".format(m, b), range(0, 25), df) 
	#Modificar los valores del range para incrementar el ranfo del trazado de la linea

if __name__ == "__main__":
	run()
