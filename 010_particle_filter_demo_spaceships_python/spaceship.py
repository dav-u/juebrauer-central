import cv2 as cv
import numpy as np
from world import World

class SpaceshipPart:
  WIDTH = 20
  HEIGHT = 20

  def __init__(self, pos: tuple[float, float], vel: tuple[float, float]):
    self.pos = pos
    self.vel = vel
  
  def draw(self, img: cv.Mat):
    top_left_corner = (int(self.pos[0]) - SpaceshipPart.WIDTH//2,
                       int(self.pos[1]) - SpaceshipPart.HEIGHT//2)
    bottom_right_corner = (int(self.pos[0]) + SpaceshipPart.WIDTH//2,
                           int(self.pos[1]) + SpaceshipPart.HEIGHT//2)

    cv.rectangle(img, np.array(top_left_corner), bottom_right_corner, color=(0, 255, 0), thickness=-1)
    cv.rectangle(img, top_left_corner, bottom_right_corner, color=(0, 178, 0), thickness=2)
  
  def update(self, world: World, delta_t: float):
    if np.random.uniform(low=0.0, high=100.0) <= 5.0:
      self.randomize_velocity()

    # move pos in direction of velocity
    self.pos = (self.pos[0] + self.vel[0] * delta_t,
                self.pos[1] + self.vel[1] * delta_t)

    # bounce of walls
    new_pos = np.clip(self.pos, (0, 0), world.size)
    if self.pos[0] != new_pos[0]: self.vel = (self.vel[0] * -1, self.vel[1])
    if self.pos[1] != new_pos[1]: self.vel = (self.vel[0], self.vel[1] * -1)

    self.pos = tuple(new_pos)

  def randomize_velocity(self):
    vel_x = np.random.choice([-1.0, 0.0, 1.0])
    vel_y = np.random.choice([-1.0, 0.0, 1.0])

    self.vel = (vel_x, vel_y)

class Spaceship:
  pos: tuple[float, float]
  parts: list[SpaceshipPart]

  def __init__(self, pos: tuple[float, float], part_count: int = 0):
    self.parts = []
    for i in range(part_count):
      part_pos = (pos[0] + SpaceshipPart.WIDTH*i, pos[1])
      part = SpaceshipPart(part_pos, vel=(0, 0))
      self.parts.append(part)
  
  def update(self, world: World, delta_t: float):
    for part in self.parts:
      part.update(world, delta_t)

  def draw(self, img: cv.Mat):
    for part in self.parts:
      part.draw(img)