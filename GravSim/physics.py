from vector import vector
class Object:
	def __init__(self, postition=[0,0,0], velocity=[0,0,0], mass=0, charge=0, color=(0,0,0)):
		self.m=mass
		self.q=charge
		self.x=vector(postition)
		self.v=vector(velocity)
		self.color=color

class System:
	def __init__(self, objects=[], timestep=1e-3, gravConst=1, electricConst=1):
		self.o=objects
		self.t=timestep
		self.gK=gravConst
		self.eK=electricConst

	def step(self):
		for o1 in self.o:
			for o2 in self.o:
				r=o2.x-o1.x
				if(abs(r)==0):
					continue
				else:
					o1.v=o1.v+r*(o2.m*self.gK/(abs(r)*abs(r)*abs(r))*self.t)

		for o1 in self.o:
			o1.x=o1.x+o1.v*self.t

	def out(self):
		for i in range(len(self.o)):
			print "o"+ str(i)+": "+str(self.o[i].x.x)
