import random,time,os
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
blue_back="\033[0;44m"
orange_back="\033[0;43m"
red_back="\033[0;41m"
grey_back="\033[0;40m"

def clear():
  os.system("clear")

print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......... ")
print(red+"   ......"+white+".-~|")
print(red+"   ....."+white+"/   |")
print(" =============")
print("  |         |")
print("  |         |")
print("  |         |")
print("  \---------/")
print("   )-------(")
print("   (-------)")
print("   )-------(")
print("   (-------)")
print("   )-------(")
print("   (-------)")
print("   )-------(--+")
print("  /---------\ |")
print("  | | | | | | |")
print("  |  "+yellow+"STAR"+white+"   | |")
print("  |  "+yellow+"WARS"+white+"   | |")
print("  |         |-+")
print("  | "+yellow+" B   C "+white+" |")
print("  | "+yellow+" A   E "+white+" |")
print("  | "+yellow+" T   N "+white+" |")
print("  | "+yellow+" T   T "+white+" |")
print("  | "+yellow+" L   E "+white+" |")
print("  | "+yellow+" E   R "+white+" |")
print("  |         |")
print("  | | | | | |")
print("  |_|_|_|_|_|")














input()
clear()
print(red+"Hello there! For the best experience, please\nopen this in a new tab and make sure\nthe console is full screen (in spotlight) or else the\nASCII animation (made by me) will look wierd\n\n[NOTE: It seems like there's an audio issue\non spotlight pages so I had to remove the music, sorry]\n\n"+red_back+"[Press ENTER to continue]"+White)
input("")
clear()
print(red+"Choose Your Mode!"+white+"\nFight Sim full version "+green+"(full)"+white+"\nFight Sim beta version "+green+"(beta)"+white+"\nEwok Hunt "+green+"(ewok)"+white+"\nClone Trooper RPG"+green,"(clone)\n"+white+"Test your knowledge"+green,"(quiz)"+white+"\nGalaxy At War sneak peek",(green)+"(GAW)")
print(white+"________________________")
game=input(white+"(type whatever's in green)\n>").lower()
if game=="ewok":
  clear()
  os.system("python ewokhunt.py")
elif game=="beta":
  clear()
  os.system("python beta.py")
elif game=="credits":
  clear()
  os.system("python credits.py")
elif game=="full":
  clear()
  os.system("python full.py")
elif game=="quiz":
  clear()
  os.system("python quiz.py")
elif game=="gaw":
  clear()
  os.system("python GAWAnimate.py")
  clear()
  print(magenta+"Choose your faction")
  print(yellow+" 1. New Republic")
  print(red+" 2. Galactic Empire")
  fac=input(white+">")
  if fac=="1":
    clear()
    os.system("python GAWNR.py")
  elif fac=="2":
    clear()
    os.system("python GAWGE.py")
  else:
    print(red+"Error, please try again")
else:
  clear()
  os.system("python CloneTrooper.py")
