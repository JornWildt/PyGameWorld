

class SystemsRepository:
    def __init__(self):
        self.systems = []
    
    def add(self, system):
        self.systems.append(system)

    def get_all(self):
        return self.systems