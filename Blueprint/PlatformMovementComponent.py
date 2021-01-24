class PlatformMovementComponent:

    direction_vectors = [
        (0,-1),
        (0.71,-0.71),
        (1,0),
        (0.71,0.71),
        (0,1),
        (-0.71,0.71),
        (-1,0),
        (-0.71,-0.71)
    ]

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.leg = 0
        self.count = 0
