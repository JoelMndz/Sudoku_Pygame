from pygame import Surface
import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
  def __init__(self, width, height, screen:Surface, difficulty) -> None:
    self.__width = width
    self.__height = height
    self.__screen = screen
    self.__difficulty = difficulty
    self.selected = None
    self.generator_matrix()

  def generator_matrix(self):
    if self.__difficulty == 'easy':
      self.__matrix = generate_sudoku(9,30)
    elif self.__difficulty == 'medium':
      self.__matrix = generate_sudoku(9,40)
    else:
      self.__matrix = generate_sudoku(9,50)

    self.cells = []
    for i in range(9):
      data = []
      for j in range(9):
        data.append(Cell(self.__matrix[i][j],i,j,self.__screen))
      self.cells.append(data)
    
    self.update_board()

  def draw(self):
    BLACK = (0,0,0)
    gap = self.__width / 9
    for i in range(10):
      if i % 3 == 0:
        thick = 4 
      else:
        thick = 1
        
      pygame.draw.line(self.__screen, BLACK,(0,i*gap),(self.__width, i*gap),thick)
      pygame.draw.line(self.__screen, BLACK, (i*gap, 0),(i*gap, self.__height),thick)

    for i in range(9):
      for j in range(9):
        self.cells[i][j].draw()
    
  def select(self, row, col):
    for i in range(9):
      for j in range(9):
        self.cells[i][j].selected = False

    self.cells[row][col].selected = True
    self.selected = (row, col)


  def click(self, x, y):
    if x < self.__width and y < self.__height:
        gap = self.__width / 9
        x = x // gap
        y = y // gap
        return (int(y),int(x))
    else:
        return None

  def clear(self):
    row, col = self.selected
    self.cells[row][col].set_cell_value(0)
    self.cells[row][col].set_sketched_value(0)

  def sketch(self, value):
    self.cells[self.selected[0]][self.selected[1]].set_sketched_value(value)

  def place_number(self, value):
    row, col = self.selected
    self.cells[row][col].set_cell_value(value)
    self.cells[row][col].set_sketched_value(0)
    self.update_board()

  def reset_to_original(self):
    self.cells = []
    for i in range(9):
      data = []
      for j in range(9):
        data.append(Cell(self.__matrix[i][j],i,j,self.__screen))
      self.cells.append(data)
    
    self.update_board()

  def is_full(self):
    for i in range(9):
      for j in range(9):
        if self.board[i][j] == 0:
          return False
    return True

  def update_board(self):
    self.board = [[self.cells[i][j].value for j in range(9)] for i in range(9)]

  def check_board(self):
    if self.is_full():
      for i in range(9):
        for j in range(9):
          number = self.board[i][j] 
          self.board[i][j] = 0
          if not self.is_valid(i,j,number):
            self.board[i][j] = number
            return False
          self.board[i][j] = number
      return True
    return False

  def valid_in_row(self, row, num):
    for j in range(9):
      if self.board[row][j] == num:
        return False
    return True

  def valid_in_col(self, col, num):
    for i in range(9):
      if self.board[i][col] == num:
        return False
    return True

  def valid_in_box(self, row_start, col_start, num):
    for i in range(row_start,row_start+3):
      for j in range(col_start,col_start+3):
        if self.board[i][j] == num:
          return False
    return True

  def is_valid(self, row, col, num):
    row_start = row // 3 * 3
    col_start = col // 3 * 3
    return self.valid_in_box(row_start,col_start,num) and self.valid_in_col(col,num) and self.valid_in_row(row,num)

  

  