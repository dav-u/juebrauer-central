import cv2 as cv
from particle_filter.particle import Particle
from particle_filter.update_model import UpdateModel
from demo import World

import numpy as np

class ParticleFilter:
  particles: list[Particle]
  prediction_model: UpdateModel
  perception_model: UpdateModel
  world_size: tuple[int, int]

  def __init__(
      self,
      prediction_model: UpdateModel,
      perception_model: UpdateModel,
      world_size: tuple[int, int],
      particle_count: int,
      max_vel: tuple[float, float] = (1.0, 1.0)):
    self.prediction_model = prediction_model
    self.perception_model = perception_model
    self.world_size = world_size
    self.particle_count = particle_count
    self.max_vel = max_vel

    self.reset()
  
  def reset(self):
    """Deletes the old particles and creates new, random particles"""
    self.particles = []
    weight = 1.0 / self.particle_count

    for _ in range(self.particle_count):
      pos = np.random.uniform(low=(0, 0), high=self.world_size)
      vel = np.random.uniform(
        low=(-self.max_vel[0], -self.max_vel[1]), 
        high=(self.max_vel[0], self.max_vel[1]))
      
      # state consists of 4 values: (x_pos, y_pos, x_vel, y_vel)
      state = np.concatenate((pos, vel))

      self.particles.append(Particle(state, weight))
    
  def set_prediction_model(self, prediction_model: UpdateModel):
    self.prediction_model = prediction_model

  def set_perception_model(self, perception_model: UpdateModel):
    self.perception_model = perception_model

  def update(self, delta_t: float):
    for p in self.particles:
      self.prediction_model.update(p, delta_t)
      self.perception_model.update(p, delta_t)

      # limit updates to state space.
      # particle positions need to stay between (0, 0) and world size.
      # particle velocities need to stay between -vel and +vel.
      p.state = np.clip(p.state, a_min=(0, 0, -self.max_vel[0], -self.max_vel[1]), a_max=(*self.world_size, *self.max_vel))

      # TODO: weights
      # TODO: resampling

  def draw(self, img: cv.Mat):
    for p in self.particles:
      cv.circle(img, p.state[:2].astype('int'), radius=3, color=(0, 0, 255))

