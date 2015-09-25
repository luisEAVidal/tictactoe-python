# Copyright 2012 Chris Kline
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
An AI player of our game. Subclasses Player and implements the simplest
(i.e. dumbest) AI algorithm: make a move at random.
"""

import random
from player import Player

class AIPlayer(Player):
  def pick_movement(self, mov, n):
    corner_cells = [1, n, (n*(n-1))+1, (n*(n-1)+n)] # 3 cells available for IAPlayer
    edge_cells = []	# 5 cells available for IAPlayer
    center_cells = []	# 8 cells available for IAPlayer

    for cell in xrange(2, n):
        edge_cells.append(cell)

    for cell in xrange((n*(n-1)+1)+1, n*n):
        edge_cells.append(cell)

    left_cell = n+1
    max_cell = 1+(n-2)*n
    i = 1

    while left_cell <= max_cell:
        edge_cells.append(left_cell)
        i += 1
        left_cell = 1+(n*i)

    right_cell = n+n
    max_cell = n+(n-2)*n
    i = 1

    while right_cell <= max_cell:
        edge_cells.append(right_cell)
        i += 1
        right_cell = n+(n*i)

    max_rows = n-2
    i = 1

    while i <= max_rows:
        first_center_cell = 2+(n*i)
        last_center_cell = n+(n*i)

        for cell in xrange(first_center_cell, last_center_cell):
            center_cells.append(cell)

        i += 1

    for cell in corner_cells:
        if mov == cell:
            corner_cells.remove(cell)
            return random.choice(corner_cells)

    for cell in edge_cells:
        if mov == cell:
            edge_cells.remove(mov)
            return random.choice(edge_cells)

    for cell in center_cells:
        if mov == cell:
            center_cells.remove(mov)
            if n == 3:
                return random.choice(xrange(1,10))
            else:
                return random.choice(center_cells)

  def make_move(self, game):
    n = game.size
    mov = game.movement

    next_mov = self.pick_movement(int(mov), n)

    game.make_move(next_mov, self.symbol)





