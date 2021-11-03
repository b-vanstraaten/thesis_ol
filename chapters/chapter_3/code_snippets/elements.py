elements = {
    "left_plunger": {
        "singleInput": {"port": ("con1", 1)},
        "hold_offset": {"duration": 250},
        "operations": {
            "constant": "constant"
        },
    },
    "right_plunger": {
        "singleInput": {"port": ("con1", 2)},
        "hold_offset": {"duration": 250},
        "operations": {
            "constant": "constant"
        },
    },
    "charge_sensor_plunger": {
        "singleInput": {"port": ("con1", 3)},
        "hold_offset": {"duration": 250},
        "operations": {
            "constant": "constant"
        },
    },
    "charge_sensor_ohmic": {
        "singleInput": {"port": ("con1", 4)},
        "time_of_flight": 180,
        "smearing": 0,
        "intermediate_frequency": 100e6,
        "outputs": {"out1": ("con1", 1)},
        "operations": {
            "measure": "measure"
        },
    },
}
