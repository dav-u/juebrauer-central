import numpy as np

class Particle:
  def __init__(self, state: np.ndarray , weight: float) -> None:
    """state is a numpy array with 4 entries [x_pos, y_pos, x_vel, y_vel]"""
    self.state = state
    self.weight = weight
  
  def get_pos(self):
    return self.state[:2].copy()

  def set_pos(self, pos: np.ndarray):
    self.state[:2] = pos

  def get_vel(self):
    return self.state[2:].copy()

  def set_vel(self, vel: np.ndarray):
    self.state[2:] = vel