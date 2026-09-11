import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import CONF_SWITCH_DATAPOINT

from .. import CONF_TUYALOWPOWER_ID, TuyaLowPower , tuya_low_power_ns

DEPENDENCIES = ["tuya_low_power"]
CODEOWNERS = ["@jesserockz"]

TuyaSwitch = tuya_low_power_ns.class_("TuyaSwitch", switch.Switch, cg.Component)

CONFIG_SCHEMA = (
    switch.switch_schema(TuyaSwitch)
    .extend(
        {
            cv.GenerateID(CONF_TUYALOWPOWER_ID): cv.use_id(TuyaLowPower ),
            cv.Required(CONF_SWITCH_DATAPOINT): cv.uint8_t,
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = await switch.new_switch(config)
    await cg.register_component(var, config)

    paren = await cg.get_variable(config[CONF_TUYALOWPOWER_ID])
    cg.add(var.set_tuya_parent(paren))

    cg.add(var.set_switch_id(config[CONF_SWITCH_DATAPOINT]))
