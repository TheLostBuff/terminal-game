import random 
from decimal import Decimal

class Player:
    def __init__(self, name=0, pronouns=0, occupation=0, home=0, size=0, alive = True):
        self.name = name
        self.job = occupation
        self.health = 100
        self.size = size
        self.life = alive
        self.home = home
        self.position = {}
        self.task ={}
        self.path =[]
        self.items = {}
        self.sights =[]
        self.friends = {}
        self.pronouns = []
  
    def character_setup(self, log=0):
        self.name = input ("What is my name?")

        pronouns = input (["What is my first pronoun?", "What is my second pronoun?", "What is my third pronoun?"])
        self.pronouns= pronouns.split(",")
        self.job = input ("Are you a Journeyman, warrior, or blacksmith?")
        self.home = input ("Where is my home?")
        valSize = False
        while valSize == False:
            temp_size= input("How big am I? (1-3)")
            valSize = False
            try: 
                self.size = int(temp_size)
                if self.size >3 or self.size < 1:
                    print("Invalid size. Please select a size from 1 to 3?")
                else:
                    valSize = True

            except:
                print("Invalid size. Please select a size from 1 to 3?")
        
            
        return Player(self.name, self.job, self.pronouns, self.home, self.size)


    def fight(self, enemy, log=0):
        if enemy.name in self.friends:
            print ("Why would we fight?")
            return
        if self.size > enemy.size:
            damage= int(self.size) - int(enemy.size)
            enemy.health -= damage
            if enemy.health > 0:
                print ("{enemy_name} was unwise to pick a fight with {self_name} and took ".format(enemy_name= enemy.name, self_name=self.name) + str(damage)+" damage. " + enemy.pronouns[0] + " now has " + str(enemy.health) + " health_points")
            else:
                print ("{enemy_name} took more damage than ".format(enemy_name= enemy.name) + pronouns[0] + " could handle from {self_name}. They have died.".format(self_name=self.name))
        elif self.size == enemy.size:
            print ("{enemy} and {self} have come to recognize each other as equals and have become acquainted.".format(enemy = enemy.name, self = self.name))
            self.friends[enemy.name]= enemy.job
            enemy.friends [self.name] = self.job
        else: 
            damage= int(enemy.size) - int(self.size)
            self.health -= damage
            if self.health >0:
                print ("{self} was not ready for the attack. They took ".format(self=self.name) + str(damage) + " damage. They now have " + str(self.health) + "health" )
            else:
                print ("{self} took more damage than ".format(self=self.name) + pronouns[0] + " could handle from {enemy_name}. They have died.".format(enemy_name=enemy.name))


    def talk(self, stranger, log=0):
        if self.friends.get(stranger) == None:
            if self.job.upper() == stranger.job.upper() and self.home.upper() == stranger.home.upper():
                print ("{self} and {stranger} realize they both are ".format(self=self.name, stranger=stranger.name) + self.job + "s and are from " + self.home + " and have decided to become best friends!")
                self.friends[stranger.name.title()]= [stranger.job, stranger.home]
                stranger.friends [self.name.title()] = [self.job, self.home.title()]
            elif self.job.upper() == stranger.job.upper():
                self.friends[stranger.name.title()]= [stranger.job, stranger.home]
                stranger.friends [self.name.title()] = [self.job, self.home.title()]
                print ("{self} and {stranger} realize they both are ".format(self=self.name, stranger=stranger.name) + self.job + "s and have decided to become friends!")
            elif self.home.upper() == stranger.home.upper():
                self.friends[stranger.name.title()]= [stranger.job, stranger.home]
                stranger.friends [self.name.title()] = [self.job, self. home]
                print ("{self} and {stranger} realize they both are from ".format(self=self.name, stranger=stranger.name) + self.home + " and have decided to become friends!")
            else:
                print("{self} and {stranger} don't have much in common and stand awkwardly about".format(self=self.name, stranger=stranger.name))
  # travel must be the main function consisting of different inputs that will progress the story
  #def travel(self, goal, log):

  #def clutz(self, obstacle, log):

  #def sight(self, goal, log):


#class Items: 



#class Weather: 
  #def generate_weather (self, player, obstacle, log)
  #def delay (self, player, obstacle, log)
  #def disorientate (self, player, goal, log)
  #def clear (self, player, obstacle, log)


#class Goal:
  #def __init__(self, view, distance, attribute)
  #def distance (self, player, weather, log)
  #def reroute (self, player, obstacle, weather, log)
  #def 


#class Obstacles:
  #def __init__(self, form, hazard = randint(range(11)), attack, side)
  #def damage (self, hazard, player, goal, log)
  #def appearance (self, player, weather, log)
  #def benefit (self, player, weather, log)


#class Log:
 # def __init__(self,day=0,)
  #def distance_from_goal (self, player, goal)
  #def damage (self, weather)
  #def update_history (self, weather, players, obstacle)


#player1 = Player().character_setup()
#print (player1.pronouns)
player1 = Player()
player1.character_setup()
#def start_game()