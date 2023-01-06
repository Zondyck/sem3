#!/usr/bin/env python3 

class Ptak:
	hlad = 100
	vaha = 50
		
	def __init__(self, hlad, vaha):
		
		self.hlad = hlad
		self.vaha = vaha
				
	def snez (self, gramu):
		self.vaha += gramu
		self.hlad -= gramu		

	def __str__(self):
		return ("Jsem pták s váhou {0} a mám hlad {1}.".format(self.vaha, self.hlad))

p = Ptak(20,40)
print(p)
p.snez(10)
print(p)