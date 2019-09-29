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


from player import Player
from connection.codenjoy_connection import CodenjoyConnection, ws_url

URL = ''

try:
    ws = CodenjoyConnection(ws_url(URL), Player())
    ws.connect()
    ws.run_forever()
except KeyboardInterrupt:
    ws.close()
