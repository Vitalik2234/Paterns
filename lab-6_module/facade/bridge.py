class Device:
    def power_on(self):
        raise NotImplementedError("This method should be implemented in subclasses")

    def power_off(self):
        raise NotImplementedError("This method should be implemented in subclasses")


class FanDevice(Device):
    def power_on(self):
        return "Fan is now running."

    def power_off(self):
        return "Fan is now off."


class ACDevice(Device):
    def power_on(self):
        return "Air conditioner is now on."

    def power_off(self):
        return "Air conditioner is now off."


class DeviceController:
    def __init__(self, device: Device):
        self.device = device

    def switch_on(self):
        return self.device.power_on()

    def switch_off(self):
        return self.device.power_off()

    def schedule(self, duration):
        return f"Device will run for {duration} minutes."
