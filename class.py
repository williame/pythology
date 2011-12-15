#!/usr/bin/env python

class Test:
	def __init__(self,a,b):
		self.a=a;
		self.b=b;
	
def main():
	x = Test(10,3)
	print x.a
	print x.b

if __name__ == '__main__':
	main()
	
