from math import sqrt
from interfaces import IPort  # Додаємо цей імпорт

class Port(IPort):
    def __init__(self, port_id, latitude, longitude):
        self.ID = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.dockedShips = []

    def incomingShip(self, ship):
        """Handles the arrival of a ship to the port."""
        self.dockedShips.append(ship)
        print(f"Ship {ship.ID} has arrived at port {self.ID}.")

    def outgoingShip(self, ship):
        """Handles the departure of a ship from the port."""
        if ship in self.dockedShips:
            self.dockedShips.remove(ship)
            print(f"Ship {ship.ID} has left port {self.ID}.")

    def getDistance(self, other_port):
        """Calculates the distance to another port."""
        return sqrt((self.latitude - other_port.latitude) ** 2 + (self.longitude - other_port.longitude) ** 2)
