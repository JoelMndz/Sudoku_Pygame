import pygame

class Button:
  def __init__(self, screen:pygame.Surface, text, width, height, pos, font) -> None:
    self.screen = screen
    self.color = (255,140,0)
    self.screen_rec = self.screen.get_rect()
    self.width = width
    self.height = height
    self.text_color = (255,255,255)

    self.rect = pygame.Rect(pos[0],pos[1],self.width,self.height)
  
    self.texto_image = font.render(text,True,self.text_color,self.color)
    self.texto_image_rect = self.texto_image.get_rect()
    self.texto_image_rect.center = self.rect.center

  def draw(self):
    self.screen.fill(self.color, self.rect)
    self.screen.blit(self.texto_image,self.texto_image_rect)
