class EntityRepository:

    def __init__(self):
        self.entities_index = {}
        self.components_index = {}
        self.next_entity_id = 0


    def add_entity(self, entity):
        self.next_entity_id += 1
        entity.id = self.next_entity_id
        self.entities_index[entity.id] = entity

        for component_type in entity.components:
            if not component_type in (self.components_index):
                self.components_index[component_type] = set()
            self.components_index[component_type].add(entity.components[component_type])

        return entity


    def remove_entity(self, entity):
        del self.entities_index[entity.id]
        for component_type in entity.components:
            component_list = self.components_index[component_type]
            component_list.remove(entity.components[component_type])


    def clear_scene_entities(self):
        for entity_id in list(self.entities_index):
            entity = self.entities_index[entity_id]
            if entity.is_scene_entity:
                self.remove_entity(entity)


    def get_entity(self, id):
        return self.entities_index[id]


    def get_components_of_type(self, type):
        if not type in (self.components_index):
            return set()
        else:
            return self.components_index[type]


    def get_components_of_types(self, *types):
        found_entities = {}
        for type in types:
            for component in self.get_components_of_type(type):
                entity = component.entity
                if not entity in found_entities:
                    found_entities[entity] = 0
                found_entities[entity] += 1

        type_count = len(types)
        for entity in found_entities:
            if found_entities[entity] == type_count:
                yield [entity.components[type] for type in types]

