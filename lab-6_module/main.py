from fastapi import FastAPI
from pydantic import BaseModel
from facade.smart_home_facade import HomeAutomationSystem

app = FastAPI()
automation_system = HomeAutomationSystem()


class IlluminationSettings(BaseModel):
    intensity: int


class TemperatureSettings(BaseModel):
    value: int


class DeviceControl(BaseModel):
    action: str


@app.post("/enable_protection/")
def enable_protection():
    return {"result": automation_system.activate_protection()}


@app.post("/manage_lights/")
def manage_lights(request: IlluminationSettings):
    if request.intensity:
        return {"result": automation_system.adjust_lighting(request.intensity)}
    else:
        return {"result": automation_system.adjust_lighting()}


@app.post("/configure_temperature/")
def configure_temperature(request: TemperatureSettings):
    return {"result": automation_system.adjust_climate(request.value)}


@app.post("/start_music/")
def start_music():
    return {"result": automation_system.start_music_playback()}


@app.post("/operate_fan/")
def operate_fan(request: DeviceControl):
    return {"result": automation_system.manage_fan(request.action)}


@app.post("/operate_ac/")
def operate_ac(request: DeviceControl):
    return {"result": automation_system.manage_ac(request.action)}



