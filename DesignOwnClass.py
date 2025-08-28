# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # initialize base class
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}")

    def charge(self):
        print(f"🔋 {self.device_info()} is charging...")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 14", 128, 3200)

# Use methods
print(phone1.phone_info())
phone1.make_call("+123456789")
phone2.charge()
