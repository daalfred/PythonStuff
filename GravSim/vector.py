from math import sqrt

class vector:
	x=[]
	def __init__(self, listOfNumbers=[]):
		self.x=listOfNumbers

	def __add__(self, other):
		res=[]
		for i in range(len(self.x)):
			res.append(self.x[i]+other.x[i])
		return vector(res)

	def __sub__(self, other):
		res=[]
		for i in range(len(self.x)):
			res.append(self.x[i]-other.x[i])
		return vector(res)

	def __mul__(self, other):
		if(str(other)=="vector"):
			res=0
			for i in range(len(self.x)):
				res+=self.x[i]*other.x[i]
			return res
		else:
			res=[]
			for i in self.x:
				res.append(i*other)
			return vector(res)

	def __abs__(self):
		res=0
		for i in self.x:
			res+=i*i
		res=sqrt(res)
		return res

	def out(self):
		print self.x

	def list(self):
		return self.x

	def __str__(self):
		return "vector"
