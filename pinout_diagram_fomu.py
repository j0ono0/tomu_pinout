###########################################
#
# TOMU pinout
#
# Export the diagram via commandline:
# >>> py -m pinout.manager -e pinout_diagram output/fomu_pinout.svg -o
#
###########################################


from typing import Text
from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
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


diagram = Diagram_2Rows(1024, 800, 700, tag="diagram")
diagram.add_stylesheet("styles.css")
diagram.panel_02.add(TextBlock(data.title, x=20, y=40))
diagram.panel_02.add(TextBlock(data.description, x=20, y=60))


img_01 = Image(**data.fomu_image_bottom)
txt_01 = TextBlock("Fig 1", y=-10)
fig_01 = diagram.panel_01.add(
    Group(
        x=400,
        y=100,
        children=[img_01, txt_01],
    ),
)
for anno in data.fomu_annotations:
    title = anno.pop("title")
    x, y = img_01.coord(title)
    fig_01.add(AnnotationLabel(content=title, x=x, y=y, **anno))

tomu_img = Image(**data.tomu_image_bottom)
# Adjust the transformed image width to maintain original size ratio
tx, ty = tomu_img.im_size
tomu_img.width = tomu_img.height * tx / ty
tomu = diagram.panel_01.add(
    Group(
        x=300,
        y=380,
        children=[
            TextBlock("Fig 2: tomu", y=-10),
            tomu_img,
        ],
    ),
)

# Add pinlabels from data
for lbls in data.tomu_pinlabels:
    LBL_MARGIN = 40
    x, y = tomu_img.coord(lbls["title"])
    scale = lbls.pop("scale", (1, 1))

    # Vertically align label_starts
    if scale[0] > 0:
        start_x = tomu_img.width - x + LBL_MARGIN
    else:
        start_x = x + LBL_MARGIN

    # Modify labels with 'pin-id' tag
    for lbllst in lbls["labels"]:
        for i, lbl in enumerate(lbllst):
            if lbl[1] == "pin-id":
                lbllst[i] = (*lbl, {"body": {"width": 50}})

    tomu.add(
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
