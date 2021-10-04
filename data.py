tomu_text = {
    "title": "<tspan class='h1'>TOMU Pinout</tspan>",
    "description": """Features of the TOMU (0.4) development board.
    See EFM32HG309 datasheet for detail 
    on alternate pin functionality.
    tomu.im""",
    "notes": """
    &#x2022;  LED0/1 connected via resistors R2/R1 respectively
    &#x2022;  USB D+/D- connected via resistors R4/R3 respectively
    """,
}


tomu_image_top = {
    "src": "./images/tomu-top-3d.png",
    "x": 0,
    "y": 300,
    "width": 300,
    "height": 300,
    "rotate": -90,
    "coords": {
        "usb_GND": (550, 180),
        "usb_D+": (400, 180),
        "usb_D-": (250, 180),
        "usb_+5V": (100, 180),
        "CAP0B": (550, 860),
        "CAP0A": (400, 885),
        "CAP1B": (250, 885),
        "CAP1A": (100, 860),
    },
}
tomu_image_bottom = {
    "src": "./images/tomu-bottom-3d.png",
    "x": 0,
    "y": 0,
    "width": 300,
    "height": 300,
    "rotate": 0,
    "coords": {
        "LED0": (550, 725),
        "RESET": (560, 584),
        "LEU0_TX": (560, 472),
        "LEU0_RX": (560, 374),
        "GND_1": (560, 282),
        "USB +5V": (506, 102),
        "LED1": (77, 722),
        "+3.3V": (80, 570),
        "DBG_SWDIO": (80, 392),
        "DBG_SWCLK": (80, 220),
        "GND_2": (80, 48),
    },
}


tomu_pinlabels_top = [
    # USB
    {
        "title": "usb_GND",
        "scale": (-1, 1),
        "labels": [[("0", "pin-id"), ("GND", "gnd")]],
    },
    {
        "title": "usb_D+",
        "scale": (-1, 1),
        "labels": [[("18", "pin-id"), ("D+", "comms")]],
    },
    {
        "title": "usb_D-",
        "scale": (-1, 1),
        "labels": [[("17", "pin-id"), ("D-", "comms")]],
    },
    {
        "title": "usb_+5V",
        "scale": (-1, 1),
        "labels": [[("15", "pin-id"), ("+5V", "pwr")]],
    },
    # Buttons
    {
        "title": "CAP0B",
        "labels": [[("23", "pin-id"), ("CAP0B", "comms")]],
    },
    {
        "title": "CAP0A",
        "labels": [[("3", "pin-id"), ("CAP0A", "comms")]],
    },
    {
        "title": "CAP1B",
        "labels": [[("24", "pin-id"), ("CAP1B", "comms")]],
    },
    {
        "title": "CAP1A",
        "labels": [[("4", "pin-id"), ("CAP1A", "comms")]],
    },
]

tomu_pinlabels_bottom = [
    # LEDs
    {
        "title": "LED0",
        "labels": [[("5", "pin-id"), ("LED 0", "led")]],
    },
    {
        "title": "LED1",
        "scale": (-1, 1),
        "labels": [[("1", "pin-id"), ("LED 1", "led")]],
    },
    # Programing pads
    {
        "title": "RESET",
        "labels": [[("7", "pin-id"), ("RESET", "pwr")]],
    },
    {
        "title": "LEU0_TX",
        "labels": [[("10", "pin-id"), ("LEU0_TX", "comms")]],
    },
    {
        "title": "LEU0_RX",
        "labels": [[("11", "pin-id"), ("LEU0_RX", "comms")]],
    },
    {
        "title": "GND_1",
        "labels": [[("0", "pin-id"), ("GND", "gnd")]],
    },
    {
        "title": "USB +5V",
        "labels": [[("15", "pin-id"), ("USB +5V", "pwr")]],
    },
    {
        "title": "+3.3V",
        "scale": (-1, 1),
        "labels": [[("2", "pin-id"), ("+3.3V", "pwr")]],
    },
    {
        "title": "DBG_SWDIO",
        "scale": (-1, 1),
        "labels": [[("20", "pin-id"), ("DBG_SWDIO", "comms")]],
    },
    {
        "title": "DBG_SWCLK",
        "scale": (-1, 1),
        "labels": [[("19", "pin-id"), ("DBG_SWCLK", "comms")]],
    },
    {
        "title": "GND_2",
        "scale": (-1, 1),
        "labels": [[("0", "pin-id"), ("GND", "gnd")]],
    },
]

fomu_image_bottom = {
    "src": "./images/tomu-fpga-dvt1c-back.png",
    "x": 0,
    "y": 0,
    "width": 200,
    "height": 200,
    "rotate": 0,
    "coords": {
        "RGB LED": (864, 650),
        "FPGA": (864, 1017),
        "SPI Flash": (285, 1308),
        "Oscillator": (1422, 1470),
        "v_reg_1": (528, 2043),
        "v_reg_2": (1260, 2043),
        "Voltage regulators": (1545, 2043),
    },
}
fomu_image_top = {
    "src": "./images/tomu-fpga-dvt1c-front.png",
    "x": 200,
    "y": 0,
    "width": 200,
    "height": 200,
    "rotate": 90,
    "coords": {
        "button_1": (92, 278),
        "usb_pin_1": (2090, 278),
    },
}

##########################################
fomu_annotations = [
    {
        "title": "RGB LED",
        "scale": (1, -1),
        "body": {"y": 12},
    },
    {
        "title": "FPGA",
        "scale": (-1, 1),
        "body": {"y": 55},
    },
    {
        "title": "SPI Flash",
        "scale": (-1, -1),
        "body": {"y": 12},
    },
    {
        "title": "Oscillator",
        "scale": (1, -1),
        "body": {"y": 20},
    },
    {
        "title": "v_reg_1",
        "scale": (1, 1),
        "body": {"y": 40},
    },
    {
        "title": "v_reg_2",
        "scale": (1, 1),
        "body": {"y": 40},
    },
    {
        "title": "Voltage regulators",
        "scale": (1, 1),
        "body": {"y": 40},
    },
]

fomu_pinlabels = [
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
]
