import pygame

class Cell:
  def __init__(self, value, row, col, screen:pygame.Surface) -> None:
    self.value = value
    self.__row = row
    self.__col = col
    self.__screen = screen
    self.sketched = 0
    self.static = value != 0
    self.selected = False
  
  def set_cell_value(self, value):
    if not self.static:
      self.value = value

  def set_sketched_value(self, value):
    if not self.static:
      self.sketched = value

  def draw(self):
    font = pygame.font.SysFont("comicsans", 40)
    width,height =self.__screen.get_size()
    gap = width / 9
    x = self.__col * gap
    y = self.__row * gap

    if self.value != 0:
      text = font.render(str(self.value), 1, (0,0,0))
      self.__screen.blit(text,(x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
    elif self.sketched != 0:
      text = font.render(str(self.sketched), 1, (128, 128, 128))
      self.__screen.blit(text,(x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
    
    if self.selected and not self.static:
      pygame.draw.rect(self.__screen, (255,0,0), (x,y, gap ,gap), 3)
  