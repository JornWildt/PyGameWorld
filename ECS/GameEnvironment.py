
class GameEnvironment:
    def __init__(self):
        self.services = {}

    def register(self, service, service_name):
        self.services[service_name] = service

    def resolve(self, name):
        return self.services[name]
        