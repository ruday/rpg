#Importation des classes
from classes.magic import Spell
from classes.character import Person, bcolors
from classes.inventory import Item
from classes.options import *
from classes.key import *
from classes.sauvegarde import *
from classes.file_management import fileExec
import os, sys, time


#player list of things
player_spells = []
player_items = []

#enemy list of things
enemy_spells = []
enemy_items = []

#INSTANTIATE PEOPLE
php = 1
pmp = 1
patk = 1
pdf = 1

player1 = Person("hero: ", php , pmp, patk, pdf, player_spells, player_items)

#instantiate enemy
ehp = 1
emp = 1
eatk = 1
edf = 1

enemy = Person("", ehp, emp, eatk, edf, enemy_spells, enemy_items)
#multiple user
players = [player1]

#multiple enemy
enemies = [enemy]


####################################################################################################

#Menu debut du jeu
answers = inquirer.prompt(Menu_main)
if answers["main"] == "START":
  running = True
  i = 0
  while running:
    storyline = fileExec("texte/story.txt")
    storyline.l_fileExec("texte/story.txt")
    running = False
#reprendre la partie
elif answers["main"] == "Continue":
  print("now loading")
else:
  sys.exit()
