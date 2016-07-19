class World:
    def __init__(self):
        self.entities = []
        self.systems = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_system(self, system):
        self.systems.append(system)

    def update(self):
        for system in self.systems:
            system.update(self.entities)

    def draw(self, display):
        for system in self.systems:
            system.draw(self.entities, display)


class Component:
    pass


class System:
    def update(self, entities):
        pass

    def draw(self, entities, display):
        pass


class Entity:
    def __init__(self, name):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def get_component(self, type_):
        for component in self.components:
            if isinstance(component, type_):
                return component
