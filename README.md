# GROT game client

## Token

To play GROT you have to sign in with GitHub account on
[GROT game server](http://grot-server.games.stxnext.pl).
After sign in you will get token that you have to register in game client.

## Instalation

Clone GROT client repository
```
git clone https://github.com/stxnext/grot-client
cd grot-client
```

Register your unique token in the client
```
python3 client.py register your-unique-token
```

## Play

### Play one move in loop (development mode)

```
python3 client.py play_devel
```

### Play full game against STX Bot

```
python3 client.py play_vs_bot
```

### Play full game against other players

Create your onw room
```
python3 client.py new_room --max-players=10
```

Or find `<room_id>` on [/games](http://grot-server.games.stxnext.pl/games).

Join game
```
python3 client.py join <room_id>
```

Wait for game start (when room is full or after X minutes or manually).

Room owner can start game manually
```
python3 client.py start <room_id>
```

Check results [/games/room_id](http://grot-server.games.stxnext.pl/games/<room_id>).


## Sample response

Sample response from the server that describe current game state
(score, available moves, board state - points and arrows' direction).

```python
{
    "score": 0,  # obtained points
    "moves": 5,  # available moves
    "moved": [None, None],  # your last choice [x, y]
    "board": [
        [
            {
                "points": 1,
                "direction": "up",
                "x": 0,
                "y": 0,
            },
            {
                "points": 0,
                "direction": "down",
                "x": 1,
                "y": 0,
            }
        ],
        [
            {
                "points": 5,
                "direction": "right",
                "x": 0,
                "y": 1,
            },
            {
                "points": 0,
                "direction": "left",
                "x": 1,
                "y": 1,
            }
        ]
    ]
}
```
