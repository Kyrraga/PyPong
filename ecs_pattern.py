class World:
    entities = []
    systems = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def add_system(self, system):
        self.systems.append(system)

    def update(self):
        for system in self.systems:
            system.update(self.entities)

    def draw(self):
        for system in self.systems:
            system.draw(self.entities)


class Component:
    pass


class System:
    def update(self):
        pass

    def draw(self, display):
        pass


class Entity:
    components = []

    def add_component(self, component):
        self.components.append(component)

    def get_component(self, type_):
        for component in self.components:
            if isinstance(component, type_):
                return component
