import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

while True:
  # check for all events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() # close window
      print('pygame End')
      quit() # end pygame
