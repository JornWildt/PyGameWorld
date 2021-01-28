import uuid

class Entity:
    def __init__(self, components, is_scene_entity):
        self.id = None
        self.is_scene_entity = is_scene_entity
        self.components = {}
        for c in components:
            c.entity = self
            self.components[type(c)] = c

    def get_component_of_type(self, type):
        return self.components[type] if type in self.components else None
