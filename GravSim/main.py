from physics import *
from PIL import Image, ImageDraw
import time
size=2048*2
zoom=4
img = Image.new( 'RGB', (size,size), "black") # Create a new black image
pixels = img.load() # Create the pixel map

a=4

os1= [Object([100,0,0],[0,-.5,0],10,0,(255,0,0)), Object([-100,0,0],[0,.7,0],20,0,(0,255,0)), Object([0,-80,0],[0,0,0],80,0,(0,0,255))]
os2= [Object([100,0,0],[0,0,0],10,0,(255,0,0)), Object([-100,0,0],[0,0,0],20,0,(0,255,0)), Object([0,-80,0],[0,0,0],80,0,(0,0,255))]
os3= [Object([100,0,0],[0,.95,0],10,0,(255,0,0)), Object([-100,0,0],[0,-8.,0],20,0,(0,255,0)), Object([0,-80,0],[-0.1,0,0],80,0,(0,0,255)),Object([0,0,0],[0.5,-.1,0],20,0,(255,255,0))]
os4= [Object([100,0,0],[0,0.2,0],10,0,(255,0,0)), Object([-100,0,0],[0,-0.1,0],20,0,(0,255,0)),Object([0,0,0],[0,0,0],20,0,(255,255,0))]
os5= [Object([100,0,0],[0,-.5,0],20,0,(255,0,0)), Object([-100,0,0],[0,0.7,0],20,0,(0,255,0)), Object([0,-80,0],[0,0,0],20,0,(0,0,255))]
os6= [Object([100,0,0],[-0.05*a,0.08660254*a,0],20,0,(255,0,0)), Object([-100,0,0],[-0.05*a,-0.08660254*a,0],20,0,(0,255,0)), Object([0,-173.205,0],[0.1*a,0,0],20,0,(0,0,255))]

s = System(os6,0.005,1)

draw = ImageDraw.Draw(img)
for o in s.o:
	draw.ellipse(((int(o.x.x[0]*zoom)+size/2)%size-3, (int(o.x.x[1]*zoom)+size/2)%size-3, (int(o.x.x[0]*zoom)+size/2)%size+3, (int(o.x.x[1]*zoom)+size/2)%size+3), fill=(255,255,255))


for i in range(int(5e5)):
	s.step()
	for o in s.o:
		a=(int(o.x.x[0]*zoom)+size/2)
		b=(int(o.x.x[1]*zoom)+size/2)
		if size > a and size > b and a>0 and b>0:
			pixels[a%size,b%size]=o.color


#img.show()
img.save(str(len(s.o))+"mS"+str(time.time()), "BMP")
