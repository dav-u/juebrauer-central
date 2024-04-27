from particle_filter import ParticleFilter, UpdateModel
from demo import PredictionModel, MeasurementModel, Spaceship, World, ShittySensor
import cv2 as cv
import numpy as np

if __name__ == '__main__':
  background_img_filename = 'pics/earth_orbit.jpg'
  background_img = cv.imread(background_img_filename)

  enemy_ship = Spaceship(pos=(100, 100), part_count=5)
  world = World(background_img.shape[:2]) # make the world as big as our image
  world.add_spaceship(enemy_ship)

  prediction_model = PredictionModel()
  measurement_model = MeasurementModel()
  particle_filter = ParticleFilter(prediction_model, measurement_model, world.size, particle_count=1000)
  sensor = ShittySensor(variance=10.0, measurements_per_part=10, wrong_measurement_count=10)

  is_paused = False
  while True:
    image = background_img.copy()

    world.update(delta_t=1.0)

    measurements = sensor.measure_ships(world)
    measurement_model.set_measurements(measurements)

    particle_filter.update(delta_t=1.0)

    enemy_ship.draw(image)
    particle_filter.draw(image)
    ShittySensor.draw_measurements(image, measurements)

    cv.imshow('Tracking an alien spaceship with a particle filter!', image)

    key = cv.waitKey(0 if is_paused else 10)
    if key == ord('x'): break
    if key == ord(' '): is_paused = not is_paused