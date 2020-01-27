from threading import Thread
import fileinput


class ecrire(Thread):
  def __init__(self, lettre):
    Thread.__init__(self)
    self.lettre = lettre


  def run(self):
    for line in fileinput.input():
      pass
    sys.stdout.write(self.lettre)


class lire(Thread):
  def __init__(self, lettre):
    Thread.__init__(self)
    self.lettre = lettre

  def run(self):
    f = ope


def main():
  exit_coomand = "exit"


if (__name__ == '__main__'):
  main()

