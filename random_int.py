#save this file as random_int.py
from random import randint
def ranint():
	r = randint(65,91)
	return r
	
def main():
	for r in range (10):
		ri = ranint()
		print (ri,end="")

	
main()
