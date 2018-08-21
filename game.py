#First let's import the system modules we'll be using
import random
import difflib
import time
import sys
import re
import os
import subprocess


#Now we import our user defined modules
from player import *
from monster import *
from item import *
from room import *
from musichandler import *

#initialize sounds
#def play_music(file):
#    thr = threading.Thread(target=subprocess.call, args=[["afplay", file]])
#    thr.start()

#audio_file = os.getcwd() + "/music/intro.mp3"
#play_music(audio_file)

mixer = MusicPlayer()
mixer.play('intro')

#List of keywords to use in the game
commands =[
"attack",
"north",
"east",
"south",
"west",
"open",
"search",
"look",
"take",
"fight",
"run",
"stats",
"health",
"help",
"quit",
"exit",
"gold",
"items",
"sleep",
"eat",
"rest",
"shake tree",
"harvest",
"dig",
"clear",
"exp"]

admin_commands = [
'add gold',
'remove gold',
'heal',
'song playing',
'stop song',
'play song',
'list songs',
'play sound']

class Game:
    def __init__(self, player):
        """Operate main game loop and manage state"""
        self.player = player
        self.running = True
        self.isadmin = False
        self.commands = commands

        #Place system window into correct size
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=HEIGHT, cols=WIDTH))

        try:
            if sys.argv[1] == "secretadmin":
                print("~ . ~ . ~ Starting game as Admin ~ . ~ . ~")
                self.isadmin = True
                self.commands = commands + admin_commands
                time.sleep(1)


        except IndexError:
            pass


        #This part just starts the game when a new Game object instance is created
        if self.running:
            self.run()

    def printframe(self, contents):
        print(".----------.----------.----------.----------.----------.----------.----------.")
        for c in contents.split("\n"):
            print("| %s" % str(c))
        print(".__________.__________.__________.__________.__________.__________.__________.")

    def clearframe(self):
        for i in range(0, HEIGHT):
            print("")

    def title_screen(self):
        """Show the intro title screen"""
        print("################################################################################")
        print("#|                                                                             #")
        print("#|                                                                             #")
        print("#|                                                                             #")
        print("#|           _      _  _    _    _         _____                               #")
        print("#|          | |    (_)| |  | |  | |       |_   _|                              #")
        print("#|          | |     _ | |_ | |_ | |  ___    | |  ___ __      __ _ __           #")
        print("#|          | |    | || __|| __|| | / _ \   | | / _ ]\ \ /\ / /| '_ \          #")
        print("#|          | |____| || |_ | |_ | ||  __/   | || (_) |\ V  V / | | | |         #")
        print("#|          \_____/|_| \__| \__||_| \___|   \_/ \___/  \_/\_/  |_| |_|         #")
        print("#|                                                                             #")
        print("#|      ___             _  _             ___                                   #")
        print("#|     |_ _|   __ __   | || |    o O O  / __|     _ _    ___    __ __    ___   #")
        print("#|      | |    \ V /    \_, |   o      | (_ |    | '_|  / _ \   \ V /   / -_)  #")
        print("#|     |___|   _\_/_   _|__/   TS__[O]  \___|   _|_|_   \___/   _\_/_   \___|  #")
        print("#|   _|'''''|_|'''''|_| ''''| {======|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''| #")
        print("#|  '`-0-0-''`-0-0-''`-0-0-'./o--000''`-0-0-''`-0-0-''`-0-0-''`-0-0-''`-0-0-'  #")
        print("#|                                                                             #")
        print("#|                        Press 1 to load game                                 #")
        print("#|                        Press 2 to start new game                            #")
        print("#|                        Press 3 for game options                             #")
        print("#|                                                                             #")
        print("#|                                                                             #")
        print("################################################################################")
        #Intro screen above (code folded)
        start = True
        while start:
            cmd = raw_input(" > ")
            wronginput = 0

            if cmd == "1":
                start = False
                self.load_game_screen()
            elif cmd == "2":
                start = False
                self.new_game()
            
            elif cmd == "3":
                start = False
                self.show_options()
            else:
                wronginput += 1
                if (wronginput > 2):
                    print("Please type 1, 2, or 3 to select options")
                    wronginput = 0

    def load_game_screen(self):
        """Show different games that have been saved"""
        #Pull in .save files from data directory
        pass

    def new_game(self):
        """Start a new game"""
        self.clearframe()
        mixer.stop()
        mixer.play_sound_effect('train')
        print(".")
        time.sleep(GAMERATE)
        self.clearframe()
        print(". . . ")
        time.sleep(GAMERATE)
        self.clearframe()
        print(". . . . . ")
        time.sleep(GAMERATE)
        self.clearframe()
        print(".. Hello?")
        time.sleep(GAMERATE)
        mixer.play('storytime')
        print("Ehh, it looks like you hit your head pretty bad. Are you okay?")
        time.sleep(GAMERATE)
        self.clearframe()
        print("No reason to be embarrased.. weird things happen all the time in this town.")
        time.sleep(GAMERATE)
        print(". . . ")
        time.sleep(GAMERATE)
        self.clearframe()



        print("Do you remember your name?")
        time.sleep(3)
        naming = True
        while naming:
            name = raw_input(" Enter your name > ")
            time.sleep(2)
            print("So your name is %s?"%name)
            confirming = True
            while confirming:
                inp = raw_input(" Y or N > ")
                if inp == "Y" or inp == "y" or inp == "yes":
                    confirming = False
                    time.sleep(GAMERATE)
                    print("That's a silly name, but we each have one I guess!")
                    naming = False
                else:
                    time.sleep(GAMERATE)
                    print("Let's try this again. . .")
                    time.sleep(GAMERATE)
                    break


            naming = False
        print("Hello %s"%name)

    def show_options(self):
        """change the game options"""
        pass

    def run(self):
        failed_attempts = 0
        #Show the title screen
        self.title_screen()
        while self.running:
            # - - - All of the checking of player commands goes here! - - - - #

            #if a user enters a faulty command, we can catch it with this!
            try: 
                #take in a new command entered by the user
                command = raw_input(" > ")
                
                #We will use a check_command function to see which command is called:
                if self.check_command(command) == "stats":
                    print(self.player)

                elif self.check_command(command) == "exit" or self.check_command(command) == "quit":
                    mixer.stop()
                    break

                elif self.check_command(command) == "exp":
                    player.exp_str()

                elif self.check_command(command) == "gold":
                    self.printframe("You currently have %d gold schmeckles"%self.player.inventory["gold"])
                    rsfx = random.randint(0, 3)
                    if rsfx == 0:
                        mixer.play_sound_effect('gold1')
                    elif rsfx == 1:
                        mixer.play_sound_effect('gold2')
                    elif rsfx == 2:
                        mixer.play_sound_effect('gold3')
                    elif rsfx == 3:
                        mixer.play_sound_effect('gold4')

                elif self.check_command(command) == "help":
                    for cmds in commands:
                        print cmds
                        time.sleep(0.2)

                elif self.check_command(command) == "look":
                    print(ROOMLIST[player.pos[0]][player.pos[1]].desc)

                elif self.check_command(command) == "clear":
                    self.clearframe()

                elif self.check_command(command) == "song playing":
                    print(mixer.is_playing())

                elif self.check_command(command) == "stop song":
                    print("Stopping current song")
                    mixer.stop()

                elif self.check_command(command) == "play song":
                    try:
                        songname = str(command.split(" ")[2])
                        mixer.play(songname)
                    except IndexError:
                        print("No song found, try 'play song songname' to select a song")
                    except KeyError:
                        print("The song '%s' was not found in the database." % songname)

                elif self.check_command(command) == "play sound":
                    try:
                        soundname = str(command.split(" ")[2])
                        mixer.play_sound_effect(soundname)
                    except IndexError:
                        print("No song found, try 'play sound soundname' to select a sound effect")
                    except KeyError:
                        print("The sound effect '%s' was not found in the database." % songname)



                elif self.check_command(command) == "add gold":
                    try:
                        amount = int(re.search(r'\d+', command).group())
                        self.player.add_gold(amount)
                        rsfx = random.randint(0, 3)
                        if rsfx == 0:
                            mixer.play_sound_effect('gold1')
                        elif rsfx == 1:
                            mixer.play_sound_effect('gold2')
                        elif rsfx == 2:
                            mixer.play_sound_effect('gold3')
                        elif rsfx == 3:
                            mixer.play_sound_effect('gold4')

                    except AttributeError:
                        print("No gold found, try again with the format 'add gold 22' for example")

                elif self.check_command(command) == "remove gold":
                    try:
                        amount = int(re.search(r'\d+', command).group())
                        self.player.remove_gold(amount)
                        rsfx = random.randint(0, 3)
                        if rsfx == 0:
                            mixer.play_sound_effect('gold1')
                        elif rsfx == 1:
                            mixer.play_sound_effect('gold2')
                        elif rsfx == 2:
                            mixer.play_sound_effect('gold3')
                        elif rsfx == 3:
                            mixer.play_sound_effect('gold4')
                    except AttributeError:
                        print("No gold found, try again with the format 'remove gold 22' for example")

                else:
                    print("Command not found")
                    failed_attempts += 1

                if failed_attempts > 2:
                    print("Try using the 'help' command to see a list of commands")
                    failed_attempts = 0


            except IndexError:
                print("Command not found")
                continue

    def check_command(self, cmd):
        """Return a string of which command is closest from the commands list"""
        try:
            return difflib.get_close_matches(cmd, self.commands)[0]
        except IndexError:
            return None

player = Player("Matt")
game = Game(player)