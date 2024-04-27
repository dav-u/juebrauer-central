from particle_filter import UpdateModel, Particle
import numpy as np

class MeasurementModel(UpdateModel):
  measurements: np.ndarray
  move_to_measurement_speed: int

  def __init__(self, move_to_measurement_speed: int = 0.05):
    super().__init__()
    self.move_to_measurement_speed = move_to_measurement_speed
    self.measurements = np.array([])

  def set_measurements(self, measurements: np.ndarray):
    """measurements are pairs of [x, y] coordinates.
       measurements needs to be a 2d numpy array of shape (N, 2)."""
    self.measurements = measurements.copy()

  def update(self, p: Particle, delta_t: float):
    if len(self.measurements.shape) != 2 or self.measurements.shape[1] != 2:
      raise Exception("Before calling update() call set_measurements(). Measurements need to have shape (N, 2)")

    p_pos = p.get_pos()
    p_vel = p.get_vel()

    # find the point in measurements that is closest
    # to p_pos (our particle position)
    closest_measurement = self._closest_measurement_to(p_pos)

    direction = closest_measurement - p_pos

    # update position in direction of nearest measurement
    pos_update = direction * self.move_to_measurement_speed
    p_pos += pos_update

    # pos_update is change in position => pos_update/time is estimate for velocity
    p_vel += pos_update / delta_t

    # measured_vel = direction / delta_t
    # p_vel += measured_vel * self.move_to_measurement_speed

    p.set_pos(p_pos)
    p.set_vel(p_vel)

  def _closest_measurement_to(self, pos: np.ndarray):
    """finds the closest measurement to the provided pos [x, y]"""

    # get the index of the measurement that has the lowest
    # squared distance (lowest squared distance => lowest distance)
    dists_squared = np.sum((self.measurements - pos)**2, axis=1)
    index = np.argmin(dists_squared)
    
    return self.measurements[index]
