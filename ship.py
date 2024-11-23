# ship.py
from interfaces import IShip

class Ship(IShip):
    def __init__(self, ship_id, fuel, current_port, total_capacity, max_containers, max_heavy, max_refrigerated, max_liquid, fuel_per_km):
        self.ID = ship_id
        self.fuel = fuel
        self.currentPort = current_port
        self.totalWeightCapacity = total_capacity
        self.maxNumberOfAllContainers = max_containers
        self.containers = []
        self.fuelPerKm = fuel_per_km

    def sailTo(self, port, ports):
        """Sails the ship to the specified port."""
        distance = self.currentPort.getDistance(port)
        fuel_needed = distance * self.fuelPerKm

        if self.fuel >= fuel_needed:
            # Достатньо пального для досягнення порту
            self.fuel -= fuel_needed
            self.currentPort.outgoingShip(self)
            port.incomingShip(self)
            self.currentPort = port
            print(f"Ship {self.ID} successfully sailed to port {port.ID}.")
            return True
        else:
            # Недостатньо пального: шукаємо найближчий порт для дозаправки
            print(f"Not enough fuel to reach port {port.ID}. Searching for the nearest port for refueling...")
            nearest_port, min_distance = None, float('inf')

            for candidate_port in ports:  # Передаємо список портів
                if candidate_port == self.currentPort:
                    continue
                distance_to_candidate = self.currentPort.getDistance(candidate_port)
                if distance_to_candidate < min_distance:
                    nearest_port, min_distance = candidate_port, distance_to_candidate

            if nearest_port:
                # Пливемо до найближчого порту для дозаправки
                print(f"Nearest port found: {nearest_port.ID}. Sailing there for refueling.")
                distance_to_nearest = self.currentPort.getDistance(nearest_port)
                fuel_needed_to_nearest = distance_to_nearest * self.fuelPerKm

                if self.fuel >= fuel_needed_to_nearest:
                    self.fuel -= fuel_needed_to_nearest
                    self.currentPort.outgoingShip(self)
                    nearest_port.incomingShip(self)
                    self.currentPort = nearest_port
                    print(f"Ship {self.ID} has arrived at port {nearest_port.ID} for refueling.")

                    # Дозаправка
                    refueled_amount = 500  # Наприклад, додаємо 500 одиниць пального
                    self.reFuel(refueled_amount)

                    # Після дозаправки виводимо повідомлення про успішну дозаправку
                    print(f"Ship {self.ID} has been refueled with {refueled_amount} units of fuel.")

                    # Після дозаправки намагаємось ще раз дістатися до цільового порту
                    return self.sailTo(port, ports)
                else:
                    print(f"Unable to reach port {nearest_port.ID} for refueling. Insufficient fuel.")
                    return False

            print(f"Unable to reach port {port.ID} or any nearby port for refueling. Insufficient fuel.")
            return False

    def load(self, container):
        """Loads a container onto the ship."""
        if len(self.containers) < self.maxNumberOfAllContainers:
            self.containers.append(container)
            return True
        return False

    def unLoad(self, container):
        """Unloads a container from the ship."""
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False

    def reFuel(self, amount):
        """Refuels the ship."""
        self.fuel += amount

    def getCurrentContainers(self):
        """Returns the containers currently loaded on the ship, sorted by container ID."""
        return sorted(self.containers, key=lambda c: c.ID)
