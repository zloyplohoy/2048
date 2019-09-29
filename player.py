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


from game.moves import UP, DOWN, RIGHT, LEFT


class Player:
    @staticmethod
    def make_move(board):
        """
        Your goal is to reach the highest possible sum of all
        tiles by moving and merging them on the board. Tiles
        of equal value merge when moved towards each other,
        producing a single tile of double the original value.
        Tiles move all at once in either of four directions.
        If no moves can be made, the game will save your
        highscore and start over.
        """

        """
        You will receive the current state of the game board
        as a two-dimensional list of integers. Representation
        shows raw data, while string output is prettyprinted.
        """
        print(repr(board))
        print(str(board))

        """
        You need to plot and optimal move by examining
        the board and returning your decision as one of
        the following constants: UP, DOWN, RIGHT or LEFT.
        """
        # return <DIRECTION>
