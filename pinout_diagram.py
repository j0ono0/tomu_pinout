###########################################
#
# TOMU pinout
#
# Export the diagram via commandline:
# >>> py -m pinout.manager -e pinout_diagram output/tomu_pinout.svg -o
#
###########################################


from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.text import TextBlock
from pinout.components.legend import Legend
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.annotation import AnnotationLabel
from pinout import config


# Import data for the diagram
# from data import fomu_pvt as data
import data

# Modify default component configs
config.annotation["body"]["width"] = 160
config.pinlabel["body"]["width"] = 120


diagram = Diagram_2Rows(1024, 800, 650, tag="diagram")
diagram.add_stylesheet("styles.css", embed=False)
diagram.panel_02.add(TextBlock(data.tomu_text["title"], x=20, y=40))
diagram.panel_02.add(TextBlock(data.tomu_text["description"], x=20, y=60))
diagram.panel_02.add(TextBlock(data.tomu_text["notes"], x=400, y=60))


tomu_img_top = Image(**data.tomu_image_top)
# Adjust the transformed image width to maintain original size ratio
px_w, px_h = tomu_img_top.im_size
tomu_img_top.width = tomu_img_top.height * px_w / px_h
tomu_img_top.y = tomu_img_top.width

tomu_top = diagram.panel_01.add(
    Group(
        x=diagram.panel_01.inset_width / 2 - tomu_img_top.bounding_rect().w / 2,
        y=40,
        children=[
            TextBlock("Fig 1: tomu - top", y=-10),
            tomu_img_top,
        ],
    ),
)

# Add pinlabels from data
for lbls in data.tomu_pinlabels_top:
    LBL_MARGIN = 40
    x, y = tomu_img_top.coord(lbls["title"])
    scale = lbls.pop("scale", (1, 1))

    # Vertically align label_starts
    if scale[0] > 0:
        start_x = tomu_img_top.bounding_coords().x2 - x + LBL_MARGIN
    else:
        start_x = x + LBL_MARGIN

    # Modify labels with 'pin-id' tag
    for lbllst in lbls["labels"]:
        for i, lbl in enumerate(lbllst):
            if lbl[1] == "pin-id":
                lbllst[i] = (*lbl, {"body": {"width": 50}})

    tomu_top.add(
        PinLabelGroup(
            x=x,
            y=y,
            pin_pitch=(0, 0),
            label_start=(start_x, 0),
            label_pitch=(0, 0),
            labels=lbls["labels"],
            scale=scale,
        )
    )


#############################

tomu_img_bottom = Image(**data.tomu_image_bottom)
# Adjust the transformed image width to maintain original/pixel size ratio
px_w, px_h = tomu_img_bottom.im_size
tomu_img_bottom.width = tomu_img_bottom.height * px_w / px_h
tomu_bottom = diagram.panel_01.add(
    Group(
        x=diagram.panel_01.inset_width / 2 - tomu_img_bottom.bounding_rect().w / 2,
        y=330,
        children=[
            TextBlock("Fig 2: tomu - bottom", y=-10),
            tomu_img_bottom,
        ],
    ),
)

# Add pinlabels from data
for lbls in data.tomu_pinlabels_bottom:
    LBL_MARGIN = 40
    x, y = tomu_img_bottom.coord(lbls["title"])
    scale = lbls.pop("scale", (1, 1))

    # Vertically align label_starts
    if scale[0] > 0:
        start_x = tomu_img_bottom.bounding_coords().x2 - x + LBL_MARGIN
    else:
        start_x = x + LBL_MARGIN

    # Modify labels with 'pin-id' tag
    for lbllst in lbls["labels"]:
        for i, lbl in enumerate(lbllst):
            if lbl[1] == "pin-id":
                lbllst[i] = (*lbl, {"body": {"width": 50}})

    tomu_bottom.add(
        PinLabelGroup(
            x=x,
            y=y,
            pin_pitch=(0, 0),
            label_start=(start_x, 0),
            label_pitch=(0, 0),
            labels=lbls["labels"],
            scale=scale,
        )
    )
