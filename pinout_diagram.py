###########################################
#
# TOMU pinout
#
###########################################


from pinout.core import Group, Image
from pinout.components.layout import Diagram, Panel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.annotation import AnnotationLabel
from pinout import config

# Experimental layout class!!!!!!!
from template import LayoutA

# Import data for the diagram
# from data import fomu_pvt as data
import data

# Modify default component configs
config.annotation["body"]["width"] = 160

layout = LayoutA(1024, 800, 700, "diagram")
diagram = layout.diagram
layout.add_title(data.title)
layout.add_description(data.description)

layout.add_graphic(
    {
        "x": 512,
        "y": 200,
        "image": "./images/tomu-fpga-dvt1c-back.png",
        "annotations": data.fomu_annotations,
    }
)
layout.add_graphic(
    {
        "x": 512,
        "y": 560,
        "image": "./images/tomu-fpga-dvt1c-front.png",
        "pinlabels": data.fomu_pinlabels,
    }
)

# Export the diagram via commandline:
# >>> py -m pinout.manager -e pinout_diagram output/fomu_pinout.svg -o
