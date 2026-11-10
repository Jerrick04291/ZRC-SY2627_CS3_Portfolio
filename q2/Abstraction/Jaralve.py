from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2PH"


class TempSensor(Sensor):
    def get_reading(self):
        return "24.5C"


p = PHSensor()
t = TempSensor()

print("------Lab Inventory System------")
print(f"[pH Sensor] Reading: {p.get_reading()}")
print(f"[Temperature Sensor] Reading: {t.get_reading()}")
print("\n---------------------------------")