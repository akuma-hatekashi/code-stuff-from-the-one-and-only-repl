import random,time,os
from time import sleep
Red = "\033[0;31m"
Green = "\033[0;32m"
White = "\033[0;37m" 
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
pink_back="\033[0;45m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
red_back="\033[0;41m"
grey_back="\033[0;40m"

sp = 0.05

def starwars1():
  print(yellow+"      _                                       ")  
  print(yellow+"  ___| |_ __ _ _ __  __      ____ _ _ __ ___  ")
  print(yellow+" / __| __/ _` | '__| \ \ /\ / / _` | '__/ __| ")
  print(yellow+" \__ \ || (_| | |     \ V  V / (_| | |  \__ \ ")
  print(yellow+" |___/\__\__,_|_|      \_/\_/ \__,_|_|  |___/ ")
  print(yellow+"               FIGHT SIMULATOR                ")
  print("                                        ")
  print(yellow+"                 by @FloCal35                 ")

def victor():
  print(yellow+ " **    **                    **       ** **         ")
  print(blue+   "//**  **                    /**      /**//          ")
  print(yellow+ " //****    ******  **   **  /**   *  /** ** ******* ")
  print(blue+   "  //**    **////**/**  /**  /**  *** /**/**//**///**")
  print(yellow+ "   /**   /**   /**/**  /**  /** **/**/**/** /**  /**")
  print(blue+   "   /**   /**   /**/**  /**  /**** //****/** /**  /**")
  print(yellow+ "   /**   //****** //******  /**/   ///**/** ***  /**")
  print(blue+   "   //     //////   //////   //       // // ///   // ")

def defeat():
  print(red+"'||' '|'                     '||''|.    ||               '||  ")
  print(red+"  || |     ...   ... ...      ||   ||  ...    ....     .. ||  ")
  print(red+"   ||    .|  '|.  ||  ||      ||    ||  ||  .|...||  .'  '||  ")
  print(red+"   ||    ||   ||  ||  ||      ||    ||  ||  ||       |.   ||  ")
  print(red+"  .||.    '|..|'  '|..'|.    .||...|'  .||.  '|...'  '|..'||. ")

bad_sym=Red+'[X]'+White
good_sym=Green+'[+]'+White
even_sym=cyan+'[*]'+White
aten_sym=yellow+'[!]'+White

def clear():
  os.system("clear")

h1=green+"=========="
h2=green+"========="
h3=green+"========"
h4=green+"======="
h5=yellow+"======"
h6=yellow+"====="
h7=yellow+"===="
h8=red+"==="
h9=red+"=="
h10=red+"="
h11=red+""

s1=cyan+"=========="
s2=cyan+"========="
s3=cyan+"========"
s4=cyan+"======="
s5=cyan+"======"
s6=cyan+"====="
s7=cyan+"===="
s8=cyan+"==="
s9=cyan+"=="
s10=cyan+"="
s11=cyan+""

a0=magenta+"Infinite"
a1=magenta+"=========="
a2=magenta+"========="
a3=magenta+"========"
a4=magenta+"======="
a5=magenta+"======"
a6=magenta+"====="
a7=magenta+"===="
a8=magenta+"==="
a9=magenta+"=="
a10=magenta+"="
a11=magenta+""

class human:
  def __init__ (self, health, shield, weapon):
    self.health=health
    self.shield=shield
    self.weapon=weapon
  def show_hp(self):
    if self.health > 90:
      hlth=h1
    elif self.health > 80 and self.health < 91:
      hlth=h2
    elif self.health > 70 and self.health < 81:
      hlth=h3
    elif self.health > 60 and self.health < 71:
      hlth=h4
    elif self.health > 50 and self.health < 61:
      hlth=h5
    elif self.health > 40 and self.health < 51:
      hlth=h6
    elif self.health > 30 and self.health < 41:
      hlth=h7
    elif self.health > 20 and self.health < 31:
      hlth=h8
    elif self.health > 10 and self.health < 21:
      hlth=h9
    elif self.health > 0 and self.health < 11:
      hlth=h10
    else:
      hlth=h11
    print(Green+"| Total Health:  "+hlth+"|  "+str(self.health)+white)
    if self.shield > 90:
      sld=s1
    elif self.shield > 80 and self.shield < 91:
      sld=s2
    elif self.shield > 70 and self.shield < 81:
      sld=s3
    elif self.shield > 60 and self.shield < 71:
      sld=s4
    elif self.shield > 50 and self.shield < 61:
      sld=s5
    elif self.shield > 40 and self.shield < 51:
      sld=s6
    elif self.shield > 30 and self.shield < 41:
      sld=s7
    elif self.shield > 20 and self.shield < 31:
      sld=s8
    elif self.shield > 10 and self.shield < 21:
      sld=s9
    elif self.shield > 0 and self.shield < 11:
      sld=s10
    else:
      sld=s11
    print(cyan+"| Total Shield:  "+sld+"|  "+str(self.shield)+white)

