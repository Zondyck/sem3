
	
#!/usr/bin/env python3 

class Ptak:
	
	def __init__(self, hlad, vaha):
		
		self._hlad = hlad
		self._vaha = vaha
		
	def snez (self, hlad, vaha):
		hlad = 100
		vaha = 50
		
		if self._hlad > 0:
			self._vaha = vaha + 100 - hlad
	      return ("Jsem pták s váhou {0} a hladem {1}".format(self.vaha, self.hlad))
	      
p = Ptak
p.snez()