from numpy import *
from PIL import Image, ImageDraw, ImageFont



class ANN:
	def __init__(self, layers, alpha):
		self.layers = layers
		self.outputs = [zeros(i) for i in self.layers] #outputs[0]==input
		self.activation = self.outputs[1:]
		self.deltas = self.activation
		self.weights = [(random.rand(len(self.outputs[i+1]),len(self.outputs[i])+1)-.5)*1e-3 for i in range(len(self.outputs)-1)]
		self.alpha = alpha

	def forwardCalc(self, data=[]):
		self.outputs[0] = data
		for i in range(len(self.activation)):
			self.activation[i] = matmul(self.weights[i], append(self.outputs[i],1))
			self.outputs[i+1] = tanh(self.activation[i])

	def calcDeltas(self, ref=[]):
		self.deltas[-1] = (ref - self.outputs[-1]) * cosh(self.activation[-1]) ** -2
		for i in range(len(self.deltas)-1)[::-1]:
			self.deltas[i] = matmul(self.deltas[i+1], self.weights[i+1][:,:-1]) * cosh(self.activation[i])**-2

	def changeWeights(self):
		for i in range(len(self.weights)):
			self.weights[i] += self.alpha * matmul(transpose([self.deltas[i]]), [append(self.outputs[i],1)])

	def backPropagate(self, ref):
		self.calcDeltas(ref)
		self.changeWeights()

if __name__ == '__main__':
	font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",10)
	ann=ANN([3,1,3],1e-1)
	data=[]
	E=[]
	D=array([[10,0,0],[0,1,0],[0,0,1]])
	R=array([[0.707,-0.707,0],[0.707,0.707,0],[0,0,1]])
	for i in range(10):
		#c = int(random.rand(1)*10)
		img = Image.new('L', (10,10), (255))
		draw = ImageDraw.Draw(img)
		draw.text((2,2), str(i), (0), font)
		#data.append([array(img).ravel(), array([int(j == i) for j in range(0,10)])])

	for i in range(100000):
		a=matmul(R,matmul(D,random.rand(3)))/10
		data.append([a,a])

	for i in range(100000):
		p=int(random.rand()*10)
		ann.forwardCalc(data[i][0])
		ann.backPropagate(data[i][1])
		e=ann.outputs[-1]-data[i][1]

		E.append(matmul(e,e))
		if (i-1)%5000==0: print("Error: " + str(mean(E[-5000:-1])))

	for i in range(10):
		ann.forwardCalc(array([3,3,0])/10)
		print(str(ann.outputs[-1]))
		ann.forwardCalc(array([0,3,5])/10)
		print(str(ann.outputs[-1]))
	#print([size(d) for d in delta])
