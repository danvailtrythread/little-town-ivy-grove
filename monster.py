from item import *
import random

class Monster:
	def __init__(self, name, stats):
		"""Pass in a dict of data describing the monster"""
		#When establishing monsters, it is up to you what do define,
		# however you should include health, basehp, atk, def, speed, accuracy
		self.name = name
		if isinstance(stats, dict):
			for k,v in stats.iteritems():
				setattr(self, k, v)
		else:
			raise AttributeError("Please pass in a dictionary object to the 'stats' parameter")

		#Now we add standard monster features
		self.bag = {}
		self.gold = random.randint(0, 20)

		if not hasattr(self, "health"):
			self.health = random.randint(5, 10)

		self.basehealth = self.health

	def set_loot(self, items):
		ilist = []
		if isinstance(items, Item):
			ilist.append(items.name)
			self.bag[items.name] = items
		elif isinstance(items, list):
			for i in items:
				ilist.append(i.name)
				self.bag[i.name] = i

		return str(ilist)

	def add_gold(self, amt):
		self.gold += amt

	def remove_gold(self, amt):
		self.gold -= remove_gold
		if self.gold <= 0:
			self.gold = 0

	def is_dead(self):
		if self.health <= 0:
			return True
		else:
			return False

	def award(self, player):
		player.add_inv(self.bag)
		player.add_gold(self.gold)
		return

	def take_damage(self, amt, player):
		"""take x damage from p player"""
		print("%s took %d damage from %s" % (self.name, amt, player.name))
		self.health - amt
		if self.is_dead():
			print("%s has been demolished." % self.name)
			self.award(player)
			del(self)
		elif self.health < self.basehealth * 0.5:
			print("%s is growing weary. Keep it up!" % self.name)
		elif self.health < self.basehealth * 0.25:
			print("%s is having their last breaths. Almost there!" % self.name)

	def __repr__(self):
		return str(self.__dict__)

a = Monster("a", {"defense":2})
b = Item("apple", {"health":3, "stamina":5})
c = Item("wooden sword", {"attack":4, "accuracy":3})