class match:
  def __init__ (self, kills, left):
    self.kills=kills
    self.left=left
  def show(self):
    print(yellow+"Your kills--  "+blue+str(game.kills)+yellow+"    Total people left--  "+blue+str(game.left))
class weapon:
  def __init__ (self, name, dam, ammo, gain, accuracy, colo):
    self.name=name
    self.dam=dam
    self.ammo=ammo
    self.gain=gain
    self.accuracy=accuracy
    self.colo=colo
  def show_weapon(self):
    print(self.colo+"["+self.name+"]")
  def show_ammo(self):
    if self.ammo > 100000:
      bar=a0
    elif self.ammo > 90:
      bar=a1
    elif self.ammo > 80 and self.ammo < 91:
      bar=a2
    elif self.ammo > 70 and self.ammo < 81:
      bar=a3
    elif self.ammo > 60 and self.ammo < 71:
      bar=a4
    elif self.ammo > 50 and self.ammo < 61:
      bar=a5
    elif self.ammo > 40 and self.ammo < 51:
      bar=a6
    elif self.ammo > 30 and self.ammo < 41:
      bar=a7
    elif self.ammo > 20 and self.ammo < 31:
      bar=a8
    elif self.ammo > 10 and self.ammo < 21:
      bar=a9
    elif self.ammo > 0 and self.ammo < 11:
      bar=a10
    else:
      bar=a11
    if self.ammo > 100000:
      print(magenta+"| Total Ammo:  "+bar+" |  "+white)
    else: 
      print(magenta+"| Total Ammo:  "+bar+"|  "+str(self.ammo)+white)


fist=weapon("Fist",5,110e11,2,2,grey_back)
knife=weapon("Knife",8,110e11,2,2,grey_back)
shovel=weapon("Shovel",7,110e11,2,2,grey_back)
rocks=weapon("Some rocks",14,110e11,2,2,grey_back)
stick=weapon("Wood Stick",6,110e11,2,2,grey_back)
spear=weapon("Spear",20,110e11,2,2,grey_back)
staff=weapon("Staff",20,110e11,2,2,grey_back)
slingshot=weapon("Slingshot",10,5,10,2,grey_back)
STW48=weapon("ST-W48 Blaster",50,100,2,7,blue_back)
A180=weapon("A180 (Pistol mode)",20,50,2,7,grey_back)
A180D=weapon("A180D (Repeating Blaster mode)",25,100,10,3,grey_back)
ELG=weapon("ELG-3A Pistol",10,50,2,5,grey_back)
SE44=weapon("SE-44C Pistol",10,50,2,5,grey_back)
RT97=weapon("RT-97C Heavy Blaster Rifle",35,100,10,3,grey_back)
FWMB=weapon("FWMB-10 Repeating Blaster",25,100,10,3,grey_back)
EL16=weapon("EL-16 Blaster Rifle",20,100,7,2,grey_back)
EC17=weapon("EC-17 Hold Out Blaster",10,110e11,2,1,grey_back)
DL44=weapon("DL-44 (Han blaster)",30,25,5,2,grey_back)
DC17=weapon("Dual DC-17 blaster pistols",30,100,20,2,blue_back)
DC15S=weapon("DC-15S Blaster",20,100,7,2,grey_back)
DC15=weapon("DC-15 Blaster Rifle",20,100,7,2,grey_back)
E11=weapon("E-11 Blaster",20,100,7,2,grey_back)
E11D=weapon("E-11D CQC Gun",10,50,2,2,grey_back)
dagger=weapon("Dagger",10,110e11,2,2,grey_back)
DH17=weapon("DH-17 Pistol",10,50,2,2,grey_back)
M45=weapon("M-45 Heavy Repeating Blaster",25,100,10,3,blue_back)
RK3=weapon("RK-3 Blaster Pistol",10,25,2,2,grey_back)
A280=weapon("A280 Blaster Rifle",20,100,7,2,grey_back)
E5=weapon("E-5 Blaster",20,100,7,2,grey_back)
#self, name, dam, ammo, gain, accuracy, colo

starwarsweapons=[fist,knife,shovel,rocks,stick,spear,staff,STW48,A180,A180D,slingshot,ELG,SE44,RT97,FWMB,EL16,EC17,DL44,DC17,DC15S,DC15,E11,E11D,dagger,DH17,M45,RK3,A280,E5]











