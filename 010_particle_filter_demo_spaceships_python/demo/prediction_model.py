from particle_filter import UpdateModel, Particle
import numpy as np

class PredictionModel(UpdateModel):
  def update(self, p: Particle, delta_t: float):
    p_pos = p.get_pos()
    p_vel = p.get_vel()

    p_pos += p_vel

    p_pos += np.random.uniform(low=(-5.0, -5.0), high=(5.0, 5.0))
    p_vel += np.random.uniform(low=(-0.1, -0.1), high=(0.1, 0.1))

    p.set_pos(p_pos)
    p.set_vel(p_vel)