# main.py
from port import Port
from ship import Ship
from container import BasicContainer, HeavyContainer, RefrigeratedContainer
from json_handler import save_data_to_json

def create_container(container_id, weight, container_type=None):
    if weight <= 2000:
        return BasicContainer(container_id, weight)
    elif container_type == "R":
        return RefrigeratedContainer(container_id, weight)
    else:
        return HeavyContainer(container_id, weight)

if __name__ == "__main__":
    # Створення трьох портів
    port1 = Port(1, 50.0, 75.0)  # Порт 1
    port2 = Port(2, 60.0, 85.0)  # Порт 2
    port3 = Port(3, 80.0, 95.0)  # Порт 3

    # Створення корабля
    ship = Ship(1, 50, port1, 8000, 10, 5, 3, 2, 2)

    # Створення контейнерів
    container1 = create_container(1, 1500)
    container2 = create_container(2, 2500, "R")
    container3 = create_container(3, 1700)

    # Завантаження контейнерів на корабель
    ship.load(container1)
    ship.load(container2)  # спроба завантажити холодильний контейнер

    # Переходи між портами
    if ship.sailTo(port3, [port1, port2, port3]):
        print(f"Ship {ship.ID} successfully sailed to port {port3.ID}.")
    else:
        print(f"The ship couldn't reach port {port3.ID}.")

    # Підготовка результату для JSON
    result = {
        "ports": [
            {
                "id": port1.ID,
                "latitude": port1.latitude,
                "longitude": port1.longitude,
                "containers": [c.ID for c in port1.containers],
                "ships": [
                    {
                        "id": ship.ID,
                        "fuel_left": round(ship.fuel, 2),
                        "total_capacity": ship.totalWeightCapacity,
                    }
                ] if ship.currentPort == port1 else []
            },
            {
                "id": port2.ID,
                "latitude": port2.latitude,
                "longitude": port2.longitude,
                "containers": [],
                "ships": [
                    {
                        "id": ship.ID,
                        "fuel_left": round(ship.fuel, 2),
                        "total_capacity": ship.totalWeightCapacity,
                    }
                ] if ship.currentPort == port2 else []
            },
            {
                "id": port3.ID,
                "latitude": port3.latitude,
                "longitude": port3.longitude,
                "containers": [],
                "ships": [
                    {
                        "id": ship.ID,
                        "fuel_left": round(ship.fuel, 2),
                        "total_capacity": ship.totalWeightCapacity,
                    }
                ] if ship.currentPort == port3 else []
            }
        ]
    }

    # Збереження результатів у JSON
    save_data_to_json('output.json', result)
    print("Results have been saved to 'output.json'.")
