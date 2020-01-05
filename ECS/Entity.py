import uuid

class Entity:
    def __init__(self, id, components):
        self.id = id if id != None else uuid.uuid4()

        for c in components:
            c.id = self.id

        self.components = components
