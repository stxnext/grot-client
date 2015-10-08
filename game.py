"""
Play GROT game.
"""

import http.client
import json
import random
import time


def get_move(data):
    """a
    Get coordinates (start point) of next move.
    """
    return {
        'x': random.randint(0, 4),
        'y': random.randint(0, 4),
    }


def play(room_id, token, server, debug=False):
    """
    Connect to game server and play rounds in the loop until end of game.
    """
    # connect to the game server
    client = http.client.HTTPConnection(server, 8080)
    client.connect()

    # wait until the game starts
    client.request('GET', '/games/{}/board?token={}'.format(room_id, token))

    response = client.getresponse()

    while response.status == 200:
        data = json.loads(response.read().decode())
        if debug:
            print(data)
            # sleep 3 seconds so, you will be able to read printed data
            time.sleep(3)

        # make your move and wait for a new round
        client.request(
            'POST', '/games/{}/board?token={}'.format(room_id, token),
            json.dumps(get_move(data))
        )

        response = client.getresponse()
