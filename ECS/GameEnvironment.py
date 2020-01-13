
class GameEnvironment:
    def __init__(self, settings):
        self.services = {}
        self.settings = settings

    def register(self, service, service_name):
        self.services[service_name] = service

    def resolve(self, name):
        return self.services[name]
        