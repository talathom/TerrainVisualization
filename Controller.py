import viz
import math
class Controller(viz.EventClass):
	def __init__(self):
		# base class constructor 
		viz.EventClass.__init__(self)
		self.theta = 0
		self.x = 100
		self.y = 1950
		self.z = 100
		self.view = viz.MainView
		
		# set up keyboard and timer callback methods
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
	def onKeyDown(self,key):
			if key == 'a':
				mat = viz.Matrix()
				self.x -= 5
				mat.postTrans(self.x, self.y, self.z)
				self.view.setMatrix(mat)
				self.view.setMatrix(mat)
		
			if key == 'd':
				mat = viz.Matrix()
				self.x += 5
				mat.postTrans(self.x, self.y, self.z)
				self.view.setMatrix(mat)
			
			if  key == viz.KEY_UP:
				mat = viz.Matrix()
				self.y += 5
				mat.postTrans(self.x, self.y, self.z)
				self.view.setMatrix(mat)
			
			if  key == viz.KEY_DOWN:
				mat = viz.Matrix()
				self.y -= 5
				mat.postTrans(self.x, self.y, self.z)
				self.view.setMatrix(mat)
				
			if key == 'w':
				mat = viz.Matrix()
				self.z += 5
				mat.postTrans(self.x, self.y, self.z)
				self.view.setMatrix(mat)
				
			if key == 's':
				mat = viz.Matrix()
				self.z -= 5
				mat.postTrans(self.x, self.y, self.z)
				self.view.setMatrix(mat)