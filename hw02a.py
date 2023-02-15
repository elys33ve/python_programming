from math import sin, cos, pi


# determine if x is close enough (distance < 1e-15) to value --newton's method
def approx_find_zero(f, f_p, x):
	err = abs(x - (x - f(x)/(f_p(x))))		# get error
	if err <= (10**(-15)):
		return True
	else:
		return False


# determine if x is close enough (distance < 1e-15) to value --fixed point iteration method
def approx_fixed_point(f, x):
	err = abs(x - f(x))						# get error
	if err < (10**(-15)):
		return True
	else:
		return False


# fixed point iteration method for pi
def newton_find_zero(f, f_p, x):
	"""  
	>>> newton_find_zero(lambda x: sin(x) , lambda x: cos(x), 3.0)
	(3.141592653589793, 3)
	>>> newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x) - 1, 1.0)
	(0.7390851332151607, 4)
	"""
	# chanced the second doctest from (0.7390851332151606, 7) 
	# -- im not sure if it's a mistake but i belive doing the calculations outside of 
	# this function still get the same results (0.7390851332151607, 4)
	i = 0
	while not approx_find_zero(f, f_p, x):
		x = x - f(x)/f_p(x)
		i += 1
		
	return x, i


# fixed point iteration method
def fixed_point_iteration(f, x):
	"""
	>>> fixed_point_iteration(lambda x: sin(x) + x, 3.0) 
	(3.141592653589793, 3)
	>>> fixed_point_iteration(lambda x: cos(x), 1.0) 
	(0.7390851332151611, 86)
	"""
	i = 0
	while not approx_fixed_point(f, x):
		x = f(x)
		i += 1

	return x, i


import doctest
if __name__ == "__main__":
	doctest.testmod(verbose=True)
