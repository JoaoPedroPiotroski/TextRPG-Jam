from json import loads

class Job:
  name : str
  data = None

  def __init__(self, name : str):
    self.name = name
    with open("classes.json") as f:
      content = f.read()
      self.data = loads(content)[self.name]

  def get_h_mult(self) -> float:
    return self.data["health_mul"]
  def get_man_mult(self) -> float:
    return self.data["mana_mul"]
  def get_str_mult(self) -> float:
    return self.data["strength_mul"]
  def get_def_mult(self) -> float:
    return self.data["defense_mul"]
  def get_available_skills(self) -> list:
    return self.data["available_skills"]







