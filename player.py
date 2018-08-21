class Player:
    def __init__(self, name):
        """Our first class of the project :)"""
        self.name = name

        #Describe basic attributes of the player
        self.alive = True
        self.level = 1
        self.health = 25
        self.basehealth = 25
        self.attack = 10
        self.defense = 0
        self.speed = 36
        self.accuracy = 75
        self.evasion = 4
        self.experience = 20
        self.exp_to_next_level = 100

        #sleepiness
        self.sleep = 100
        self.sleeplimit = 100
        self.pos = (10, 10)


        #Add inventory
        self.inventory = {}
        self.inventory["bag"] = {}
        self.inventory["gold"] = 25

        #Add Equipment
        self.equipment = {}
        self.equipment["head"] = None
        self.equipment["armor"] = None
        self.equipment["weapon"] = None
        self.equipment["amulet"] = None
        self.equipment["ring"] = None

    def __repr__(self):
        """__repr__ is what results when you type print(player_object)"""
        result = ".----------.----------.----------.----------.----------.----------.\n"
        result += "| Health:  %d / %d   |  Attack:   %d       |  Defense:    %d     \n" % (self.health, self.basehealth, self.attack, self.defense)
        result += "|____________________|_____________________|_____________________\n"
        result += "| Equipment:         |   Gold:  %d         |  Sleep:  %d / %d    \n" % (self.inventory['gold'], self.sleep, self.sleeplimit)
        result += "|    Head: %s        |_____________________|_____________________\n" % self.equipment["head"]
        result += "|    Armor: %s       |  Experience:      %d / %d                 \n" % (self.equipment["armor"],self.experience, self.exp_to_next_level)
        result += "|    Weapon: %s      |  |%s\n" % (self.equipment["weapon"], self.get_exp_str())
        result += "|    Amulet: %s      |                                           \n" % self.equipment["amulet"]
        result += "|    Ring: %s        |                                           \n" % self.equipment["ring"]
        result += "|____________________|___________________________________________\n"

        return result

    def get_exp_str(self):
        """Turn the current exp into a visual bar"""
        perc = float(self.experience) / self.exp_to_next_level
        #Now we need to divide it into 40 parts
        filled_slots = int(perc * 40)
        rstr = ""
        for i in range(0, filled_slots):
            rstr += "#"
        for b in range(0, (40 - filled_slots)):
            rstr += " "
        return rstr

    def exp_str(self):
        expstr = self.get_exp_str()
        print(".--------------  %d / %d  ---------------." % (self.experience, self.exp_to_next_level))
        print("| %s"%expstr)
        return

    def add_gold(self, amount):
        self.inventory["gold"] += amount
        print("You earned %d gold!" % amount)

    def spend_gold(self, amount):
        if self.inventory["gold"] - amount < 0:
            print("You do not have enough gold")
        else:
            self.inventory["gold"] -= amount
            print("You spent %d gold." % amount)

    def remove_gold(self, amount):
        print("You lost %d gold." % amount)
        self.inventory["gold"] -= amount
        if self.inventory["gold"] < 0:
            self.inventory["gold"] = 0


    def die(self):
        """death funcionality"""
        #morbid
        pass

    def take_damage(self, amt):
        self.health -= amt
        print("%s took %d damage." % (self.name, amt))
        if self.health <= 0:
            print("%s adventured valiantly, alas. Your time has come to pass." % self.name)
            self.die()
        elif self.health <= self.basehealth * 0.5:
            print("You are growing weary, but you still have some fight in you")
            print("%d / %d HP" % (self.health, self.basehealth))
        elif self.health <= self.basehealth * 0.25:
            print("You are getting very weak, find some way to heal!")
            print("%d / %d HP" % (self.health, self.basehealth))
