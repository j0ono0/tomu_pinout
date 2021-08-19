# An attempt at creating a pinout template.
# This provides a 'middle ground' between the more basic pinout framework
# and user data that populates a pinout diagram
# IE: The template is to provide all design/layout decisions
#

from pinout.core import Group, Image
from pinout.components.layout import Diagram, Panel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.annotation import AnnotationLabel
from pinout import config


class LayoutA:
    """A preconfigured layout with main panel info bar."""

    def __init__(self, width, height, main_height, tag="pinout"):
        self.diagram = Diagram(width, height, tag)
        self.main = None
        self.info = None
        self.title = None
        self.main_height = main_height

        # Add a stylesheet
        self.diagram.add_stylesheet("styles.css", embed=True)

        # Create a layout
        content = self.diagram.add(
            Panel(
                width=1024,
                height=800,
                inset=(2, 2, 2, 2),
            )
        )
        self.main = content.add(
            Panel(
                width=content.inset_width,
                height=self.main_height,
                inset=(2, 2, 2, 2),
                tag="panel--main",
            )
        )
        self.info = content.add(
            Panel(
                x=0,
                y=self.main.height,
                width=self.main.width,
                height=content.inset_height - self.main.height,
                inset=(2, 2, 2, 2),
                tag="panel--info",
            )
        )

    def add_title(self, text):
        self.title = self.info.add(
            TextBlock(
                text,
                x=20,
                y=30,
                line_height=18,
                tag="panel title_block",
            )
        )

    def add_description(self, text):
        self.info.add(
            TextBlock(
                text,
                x=20,
                y=60,
                width=self.info.width,
                height=self.info.height - self.title.height,
                line_height=18,
                tag="panel text_block",
            )
        )

    def add_graphic(self, context):
        # Create a group to hold the pinout-diagram components.
        # context is a ridiculous dict of all the required data
        x = context["x"]
        y = context["y"]
        img_path = context["image"]
        annotations = context.get("annotations", None)
        pinlabels = context.get("pinlabels", None)

        graphic = self.main.add(Group(x, y))

        # Add and embed an image
        img = graphic.add(
            Image(img_path, x=-150, y=-150, width=300, height=300, embed=True)
        )

        # Add actual pixel dimension to easily extract scaled dimensions
        img.add_coord("size", *img.im_size)

        #####################################################
        # Annotations
        if annotations:
            # x offset from edge of board
            offset = 40
            img_width = img.coord("size", raw=True).x
            x_rhs = img.coord("size").x + offset

            for anno in annotations:
                # Add coords to Image instance
                img.add_coord(anno["name"], *anno["coords"])
                # Calculate x position of annotation body
                if anno["config"]["scale"][0] == 1:
                    # label right of image
                    x = offset + img_width - img.coord(anno["name"], True).x
                else:
                    # label left of image
                    x = offset + img.coord(anno["name"], True).x
                # Create annotation label
                graphic.add(
                    AnnotationLabel(
                        x=img.coord(anno["name"]).x,
                        y=img.coord(anno["name"]).y,
                        content=anno["name"],
                        body={"x": x, "y": anno["config"]["y"]},
                        scale=anno["config"]["scale"],
                    )
                )

        #####################################################
        # Pinlabels
        if pinlabels:
            for grp in pinlabels:
                img.add_coord("pin_start", *grp["pin_start"])
                img.add_coord("pin_pitch", *grp["pin_pitch"])
                graphic.add(
                    PinLabelGroup(
                        *img.coord("pin_start"),
                        pin_pitch=img.coord("pin_pitch", True),
                        label_start=grp["label_start"],
                        label_pitch=(0, 30),
                        labels=grp["labels"],
                        scale=grp["scale"],
                    )
                )
