import sys, pygame
from board import Board
from button import Button

def main():
  pygame.init()
  size = width, height = 600, 700
  BLACK = (0,0,0)
  WHITE = (255,255,255)
  BLUE = (158,222,232)
  time = pygame.time.Clock()
  play = False
  win = False
  over = False
  key = None
  screen = pygame.display.set_mode(size)
  backgroung_image = pygame.image.load("fondo.jpg").convert()
  pygame.display.set_caption('Sudoku') 
  font = pygame.font.Font(None, 30)
  button_easy = Button(screen,"EASY",100,40,(100,350),font)
  button_medium = Button(screen,"MEDIUM",100,40,(250,350),font)
  button_hard = Button(screen,"HARD",100,40,(400,350),font)

  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          if play:
            clicked = board.click(mousePos[0],mousePos[1])
            if clicked:
              board.select(clicked[0],clicked[1])
              key = None
            if button_reset.rect.collidepoint(mousePos):
              board.reset_to_original()  
            elif button_restart.rect.collidepoint(mousePos):
              board.generator_matrix()  
            elif button_exit.rect.collidepoint(mousePos):
              play = False 
          elif win:
            if button_exit.rect.collidepoint(mousePos):
              win = False 
          elif over:
            if button_restart.rect.collidepoint(mousePos):
              over = False
              play = True 
              button_restart = Button(screen, 'RESTART',100,40,(250,650),pygame.font.Font(None, 30))
              board.generator_matrix()  
          else:
            if button_easy.rect.collidepoint(mousePos):
              play = True
              board = Board(width,height-100, screen,"easy")
              button_reset = Button(screen, 'RESET',100,40,(100,650),pygame.font.Font(None, 30))
              button_restart = Button(screen, 'RESTART',100,40,(250,650),pygame.font.Font(None, 30))
              button_exit = Button(screen, 'EXIT',100,40,(400,650),pygame.font.Font(None, 30))
            elif button_medium.rect.collidepoint(mousePos):
              play = True
              board = Board(width,height-100, screen,"medium") 
              button_reset = Button(screen, 'RESET',100,40,(100,650),pygame.font.Font(None, 30))
              button_restart = Button(screen, 'RESTART',100,40,(250,650),pygame.font.Font(None, 30))
              button_exit = Button(screen, 'EXIT',100,40,(400,650),pygame.font.Font(None, 30))
            elif button_hard.rect.collidepoint(mousePos):
              play = True
              board = Board(width,height-100, screen,"hard") 
              button_reset = Button(screen, 'RESET',100,40,(100,650),pygame.font.Font(None, 30))
              button_restart = Button(screen, 'RESTART',100,40,(250,650),pygame.font.Font(None, 30))
              button_exit = Button(screen, 'EXIT',100,40,(400,650),pygame.font.Font(None, 30))
        elif event.type == pygame.KEYDOWN and play:
          if event.key == pygame.K_0:
            key = 0
          if event.key == pygame.K_1:
            key = 1
          if event.key == pygame.K_2:
            key = 2
          if event.key == pygame.K_3:
            key = 3
          if event.key == pygame.K_4:
            key = 4
          if event.key == pygame.K_5:
            key = 5
          if event.key == pygame.K_6:
            key = 6
          if event.key == pygame.K_7:
            key = 7
          if event.key == pygame.K_8:
            key = 8
          if event.key == pygame.K_9:
            key = 9
          if event.key == pygame.K_DELETE:
            board.clear()
            key = None
          if event.key == pygame.K_RETURN:
            if board.selected != None:
              row,col = board.selected
              if board.cells[row][col].sketched != 0:
                board.place_number(board.cells[row][col].sketched)
                key = None

                if board.check_board():
                  win = True
                  play = False
                  button_exit = Button(screen, 'EXIT',100,40,(250,250),pygame.font.Font(None, 40))
                  print('GANÓ!!')
                if board.is_full() and not win:
                  over = True
                  play = False
                  button_restart = Button(screen, 'RESTART',150,50,(250,250),pygame.font.Font(None, 40))
                  print('PERDIÓ!!')

    #Pintar pantalla

    if not play and not win and not over:
      screen.fill(WHITE)
      screen.blit(backgroung_image,[0,0])
      font = pygame.font.Font(None, 70)
      text = font.render("Welcome to Sudoku", 1, BLACK)
      textpos = text.get_rect()
      textpos.centerx = screen.get_rect().centerx
      textpos.y = 100
      screen.blit(text, textpos)

      font = pygame.font.Font(None, 40)
      text = font.render("Select Game Mode:", 1, BLACK)
      textpos = text.get_rect()
      textpos.centerx = screen.get_rect().centerx
      textpos.y = 250
      screen.blit(text, textpos)
      button_easy.draw()
      button_medium.draw()
      button_hard.draw()

    elif play:
      if board.selected and key != None:
        board.sketch(key)
      screen.fill(BLUE)
      board.draw()

      button_reset.draw()
      button_restart.draw()
      button_exit.draw()
    elif win:
      screen.fill(WHITE)
      screen.blit(backgroung_image,[0,0])
      font = pygame.font.Font(None, 100)
      text = font.render("Game Won!", 1, BLACK)
      textpos = text.get_rect()
      textpos.centerx = screen.get_rect().centerx
      textpos.y = 150
      screen.blit(text, textpos)

      button_exit.draw()

    elif over:
      screen.fill(WHITE)
      screen.blit(backgroung_image,[0,0])
      font = pygame.font.Font(None, 100)
      text = font.render("Game Over :(", 1, BLACK)
      textpos = text.get_rect()
      textpos.centerx = screen.get_rect().centerx
      textpos.y = 150
      screen.blit(text, textpos)

      button_restart.draw()

    #Acrtualizar pantalla
    pygame.display.flip()
    time.tick(60)
    # pygame.font.SysFont(None,50).render("Sudoku", True,(255,255,255)).get_rect()
   

main()