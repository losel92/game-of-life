# Game of life
# 
# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.
# 
# Select grid dimensions
# Input an array of coordinates to start as filled ([i, j] where i is the row index and j the column index) - [0,0] is top right
# Enjoy!

import time
import random
import pygame
from pygame.locals import *
import sys

# Grid dimensions
gridW = 10
gridH = 10

# The cells that will be starting as alive
starting = [[0,0], [1,1], [1,2], [2,0], [2,1]]

# Seconds per frame
spf = .2

# How many times it will run
generations = 5


# Create a matrix of 0's:
grid = [ [0 for x in range( gridW )] for y in range( gridH ) ]  
n_grid = [ [0 for x in range( gridW )] for y in range( gridH ) ] 

# Insert the starting cells
for coord in starting:
  grid[coord[0]][coord[1]] = 1

def decideFate(y,x):
  # This cell: [i][j]
  # top neighbors: [i-1, i, i+1][j-1]
  # side neighbors: [i-1, i+1][j]
  # bottom neighbors: [i-1, i, i+1][j+1]
  n_count = 0
  out = 0

  # Calculate neighbors alive
  for i in range((y-1), (y+2)):
    if len(grid) > i >= 0:
      for j in range((x-1), (x+2)):
        if not (i == y and j == x) and len(grid[i]) > j >= 0:
          n_count += grid[i][j]
  
  # Makes a pretty cool grid showing the amount of live neighbors each cell has
  n_grid[y][x] = n_count

  # Decide fate
  if grid[y][x] == 1 and 1 < n_count < 4:
    out = 1
  elif grid[y][x] == 0 and n_count == 3:
    out = 1
  
  return out

def get_next_grid():
  temp_grid = [ [0 for x in range( gridW )] for y in range( gridH ) ]
  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      temp_grid[i][j] = decideFate(i,j)
  
  return temp_grid

# for j, row in enumerate(grid):
#   sadsadgrid = get_next_grid()
#   print(str(row) + " -- " + str(n_grid[j]))

# for i in range(generations):
#   for j, row in enumerate(grid):
#     for k in row: 
#       if k > 0: 
#         print(str("[1]"),end="")
#       else: 
#         print(str("[0]"),end="")
#     print("\n",end="")
#     # print(str(row) + " -- " + str(n_grid[j])) # Same as above but with neighbor count map on the side
#   print("")
#   grid = get_next_grid()
#   time.sleep(spf)
  


# Use this to print a grid with each cell's neighbor count
# Effectively tells you what the next round is going to look like
# for i in n_grid:
#   print(i)

def main():
  global grid

  pygame.init()
  run = True

  clock = pygame.time.Clock()
  time_elapsed = 0

  size = width, height = 1440, 920
  surface = pygame.display.set_mode(size)
  
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    if time_elapsed > 2000:
      time_elapsed = 0

      print("running " + str(time_elapsed / 20))
      surface.fill((0,0,0))

      # for j, row in enumerate(grid):
      #   for k, val in enumerate(row): 
      #     if val > 0: 
      for j, row in enumerate(grid):
        for k, val in enumerate(row): 
          if val > 0: 
            pygame.draw.rect(surface, 255, pygame.Rect(k*105,j*105,100,100))
          #   print(str("[1]"),end="")
          # else: 
          #   print(str("[0]"),end="")
        print(row)
        # print("\n",end="")
        # print(str(row) + " -- " + str(n_grid[j])) # Same as above but with neighbor count map on the side
      print("")
      grid = get_next_grid()

    dt = clock.tick()
    time_elapsed += dt
    pygame.display.update()


main()