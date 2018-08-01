
class ParkingLot(dict):
	def __init__(self, row, col):
		self.row = row
		self.col = col 
		self.canvas_dimx = 3000
		self.canvas_dimy = 3000
		self.spot_dimx = 200  #these can be open to parameters later
		self.spot_dimy = 350
		self.sep_dimx = 10
		self.sep_dimy = 50

	def generateParkingGrid(self):
		grid_loc = {'x' : 1, 'y' : 1}
		max_x, max_y = self.calcMaxCol(), self.calcMaxRow()
		print(max_x, max_y)

	def createParkingSpot(self, startx, starty):
		#will need name genenator
		self['newname'] = parkingSpot(starx, starty, grid_loc)

	def calcMaxCol(self):
		count_x = 0
		current_width = 0 
		while current_width <= self.canvas_dimx: 
			count_x +=1
			current_width = current_width + self.spot_dimx + self.sep_dimx
		return count_x

	def calcMaxRow(self):
		count_y = 0
		current_width = 0 
		while current_width <= self.canvas_dimy: 
			count_y +=1
			current_width = current_width + self.spot_dimy + self.sep_dimy
		return count_y



class parkingSpot:
	def __init__(self, startx, starty, grid_loc):
		self.startx = startx
		self.starty = starty
		self.color = 'yellowgreen'
		self.grid_loc = grid_loc

	def changeStatus(self):
		if self.color == 'yellowgreen':
			self.color = 'crimson' #occupied
		else:
			self.color = 'yellowgreen' #open 

