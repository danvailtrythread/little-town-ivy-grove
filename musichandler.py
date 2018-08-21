from multiprocessing import Process
import os
import subprocess

EFFECTS = {} #This holds the sound effects in the game
MUSIC = {} #This will hold a name and value of songs in the game

#DEFINE SONGS
intro = os.getcwd() + "/music/intro.mp3"
crystalcave = os.getcwd() + "/music/crystalcave.mp3"
storytime = os.getcwd() + "/music/storytime.mp3"
MUSIC['intro'] = intro
MUSIC['storytime'] = storytime
MUSIC['crystalcave'] = crystalcave
MUSIC['delusion'] = os.getcwd() + "/music/delusion.mp3"
MUSIC['forest1'] = os.getcwd() + "/music/forest.mp3"
MUSIC['wastelandbattle'] = os.getcwd() + "/music/wastelandbattle.mp3"
MUSIC['perpetualtension'] = os.getcwd() + "/music/perpetualtension.mp3"

#DEFINE EFFECTS
EFFECTS['gold1'] = os.getcwd() + "/sfx/Pickup_Gold_00.mp3"
EFFECTS['gold2'] = os.getcwd() + "/sfx/Pickup_Gold_01.mp3"
EFFECTS['gold3'] = os.getcwd() + "/sfx/Pickup_Gold_02.mp3"
EFFECTS['gold4'] = os.getcwd() + "/sfx/Pickup_Gold_03.mp3"
EFFECTS['ambience'] = os.getcwd() + "/sfx/Ambience_Cave_00.mp3"
EFFECTS['dragon1'] = os.getcwd() + "/sfx/Dragon_Growl_00.mp3"
EFFECTS['dragon2'] = os.getcwd() + "/sfx/Dragon_Growl_01.mp3"
EFFECTS['spell1'] = os.getcwd() + "/sfx/Spell_00.mp3"
EFFECTS['spell2'] = os.getcwd() + "/sfx/Spell_01.mp3"
EFFECTS['spell3'] = os.getcwd() + "/sfx/Spell_02.mp3"
EFFECTS['spell4'] = os.getcwd() + "/sfx/Spell_03.mp3"
EFFECTS['spell5'] = os.getcwd() + "/sfx/Spell_04.mp3"
EFFECTS['trap1'] = os.getcwd() + "/sfx/Trap_00.mp3"
EFFECTS['trap2'] = os.getcwd() + "/sfx/Trap_01.mp3"
EFFECTS['trap3'] = os.getcwd() + "/sfx/Trap_02.mp3"
EFFECTS['train'] = os.getcwd() + "/sfx/train.aiff"
EFFECTS['train2'] = os.getcwd() + "/sfx/train2.mp3"

class MusicPlayer:
	def __init__(self):
		self.isplaying = False
		self.last_played = None
		self.current_song = None
		self.thr = None

	def last_song(self):
		return "The last song played was titled: %s" % self.last_played
	
	def current_song(self):
		return "The current song being played is titled: %s" % self.current_song

	def is_playing(self):
		if self.thr != None:
			return self.thr.is_alive()

	def play(self, song):
		"""Play a specific song"""
		if self.is_playing():
			self.stop()
		self.current_song = song
		if self.thr != None:
			if self.thr.is_alive():
				print("currently song playing..")
		self.thr = Process(target=subprocess.call, args=[["afplay", MUSIC[song]]])
		self.thr.start()

	def stop(self):
		if self.is_playing():
			self.thr.terminate()
			subprocess.call(["killall", "afplay"], shell=False)

	def play_sound_effect(self, effect):
		try:
			sfx = Process(target=subprocess.call, args=[["afplay", EFFECTS[effect]]])
			sfx.start()
		except KeyError:
			print("Sound effect '%s' not found in database" % str(effect))

