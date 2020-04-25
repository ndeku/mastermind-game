class Peg(object):
  "Value object which understands its color"

  def __init__(self, color):
    self.color = color

  def __eq__(self, obj):
    "Override the default implementation for value object"
    if not isinstance(obj, Peg):
      return False
    return obj.color == self.color

  def __hash__(self):
    "Override the default implementation for value object"
    return hash(self.color)

  def __str__(self):
    return str(self.color)