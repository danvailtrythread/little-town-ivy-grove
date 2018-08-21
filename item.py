from globals import *

class Item:
	def __init__(self, name, attrs):
		self.name = name
		if isinstance(attrs, dict):
			for k,v in attrs.iteritems():
				setattr(self, k, v)
		else:
			raise AttributeError("Please pass in a dictionary object to the 'attrs' parameter")

	def get_value(self):
		val = 0
		for i in self.__dict__.values():
			if isinstance(i, int):
				val += i
		return val * VALUE_COEFFICIENT

	def __repr__(self):
		return str(self.__dict__)


apple = Item('apple', {'health':10, 'stamina':10})