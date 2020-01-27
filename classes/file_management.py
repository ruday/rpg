import time

class fileExec:
  def __init__(self, path):
    self.path = path
    self.ecrire = ""
    self.lire = ""
    self.pause = ""
    self.flag = ""
    
  def l_fileExec(self, path):
    with open(path, "r+") as f:
      for line in f:
        print(line)
        time.sleep(4)
        print("...")
 
  
