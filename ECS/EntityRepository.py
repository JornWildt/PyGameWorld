

class EntityRepository:

    def __init__(self):
        self.entities_index = {}
        self.components_index = {}


    def add_entity(self, entity):
        self.entities_index[entity.id] = entity
        for component in entity.components:
            component_type = type(component)
            if not component_type in (self.components_index):
                self.components_index[component_type] = []
            self.components_index[component_type].append(component)


    def get_entity(self, id):
        return self.entities_index[id]


    def get_components_of_type(self, type):
        if not type in (self.components_index):
            return []
        else:
            return self.components_index[type]


