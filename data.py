fomu_pvt = {
    "title": "<tspan class='h1'>FOMU PVT (FPGA TOMU)</tspan>",
    "description": """Features of the FOMU development board.
    https://tomu.im/fomu.html
    """,
    "image": {
        "front": "./images/tomu-fpga-dvt1c-front.png",
        "back": "./images/tomu-fpga-dvt1c-back.png",
    },
    "annotations": [
        {
            "name": "RGB LED",
            "coords": (864, 650),
            "config": {"y": 12, "scale": (1, -1)},
        },
        {"name": "FPGA", "coords": (864, 1017), "config": {"y": 55, "scale": (-1, 1)}},
        {
            "name": "SPI Flash",
            "coords": (285, 1308),
            "config": {"y": 12, "scale": (-1, -1)},
        },
        {
            "name": "Oscillator",
            "coords": (1422, 1470),
            "config": {"y": 20, "scale": (1, -1)},
        },
        {
            "name": "v_reg_1",
            "coords": (528, 2043),
            "config": {"y": 40, "scale": (1, 1)},
        },
        {
            "name": "v_reg_2",
            "coords": (1260, 2043),
            "config": {"y": 40, "scale": (1, 1)},
        },
        {
            "name": "Voltage regulators",
            "coords": (1545, 2043),
            "config": {"y": 40, "scale": (1, 1)},
        },
    ],
    "labelgroups": [
        {
            "name": "buttons",
            "pin_start": (92, 278),
            "label_start": (100, 0),
            "pin_pitch": (0, 400),
            "scale": (-1, 1),
            "labels": [
                [("btn 1", "btn")],
                [("btn 2", "btn")],
                [("btn 3", "btn")],
                [("btn 4", "btn")],
            ],
        },
        {
            "name": "usb_pins",
            "pin_start": (2090, 278),
            "label_start": (100, 0),
            "pin_pitch": (0, 400),
            "scale": (1, 1),
            "labels": [
                [("Vcc", "pwr")],
                [("Data [+]", "data")],
                [("Data [-]", "data")],
                [("GND", "gnd")],
            ],
        },
    ],
}
