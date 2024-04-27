import demo.spaceship as spaceship
import cv2 as cv

class World:
  spaceships: list[spaceship.Spaceship]

  def __init__(self, size: tuple[int, int]) -> None:
    self.size = size
    self.spaceships = []
  
  def add_spaceship(self, spaceship: spaceship.Spaceship):
    self.spaceships.append(spaceship)
  
  def update(self, delta_t: float):
    for ship in self.spaceships:
      ship.update(self.size, 1.0)
  
  def draw(self, img: cv.Mat):
    for ship in self.spaceships:
      ship.draw(img)