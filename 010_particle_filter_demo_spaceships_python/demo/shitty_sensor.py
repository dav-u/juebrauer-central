from . import World, Spaceship, SpaceshipPart
import numpy as np
import cv2 as cv

class ShittySensor:
  variance: float
  measurements_per_part: int
  wrong_measurement_count: int

  def __init__(self, variance: float = 100.0, measurements_per_part: int = 1, wrong_measurement_count: int = 10):
    self.variance = variance
    self.measurements_per_part = measurements_per_part
    self.wrong_measurement_count = wrong_measurement_count

  def measure_ships(self, world: World) -> np.ndarray:
    """Creates noisy measurements for all ships (or ship parts)
       in the specified world. Returns a [N, 2] numpy array."""
    
    ship_measurements = np.concatenate([self._measure_ship(ship) for ship in world.spaceships])
    wrong_measurements = self._create_wrong_measurements(max_pos=world.size)

    return np.concatenate((ship_measurements, wrong_measurements))

  def _measure_ship(self, ship: Spaceship):
    return np.concatenate([self._measure_part(part) for part in ship.parts])

  
  def _measure_part(self, part: SpaceshipPart) -> np.ndarray:
    return np.random.normal(loc=part.pos, scale=self.variance, size=(self.measurements_per_part, 2))

  def _create_wrong_measurements(self, max_pos: tuple[int, int]) -> np.ndarray:
    return np.random.uniform(low=(0, 0), high=max_pos, size=(self.wrong_measurement_count, 2))
  
  def draw_measurements(img: cv.Mat, measurements: np.ndarray):
    for measurement in measurements:
      cv.circle(img, center=measurement.astype('int'), radius=3, color=(0, 255, 255), thickness=-1)
