import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import CONF_SENSOR_DATAPOINT

from .. import CONF_TUYALOWPOWER_ID, TuyaLowPower, tuya_low_power_ns

DEPENDENCIES = ["tuya_low_power"]
CODEOWNERS = ["@dentra"]

TuyaTextSensor = tuya_low_power_ns.class_("TuyaTextSensor", text_sensor.TextSensor, cg.Component)

CONFIG_SCHEMA = (
    text_sensor.text_sensor_schema()
    .extend(
        {
            cv.GenerateID(): cv.declare_id(TuyaTextSensor),
            cv.GenerateID(CONF_TUYALOWPOWER_ID): cv.use_id(TuyaLowPower),
            cv.Required(CONF_SENSOR_DATAPOINT): cv.uint8_t,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = await text_sensor.new_text_sensor(config)
    await cg.register_component(var, config)

    paren = await cg.get_variable(config[CONF_TUYALOWPOWER_ID])
    cg.add(var.set_tuya_parent(paren))

    cg.add(var.set_sensor_id(config[CONF_SENSOR_DATAPOINT]))
