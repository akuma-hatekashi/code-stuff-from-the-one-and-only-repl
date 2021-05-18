#/bin/python3
import random, time
from player import Player

## Child Classes (special players)


##############################################
########### Child Classes ####################
##############################################


# Spiderman class
class Spiderman(Player): # create child class of Player
  def __init__(self):
    Player.__init__(self, "Spiderman") # use __init__ method from Player
    self.moves["web shooter"] = self.web_shooter # add new move to dictionary
    self.moves["face punch"] = self.face_punch
    self.moves["flying kick"] = self.flying_kick
    self.moves["think"] = self.think

  def web_shooter(self, enemy): # new special move for child class
    self.attack(enemy, random.randint(40, 50))
  
  def face_punch(self, enemy):
    damage = random.randint(30, 45)
    self.attack(enemy, damage)
  
  def flying_kick(self, enemy):
    if random.random() <= 0.75:
      damage = random.randint(35, 40)
      self.attack(enemy, damage)
    else:
      print("Spiderman didn't do a good kick...")
      time.sleep(1)
      damage = random.randint(20, 25)
      self.attack(enemy, damage)
  
  def think(self, enemy):
    self.energy += 0.15
    print(self.name + " has increased energy.")
    if self.energy >= 2: # if energy gets too high...
      self.moves.pop("think") # remove from dictionary of possible moves


# Pikachu class
class Pikachu(Player):
  def __init__(self):
    Player.__init__(self, "Pikachu")
    self.moves["thunder shock"] = self.thunder_shock
    self.moves["tail slap"] = self.tail_slap
    self.moves["pika block"] = self.pika_block
    self.moves["evolve"] = self.evolve
    self.specialmove = 2

# special move:
  def thunder_shock(self, enemy):
    damage = random.randint(40, 50)
    self.attack(enemy, damage)
    if random.random() <= 0.5: # 50% chance of lowering own health
      self.attack(self, 10)
  
  def tail_slap(self, enemy):
    self.attack(enemy, 35)
  
  def pika_block(self, enemy): # blocks 25 of enemy's attack
    print("Pikachu will get 20 health to block some of the enemy's attack.")
    self.health += 20
    time.sleep(1)
    self.attack(enemy, random.randint(30, 45))
  
  def evolve(self, enemy):
    self.name = "Raichu"
    self.health = 100
    print("Pikachu evolving ...")
    time.sleep(1)
    print("Pikachu evolved to Raichu!")
    self.moves.pop("thunder shock")
    self.moves.pop("tail slap")
    self.moves.pop("pika block")
    self.moves.pop("evolve")
    self.moves["thunder punch"] = self.thunder_punch
    self.moves["wild charge"] = self.wild_charge
    self.moves["raichu block"] = self.raichu_block
    self.moves["unevolve"] = self.unevolve
    self.specialmove1 = 2
  
  def thunder_punch(self, enemy):
    self.attack(enemy, random.randint(45, 50))
  
  def wild_charge(self, enemy):
    self.attack(enemy, random.randint(40, 50))
  
  def raichu_block(self, enemy):
    print("Raichu will get 25 health to block some of the attacks.")
    self.health += 25
    time.sleep(1)
    self.attack(enemy, random.randint(30, 45))
  
  def unevolve(self, enemy):
    self.name = "Pikachu"
    self.health = 100
    print("Raichu unevolved to Pikachu.")
    self.moves.pop("thunder punch")
    self.moves.pop("wild charge")
    self.moves.pop("raichu block")
    self.moves.pop("unevolve")
    self.moves["thunder shock"] = self.thunder_shock
    self.moves["tail slap"] = self.tail_slap
    self.moves["pika block"] = self.pika_block
    self.moves["evolve"] = self.evolve


# Hercules class
class Hercules(Player):
  def __init__(self):
    Player.__init__(self, "Hercules")
    self.moves["arrow shots"] = self.arrow_shots
    self.moves["club strike"] = self.club_strike
    self.moves["equalize healths"] = self.equalize_healths

  def arrow_shots(self, enemy):
    if random.random() <= 0.75:
      self.attack(enemy, random.randint(40, 45))
    else:
