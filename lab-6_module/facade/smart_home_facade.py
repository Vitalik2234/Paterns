from facade.Subsystems import (
    Lighting,
    SafetySystem,
    ClimateManager,
    MusicPlayer,
    ConfigurationManager,
)
from facade.bridge import DeviceController, FanDevice, ACDevice


class HomeAutomationSystem:
    def __init__(self):
        self.lighting = Lighting()
        self.safety = SafetySystem()
        self.climate = ClimateManager()
        self.music = MusicPlayer()
        self.config = ConfigurationManager()

        # Devices controlled via bridge
        self.fan = DeviceController(FanDevice())
        self.ac = DeviceController(ACDevice())

    def activate_protection(self):
        return self.safety.activate()

    def adjust_lighting(self, intensity=None):
        if intensity:
            return self.lighting.set_intensity(intensity)
        else:
            return self.lighting.enable()

    def adjust_climate(self, temperature):
        return self.climate.configure(temperature)

    def start_music_playback(self):
        return self.music.play()

    def manage_fan(self, action: str):
        if action == "on":
            return self.fan.switch_on()
        elif action == "off":
            return self.fan.switch_off()

    def manage_ac(self, action: str):
        if action == "on":
            return self.ac.switch_on()
        elif action == "off":
            return self.ac.switch_off()




