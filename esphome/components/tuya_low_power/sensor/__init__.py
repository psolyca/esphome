import esphome.codegen as cg
from esphome.components import sensor
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_SENSOR_DATAPOINT

from .. import CONF_TUYALOWPOWER_ID, TuyaLowPower, tuya_low_power_ns

DEPENDENCIES = ["tuya_low_power"]
CODEOWNERS = ["@jesserockz"]

TuyaSensor = tuya_low_power_ns.class_("TuyaSensor", sensor.Sensor, cg.Component)

CONFIG_SCHEMA = (
    sensor.sensor_schema(TuyaSensor)
    .extend(
        {
            cv.GenerateID(CONF_TUYALOWPOWER_ID): cv.use_id(TuyaLowPower),
            cv.Required(CONF_SENSOR_DATAPOINT): cv.uint8_t,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

    paren = await cg.get_variable(config[CONF_TUYALOWPOWER_ID])
    cg.add(var.set_tuya_parent(paren))

    cg.add(var.set_sensor_id(config[CONF_SENSOR_DATAPOINT]))
