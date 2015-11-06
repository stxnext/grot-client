"""
Play GROT game.
"""

import http.client
import json
import random
import time


def get_move(data):
    """
    Get coordinates (start point) of next move.
    """
    return {
        'x': random.randint(0, 4),
        'y': random.randint(0, 4),
    }


def play(room_id, token, server, debug=False, alias=''):
    """
    Connect to game server and play rounds in the loop until end of game.
    """
    # connect to the game server
    client = http.client.HTTPConnection(server)
    client.connect()
    game_url = '/games/{}/board?token={}'.format(room_id, token)
    if alias:
        game_url += '&alias={}'.format(alias)

    # wait until the game starts
    client.request('GET', game_url)

    response = client.getresponse()

    while response.status == 200:
        data = json.loads(response.read().decode())
        if debug:
            print(data)
            # sleep 3 seconds so, you will be able to read printed data
            time.sleep(3)

        # make your move and wait for a new round
        client.request('POST', game_url, json.dumps(get_move(data)))

        response = client.getresponse()
