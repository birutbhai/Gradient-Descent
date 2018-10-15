# Gradient descent for regression with only one attribute and till 5 iterations
def error_cal(x_values, y_values, theta_0, theta_1, training_data_size):
	error_val = 0
	for a in range(training_data_size):
		temp = (theta_0 + theta_1*x_values[a]) - y_values[a]
		error_val += temp * temp
	error_val /= float(2*training_data_size)
	return error_val
	
def gradient_descent(x_values, y_values, initial_theta_0, initial_theta_1):
            theta_0 = initial_theta_0
            theta_1 = initial_theta_1
            step_size = .25
            training_data_size = len(x_values)
            initial_error_value = error_cal(x_values, y_values, theta_0, theta_1, training_data_size)
            print "Initial values of theta_0 and theta_1 are " + str(theta_0) + str(" and ") + str(theta_1) + " respectively."
            print "Initial error value : " + str(initial_error_value) + "."
            print "Starting gardient descent algorithm iteration with step size as " + str(step_size) + "."
            for i in range(5):
            	print "Iteration" + str(i+1) + " starts."
            	temp0 = 0
            	temp1 = 0
            	for a in range(training_data_size):
            		temp0 += ((theta_0 + theta_1*x_values[a]) - y_values[a])
            		temp1 += ((theta_0 + theta_1*x_values[a]) - y_values[a]) * x_values[a]
            	temp0 /= float(training_data_size)
            	temp1 /= float(training_data_size)
            	theta_0 -= step_size * temp0
            	theta_1 -= step_size * temp1
            	print "After iteration" + str(i+1) + ", the value of theta_0 and theta_1 are " + str(theta_0) + " and " + str(theta_1) + " respectively."
            	print "Error value after iteration" + str(i+1) + ": " + str(error_cal(x_values, y_values, theta_0, theta_1, training_data_size)) + "." 
            	print "Iteration" + str(i+1) + " ends."
            change_in_error =  initial_error_value - error_cal(x_values, y_values, theta_0, theta_1, training_data_size)
            if change_in_error > 0:
            	print "Error value went down."
            elif change_in_error == 0:
            	print "Error value did not change."
            else:
            	print "Error value went up."
def main(x_values, y_values, initial_theta_0, initial_theta_1):
	gradient_descent(x_values, y_values, initial_theta_0, initial_theta_1)
 
x_values = [3, 1, 0, 4]
y_values = [2, 2, 1, 3]
initial_theta_0 = 0
initial_theta_1 = 1
main(x_values, y_values, initial_theta_0, initial_theta_1)
 	
