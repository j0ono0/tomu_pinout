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

# Import data for the diagram
# from data import fomu_pvt as data
from data import fomu_pvt as data

# Modify default component configs
config.annotation["body"]["width"] = 160


# Create a new diagram
diagram = Diagram(1024, 800, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a layout
content = diagram.add(
    Panel(
        width=1024,
        height=800,
        inset=(2, 2, 2, 2),
    )
)
panel_main = content.add(
    Panel(
        width=content.inset_width,
        height=700,
        inset=(2, 2, 2, 2),
        tag="panel--main",
    )
)
panel_info = content.add(
    Panel(
        x=0,
        y=panel_main.height,
        width=panel_main.width,
        height=content.inset_height - panel_main.height,
        inset=(2, 2, 2, 2),
        tag="panel--info",
    )
)

# Create a title and a text-block
title_block = panel_info.add(
    TextBlock(
        data["title"],
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
panel_info.add(
    TextBlock(
        data["description"],
        x=20,
        y=60,
        width=title_block.width,
        height=panel_info.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a group to hold the pinout-diagram components.
graphic = panel_main.add(Group(512, 0))

# Add and embed an image
hardware_back = graphic.add(
    Image(data["image"]["back"], x=-150, y=40, width=300, height=300, embed=True)
)
hardware_front = graphic.add(
    Image(data["image"]["front"], x=-150, y=380, width=300, height=300, embed=True)
)

# Add actual pixel dimension to easily extract scaled dimensions
hardware_back.add_coord("size", *hardware_back.im_size)


#####################################################
# Annotations
if "annotations" in data.keys():
    # x offset from edge of board
    offset = 40
    img_width = hardware_back.coord("size", raw=True).x
    x_rhs = hardware_back.coord("size").x + offset

    for anno in data["annotations"]:
        # Add coords to Image instance
        hardware_back.add_coord(anno["name"], *anno["coords"])
        # Calculate x position of annotation body
        if anno["config"]["scale"][0] == 1:
            # label right of image
            x = offset + img_width - hardware_back.coord(anno["name"], True).x
        else:
            # label left of image
            x = offset + hardware_back.coord(anno["name"], True).x
        # Create annotation label
        graphic.add(
            AnnotationLabel(
                x=hardware_back.coord(anno["name"]).x,
                y=hardware_back.coord(anno["name"]).y,
                content=anno["name"],
                body={"x": x, "y": anno["config"]["y"]},
                scale=anno["config"]["scale"],
            )
        )

#####################################################
# Pinlabels
if "labelgroups" in data.keys():
    for grp in data["labelgroups"]:
        hardware_front.add_coord("pin_start", *grp["pin_start"])
        hardware_front.add_coord("pin_pitch", *grp["pin_pitch"])
        graphic.add(
            PinLabelGroup(
                *hardware_front.coord("pin_start"),
                pin_pitch=hardware_front.coord("pin_pitch", True),
                label_start=grp["label_start"],
                label_pitch=(0, 30),
                labels=grp["labels"],
                scale=grp["scale"],
            )
        )


# Export the diagram via commandline:
# >>> py -m pinout.manager -e pinout_diagram output/fomu_pinout.svg -o
