from job import Job

class Player:
  name : str = ""
  health : float = 100
  mana : float = 100
  strength : int = 100
  defense : int = 100
  effects : list = []
  stats : dict = {
    "health" : 100,
    "mana" : 100,
    "strength" : 100,
    "defense" : 100
  }
  job : Job = None

  def __init__(self, job : Job, name : str):
    self.job = job
    self.name = name
    self.stats = {
      "health" : 10
    }
    self.health = self.health * self.job.get_h_mul()
    self.mana = self.mana * self.job.get_man_mult()
    self.defense = self.defense * self.job.get_def_mult()
    self.strength = self.strength * self.job.get_str_mult()

  def add_effect(self, effect):
    pass