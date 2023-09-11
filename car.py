from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
# In this diagram:

# Car is the base class representing a car. It contains common attributes like last_service_date.

# Engine and Battery are abstract classes representing the engine and battery components. They define the interface for maintenance criteria.

# Concrete engine classes (CapuletEngine, WilloughbyEngine, SternmanEngine) and battery classes (SpindlerBattery, NubbinBattery) inherit from their respective abstract classes and implement their specific maintenance criteria.

# TireMaintenance is a new class/interface for handling tire maintenance in the future. It defines methods for checking tire condition.

# CarModel is a class representing car models. It has associations with Engine, Battery, and TireMaintenance, allowing for flexible configurations of car models with different components.

# The CarService class is responsible for evaluating when a car needs service. It has associations with CarModel, Engine, Battery, and TireMaintenance.

# This design allows for extensibility by easily adding new engine types, battery types, tire maintenance criteria, and car models without major code modifications. It adheres to the principle of composition over inheritance, making it more flexible and maintainable.

# Please keep in mind that this is a simplified representation. In a real-world scenario, you might have more classes, methods, and relationships to accurately model your Lyft Rentals system. Additionally, you should convert this diagram to a PDF format and submit it as required.