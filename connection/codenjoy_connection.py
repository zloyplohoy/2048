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


from ws4py.client.threadedclient import WebSocketClient
from game.board import Board

try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs


class CodenjoyConnection(WebSocketClient):
    def __init__(self, url, player):
        super(CodenjoyConnection, self).__init__(url)
        self.player = player

    def received_message(self, m):
        move = self.player.make_move(Board.from_textmessage(m))
        if move:
            self.send(move)


def ws_url(url):
    if not url:
        print('Please set URL in __main__.py')
        exit()
    parsed = urlparse(url)
    host = parsed.netloc
    ws_path = 'codenjoy-contest/ws'
    player_id = parsed.path.split('/')[-1]
    code = parse_qs(parsed.query)['code'][0]

    return 'ws://{0}/{1}?user={2}&code={3}'.format(host, ws_path, player_id, code)
