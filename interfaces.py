from abc import ABC, abstractmethod


class IPort(ABC):
    """Abstract base class for port operations.

    This class defines the interface for managing incoming and outgoing ships
    in a port.
    """

    @abstractmethod
    def incomingShip(self, ship):
        """Handles the arrival of a ship to the port.

        Args:
            ship (Ship): The ship that is arriving at the port.
        """
        pass

    @abstractmethod
    def outgoingShip(self, ship):
        """Handles the departure of a ship from the port.

        Args:
            ship (Ship): The ship that is departing from the port.
        """
        pass


class IShip(ABC):
    """Abstract base class for ship operations.

    This class defines the interface for managing ship operations
    such as sailing, refueling, and loading/unloading containers.
    """

    @abstractmethod
    def sailTo(self, port):
        """Sails the ship to a specified port.

        Args:
            port (Port): The destination port to sail to.

        Returns:
            bool: True if the ship successfully sailed to the destination port, False otherwise.
        """
        pass

    @abstractmethod
    def reFuel(self, fuel):
        """Refuels the ship.

        Args:
            fuel (float): The amount of fuel to add to the ship.
        """
        pass

    @abstractmethod
    def load(self, container):
        """Loads a container onto the ship.

        Args:
            container (Container): The container to load onto the ship.

        Returns:
            bool: True if the container was successfully loaded, False otherwise.
        """
        pass

    @abstractmethod
    def unLoad(self, container):
        """Unloads a container from the ship.

        Args:
            container (Container): The container to unload from the ship.

        Returns:
            bool: True if the container was successfully unloaded, False otherwise.
        """
        pass
