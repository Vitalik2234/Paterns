from facade.singleton import Singleton


class ConfigurationManager(metaclass=Singleton):
    def __init__(self):
        self.default_temperature = 24
        self.light_mode = "soft"

    def get_default_temperature(self):
        return self.default_temperature

    def get_light_mode(self):
        return self.light_mode


class PowerManager(metaclass=Singleton):
    def __init__(self):
        self.energy_consumption = 0

    def get_usage_report(self):
        return f"Current energy usage: {self.energy_consumption} kWh."

    def optimize_power(self):
        return "Power consumption has been optimized."


class Lighting:
    def enable(self):
        return "Lights are on."

    def disable(self):
        return "Lights are off."

    def set_intensity(self, level):
        return f"Lighting intensity set to {level}%."


class SafetySystem:
    def activate(self):
        return "Protection system enabled."

    def deactivate(self):
        return "Protection system disabled."


class ClimateManager:
    def configure(self, temperature):
        return f"Climate set to {temperature}°C."


class MusicPlayer:
    def play(self):
        return "Music is now playing."

    def stop(self):
        return "Music has stopped."


