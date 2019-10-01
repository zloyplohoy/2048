# Codenjoy - it's a dojo-like platform from developers to developers.
#
# Copyright (C) 2018 - 2019 Codenjoy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import math
from game.moves import UP, DOWN, RIGHT, LEFT
import itertools
import ast


class MyGameBot:
    def writebuf(val):
        f=open("/tmp/buf","w")
        f.write(str(val))
        f.close()

    def readbuf(val):
        f = open("/tmp/buf", "r")
        out=int(f.readline().strip())
        f.close()
        return out

    def actions(b):

        def moved(b, t):
            return any(x != y for x, y in zip(b, t))

        for action, f in [("left", MyGameBot.left), ("down", MyGameBot.down), ("up", MyGameBot.up), ("right", MyGameBot.right)]:
            t = f(b)
            if moved(b, t):
                yield action, t

    def left(b):
        return MyGameBot.merge(b)

    def right(b):

        def reverse(x):
            return list(reversed(x))
        t = map(reverse, iter(b))
        return [reverse(x) for x in MyGameBot.merge(t)]

    def up(b):

        t = MyGameBot.left(zip(*b))
        return [list(x) for x in zip(*t)]

    def down(b):
        t = MyGameBot.right(zip(*b))
        return [list(x) for x in zip(*t)]
    def merge(b):

        def inner(row, a):
            if not row:
                return a
            x = row[0]
            if len(row) == 1:
                return inner(row[1:], a + [x])
            return inner(row[2:], a + [2 * x]) if x == row[1] else inner(row[1:], a + [x])

        ret = []
        for row in b:
            merged = inner([x for x in row if x != 0], [])
            merged = merged + [0] * (len(row) - len(merged))
            ret.append(merged)
        return ret

    def checkmove(b):
        return False

    def aimove(b):
        """
        Returns a list of possible moves ("left", "right", "up", "down")
        and each corresponding fitness
        """

        def fitness(b):

            snake = []
            for i, col in enumerate(zip(*b)):
                snake.extend(reversed(col) if i % 2 == 0 else col)

            m = max(snake)
            return sum(x / 10 ** n for n, x in enumerate(snake)) - \
                   math.pow((b[3][0] != m) * abs(b[3][0] - m), 2)

        def search(b, d, move=False):

            if d == 0 or (move and False):
                return fitness(b)

            alpha = fitness(b)
            if move:
                for _, child in MyGameBot.actions(b):
                    return max(alpha, search(child, d - 1, False))
            else:
                alpha = 0
                zeros = [(i, j) for i, j in itertools.product(range(4), range(4)) if b[i][j] == 0]
                for i, j in zeros:
                    c1 = [[x for x in row] for row in b]
                    c2 = [[x for x in row] for row in b]
                    c1[i][j] = 2
                    c2[i][j] = 4
                    alpha += (.8 * search(c1, d - 1, True) / len(zeros) + .2 * search(c2, d - 1, True) / len(zeros))
            return alpha

        return [(action, search(child, 5)) for action, child in MyGameBot.actions(b)]



class Player:
    global globvar
    @staticmethod


    def make_move(board):
        """
        Your goal is to reach the highest possible sum of all
        tiles by moving and merging them on the board. Tiles
        of equal value merge when moved towards each other,
        producing a single tile of double the original value.
        Tiles move all at once in either of four directions.
        If no moves can be made, the MyGameBot will save your
        highscore and start over.
        """

        """
        You will receive the current state of the MyGameBot board
        as a two-dimensional list of integers. Representation
        shows raw data, while string output is prettyprinted.
        """
        print(repr(board))
        print(str(board))
        b=ast.literal_eval(repr(board))
        """
        You need to plot and optimal move by examining
        the board and returning your decision as one of
        the following constants: UP, DOWN, RIGHT or LEFT.
        """
        fl=[]
        for sl in b:
            for i in sl:
                fl.append(i)
        midresult=sum(fl)

        oldres=MyGameBot.readbuf('')

        print(midresult,oldres)
        # if midresult == oldres:
        #     return random.choice([UP,DOWN,RIGHT,LEFT])
        MyGameBot.writebuf(midresult)

        possibleMoves =MyGameBot.aimove(b)
        print(possibleMoves)

        if len(possibleMoves) !=0:
            action = max(possibleMoves,  key = lambda x: x[1])[0]
            print(str(action))
            if action =='down':
                return DOWN
            if action == 'right':
                return RIGHT
            if action == 'left':
                return LEFT
            if action =='up':
                return UP
        else: return random.choice([UP,DOWN,RIGHT,LEFT])

