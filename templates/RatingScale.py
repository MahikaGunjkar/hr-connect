import math
global scale
cout_r =0
cout_y =0
cout_g =0

def ratings():
	
	#allocate value to scale by importing the data from the database
	if(scale >= 4):
		cout_g = +1
	elif(scale ==2 or scale ==3):
		cout_y = +1
	else:
		cout_r = +1 

def final():
	if(cout_g>cout_y):
		if(cout_g>cout_r):
			return 'green'
		elif(cout_y>cout_r):
			return 'yellow'
	else:
			return 'red'

		