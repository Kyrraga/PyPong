# -*- coding: utf-8 -*-
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

    def __iadd__(self, other):
        if isinstance(other, Entity):
            self.add_entity(other)
        elif isinstance(other, System):
            self.add_system(other)
        else:
            raise TypeError('other should be either Entity or System')


class Component:
    pass


class System:
    def update(self, entities):
        pass

    def draw(self, entities, display):
        pass


class Entity:
    """Экземпляры сущностей должны либо иметь тип Entity,
    либо наследовать от Entity и вызывать Entity.__init__(self)"""
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def get_component(self, type_):
        for component in self.components:
            if isinstance(component, type_):
                return component

    def __iadd__(self, other):
        if isinstance(other, Component):
            self.add_component(other)
        else:
            raise TypeError('other should be a Component')

    def __getitem(self, key):
        return self.get_component(key)
