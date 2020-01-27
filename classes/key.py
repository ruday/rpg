import keyboard
from .character import Person

class KeyEvent:
  def __init__(self):
    self.pause = pause
    self.quit = quit
    self.up = up
    self.down = down
    self.left = left
    self.right = right
    self.perso = perso

  def go_menu_user(self):
    while True:
      try:
        if keyboard.is_pressed('esc'):
          print("You pressed Escape")
          break
      except:
        break

  def go_pause(self):
    keyboard.wait('space')

  def go_inventory(self):
    keyboard.wait('i')
