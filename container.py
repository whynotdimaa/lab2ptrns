from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self, container_id, weight):
        self.ID = container_id
        self.weight = weight

    @abstractmethod
    def consumption(self):
        pass

class BasicContainer(Container):
    def consumption(self):
        return self.weight * 2.0

class HeavyContainer(Container):
    def consumption(self):
        return self.weight * 3.5

class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        return self.weight * 4.5
