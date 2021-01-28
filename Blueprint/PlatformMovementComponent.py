class PlatformMovementComponent:

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.leg = 0
        self.count = 0
