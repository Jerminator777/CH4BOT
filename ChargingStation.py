import Entity
class ChargingStation(Entity.Entity):
	def __init__(self, xposition, yposition):
		Entity.Entity.__init__(self, [xposition, yposition, 25, 25], "c")
		self.status = "Available"
		
	def Send_Availability(self):
		if self.status == "Available":
			print([self.xposition, self.yposition])	
		
	def Receive_Signal(self, signal_type):
		#signal_type is ["command" , [xpos_station, ypos_station]]
		if signal_type[0] == "Request":
			self.Send_Availability()
		elif signal_type[0] == "Selection":
		    [xsel, ysel] = signal_type[1]
			if [xsel, ysel] == [self.xposition, self.yposition]:		
				self.status = "Reserved"
				print("Reserved")	
