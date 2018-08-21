w,h = 20, 20 #setup a 20 by 20 array
ROOMLIST = [[0 for x in range(w)] for y in range(h)]

class Room:
	def __init__(self, pos, name, desc):
		self.pos = pos
		self.name = name
		self.desc = desc
		ROOMLIST[pos[0]][pos[1]] = self

	def read_north(self):
		"""Read the desc of a north room"""
		try:
			print(ROOMLIST[self.pos[0]][self.pos[1]-1].desc)
		except AttributeError:
			print("There seems to be nothing there")
		except IndexError:
			print("You see nothing but mountains to the north.")


homebase = Room((10,10), "Train Closet", "You seem to have fallen over in an old supply closet. You appear to be on a train. \nIn front of you stands an approachable fellow with a peacoat and round glasses. \nMaybe if you ask 'where am I' he will give you more information")
