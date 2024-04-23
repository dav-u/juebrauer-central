from spaceship import Spaceship
from world import World
import cv2 as cv

if __name__ == '__main__':
  background_img_filename = 'pics/earth_orbit.jpg'
  background_img = cv.imread(background_img_filename)

  enemy_ship = Spaceship(pos=(100, 100), part_count=5)
  world = World(background_img.shape[:2]) # make the world as big as our image

  is_paused = False
  while True:
    image = background_img.copy()

    enemy_ship.update(world, delta_t=1.0)
    enemy_ship.draw(image)

    cv.imshow('Tracking an alien spaceship with a particle filter!', image)

    key = cv.waitKey(0 if is_paused else 10)
    if key == ord('x'): break
    if key == ord(' '): is_paused = not is_paused