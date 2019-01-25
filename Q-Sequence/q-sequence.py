# Imports
from PIL import Image
import sys
import os
import time


# Check for parameter length
if len(sys.argv) == 2:
	n = int(sys.argv[1])
else:
	print("Expecting argument: Q-Folge.py <length>")
	exit()


# Generate Q-Sequence
t_ms = int(time.time()*1000)
t_start = t_ms
print("Calculating... ")
q = [1, 1]

for i in range(2,n):
	q = q + [q[i-q[i-1]]+q[i-q[i-2]]]

print("Done in " + str(int(time.time()*1000) - t_ms) + "ms.\n")

# Draw image, sf gives the size of each point, larger for larger pictures
t_ms = int(time.time()*1000)
print("Generating image...")
sf = int(n/2000) + 1

shift = [(x,y) for x in xrange(-99, 99)
	for y in xrange(-99, 99) if abs(x) + abs(y) < sf]

img = Image.new('1', (n + 2 * sf, max(q) + 1 + 2 * sf), color=0)

for i in range(n):
	for s in shift:
		img.putpixel(tuple(map(lambda x, y: x + y,
			(i + sf, max(q) + 1 + sf - q[i]), s)), 1)

plottime = (int(time.time()*1000) - t_ms)
print("Done in " + str(plottime) + "ms.\n")

# Open image
#img.save('q.bmp', 'BMP')

os.system('echo "' + str(n) + ',' + str(int(time.time()*1000) - t_start) +
	';" >> runtimeStats.csv')
#os.system('gwenview q.bmp')
#os.system('rm q.bmp')