def fight():
  print("Someone found you!! They are looking to fight!")
  input()
  th=human(random.randrange(1,100),random.randrange(0,100),random.choice(starwarsweapons))
  while True:
    if you.weapon.ammo < 0:
      you.weapon.ammo=0
    clear()
    print(pink_back+"Your Stats:")
    you.show_hp()
    print("")
    you.weapon.show_weapon()
    you.weapon.show_ammo()
    print(red_back+"\n\nTheir Stats")
    th.show_hp()
    print("")
    th.weapon.show_weapon()
    th.weapon.show_ammo()
    do=input(white+"\n\nYou can attack or run\n[1] Attack\n[2] Run\n> ")
    clear()
    if do=="1":
      clear()
      print("You attacked them!")
      da=random.randrange(1,you.weapon.dam)
      if you.weapon.ammo <= 0:
        you.weapon.ammo=0
        da=0
      if da==0:
        print(bad_sym+"You are out of ammo!")
      print(good_sym+"It did "+str(da)+" damage!")
      ska=random.randrange(1,4)
      print(aten_sym+"You used "+str(ska)+" ammo!")
      you.weapon.ammo-=ska
      if th.shield <= 0:
        th.health-=da
      else:
        th.shield-=da
      if th.shield < 0:
        th.shield=0
      if th.health <=0:
        th.health=0
        game.left-=1
        game.kills+=1
        print(good_sym+"You won the fight!")
        input()
        while True:
          clear()
          print(blue_back+"They dropped a "+th.weapon.name)
          print(cyan+"[1] Take it")
          print("[2] Leave it")
          d=input(white+"> ")
          if d=="1":
            print("You took the weapon")
            you.weapon=th.weapon
            break
          if d=="2":
            break
        break
      input()
      print("\n\nThey attacked you!")
      pa=random.randrange(1,th.weapon.dam)
      print(bad_sym+"It did "+str(pa)+" damage!")
      if you.shield <= 0:
        you.health-=pa
      else:
        you.shield-=pa
      if you.health <=0:
        print("You lost the fight!")
        break
      if you.shield <0:
        you.shield=0
      input()
    if do=="2":
      print("They attacked you as you ran away")
      pa=random.randrange(1,th.weapon.dam)
      print(bad_sym+"It dealt "+str(pa)+" damage!")
      input()
      if you.shield > 0:
        you.shield-=pa
      else:
        you.health-=pa
      if you.shield<=0:
        you.shield=0
      break



starwars1()
time.sleep(5)

input(blue+"\nWelcome to the Star Wars Fight Simulator sneak peek by @FloCal35. In this game, you be given a random weapon within the Star Wars universe to fight an AI and WIN!\nPlease note that this is only a sneak peek and that the final project will look differantly\n\n[Press ENTER to continue] ")
clear()
pp=2
game=match(0,pp)
you=human(100,0,random.choice(starwarsweapons))

while you.health > 0 and game.left > 1:
  clear()
  game.show()
  print("\n")
  you.weapon.show_weapon()
  you.weapon.show_ammo()
  print("")
  you.show_hp()
  d=input(blue_back+"\n\nWhat will you do?"+green+"\n\n[1] Look for loot\n[2] Camp\n"+yellow+"> ")
  clear()
  if d=="2":
    print("You bushed camped")
    input()
    if game.left > 11:
      bb=random.randrange(1,10)
      if bb==1 or bb==2 or bb==3:
        game.left-=random.randrange(1,5)
      if bb==2:
        fight()
      clear()
  if game.left > 10:
    try:
      ch=random.randrange(1,(110-game.left))
    except:
      ch=random.randrange(1,10)
  elif game.left <=10:
    ch=random.randrange(1,10)
  if ch==2:
    fight()
  if ch==1 or ch==2 or ch==3:
    if game.left > 3:
      try:
        if game.left > 11:
          game.left-=random.randrange(1,10)
        elif game.left <= 11:
          game.left-=3
      except:
        game.left-=1
  if d=="1":
    print(white+"You checked for loot")
    snk=random.randrange(1,7)
    if snk==1:
      print("You found ammo!")
      sj=random.randrange(1,you.weapon.gain)
      print("You found "+str(sj)+' bullets!')
      you.weapon.ammo+=sj
      input()
    elif snk==2:
      print("You found shield!!")
      buss=[5,25,50]
      bul=random.choice(buss)
      if you.shield < 100:
        you.shield+=bul
        if you.shield>100:
          you.shield=100
      input()
    elif snk==4:
      print(white+"You found a weapon!!")
      input()
      we_fou=random.choice(starwarsweapons)
      while True:
        clear()
        print(blue_back+"The weapon is a "+we_fou.name)
        print(cyan+"[1] Take it")
        print("[2] Leave it")
        c=input(white+"> ")
        if c=="1":
          you.weapon=we_fou
          print(good_sym+"You took the weapon!")
          you.weapon.ammo+=you.weapon.gain
          input()
          break
        if c=="2":
          break
    else:
      print("You found nothing!")
      input()
else:
  clear()
  if you.health > 0:
    victor()
    print(red_back+"You had "+str(game.kills)+" kills!")
  else:
    defeat()
    print("You came in "+str(game.left)+"(th) place!")
    print("You had "+str(game.kills),"kills!")
    os.system("python credits.py")
