class PlatformMovementComponent:

    def __init__(self, route, pos):
        super().__init__()
        self.route = route
        self.start_position = pos
        self.leg = 0
        self.count = 0
