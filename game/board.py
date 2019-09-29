from math import sqrt
from tabulate import tabulate


class Board(list):
    def __init__(self, int_array):
        self._str = self.list_to_2d(list(map(self.integer_to_str, int_array)))
        self.extend(self.list_to_2d(int_array))

    def __str__(self):
        return tabulate(self._str, tablefmt='grid')

    @classmethod
    def from_textmessage(cls, textmessage):
        board_symbols = str(textmessage).split('=')[1]
        return cls(list(map(cls.symbol_to_integer, board_symbols)))

    @staticmethod
    def list_to_2d(lst):
        if (sqrt(len(lst)) % 1) == 0:
            size = int(sqrt(len(lst)))
        else:
            raise ValueError('Invalid list size for 2D conversion: %s' % sqrt(len(lst)))

        return [lst[i:i + size] for i in range(0, size ** 2, size)]

    @staticmethod
    def symbol_to_integer(symbol):
        symbol_map = {
            ' ': 0,
            '2': 2,
            '4': 4,
            '8': 8,
            'A': 16,
            'B': 32,
            'C': 64,
            'D': 128,
            'E': 256,
            'F': 512,
            'G': 1024,
            'H': 2048,
            'I': 4096,
            'J': 8192,
            'K': 16384,
            'L': 32768,
            'M': 65536,
            'N': 131072,
            'O': 262144,
            'P': 524288,
            'Q': 1048576,
            'R': 2097152,
            'S': 4194304,
            'X': -1
        }

        if symbol in symbol_map.keys():
            return symbol_map[symbol]
        else:
            raise ValueError('Invalid symbol for conversion to integer: %s' % str(symbol))

    @staticmethod
    def integer_to_str(integer):
        str_map = {
            '0': '',
            '2': '2',
            '4': '4',
            '8': '8',
            '16': '16',
            '32': '32',
            '64': '64',
            '128': '128',
            '256': '256',
            '512': '512',
            '1024': '1K',
            '2048': '2K',
            '4096': '4K',
            '8192': '8K',
            '16384': '16K',
            '32768': '32K',
            '65536': '64K',
            '131072': '128K',
            '262144': '256K',
            '524288': '512K',
            '1048576': '1M',
            '2097152': '2M',
            '4194304': '4M',
            '-1': 'X'
        }

        if str(integer) in str_map.keys():
            return str_map[str(integer)]
        else:
            raise ValueError('Invalid integer for conversion to string: %s' % str(integer))
