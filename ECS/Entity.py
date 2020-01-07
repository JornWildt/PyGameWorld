import uuid

class Entity:
    def __init__(self, components):
        self.id = None
        self.components = {}
        for c in components:
            c.entity = self
            self.components[type(c)] = c

    def get_component_of_type(self, type):
        return self.components[type] if type in self.components else None
