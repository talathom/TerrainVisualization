import vizcam
from Controller import *

window = viz.MainWindow
viz.window.setSize(640, 480) # Set Window Size
pivotNav = vizcam.PivotNavigate() # Turn on Pilot Navigation
view = viz.MainView
mat = viz.Matrix()
mat.postTrans(100, 1950, 100) # Move the Camera to a Position where the terrain is visible
view.setMatrix(mat)

inputFile = open('greysriver.asc', 'r') # Open the file
#Read in the number of rows and columns
firstLine = inputFile.readline()
NCols = int(firstLine.split()[1])
secondLine = inputFile.readline()
NRows = int(secondLine.split()[1])
arr = list()

# Consume irrelevant lines
for i in range(0, 4):
	inputFile.readline()
# Read in all remaining lines
vertices = inputFile.readlines()

vertIndex = 0
for i in range(0, NRows):
	arr.append(vertices[i].split())

max = float(arr[0][0])
min = float(arr[0][0])
#Find max and min elevation
for i  in range(0, NRows):
	for j in range(0, NCols):
		arr[i][j] = float(arr[i][j])
		if arr[i][j] > max:
			max = arr[i][j]
		if arr[i][j] < min:
			min = arr[i][j]
# Output info
print("Rows "+ str(NRows))
print("Columns "+ str(NCols))
print("Max "+ str(max))
print("Min "+ str(min))

# Generate Terrain
viz.startLayer(viz.TRIANGLES)
for z in range(0, NRows-1): 
	for x in range(0, NCols-1):
		viz.vertex(x, arr[z][x], z)
		viz.vertex(x, arr[z+1][x], z+1)
		viz.vertex(x+1, arr[z][x+1], z)
		viz.vertex(x+1, arr[z][x+1], z)
		viz.vertex(x, arr[z+1][x], z+1)
		viz.vertex(x+1, arr[z+1][x+1], z+1)
		if arr[z][x] < 1896:
			viz.vertexColor(0, 0, 1)
		elif arr[z][x] < 1950:
			viz.vertexColor(0,0.25, 0)
		elif arr[z][x] < 2000:
			viz.vertexColor(0,0.5, 0)
		elif arr[z][x] < 2050:
			viz.vertexColor(0,.75, 0)
		else:
			viz.vertexColor(0, 1, 0)
viz.endLayer()

viz.go()

c = Controller()