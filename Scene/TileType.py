class TileType:

    def __init__(self, name, is_blocking):
        self.name = name
        self.is_blocking = is_blocking

TileType.Sea = TileType('sea', True)
TileType.Grass = TileType('grass', False)
TileType.Floor = TileType('floor', False)
TileType.Wall = TileType('wall', True)
TileType.Space = TileType('space', False)

