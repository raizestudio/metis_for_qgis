from re import I
from qgis.core import (
    QgsPrintLayout,
    QgsLayoutItemLabel,
    QgsLayoutItemPicture,
    QgsLayoutItemShape,
    QgsLayoutItemPage,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsUnitTypes,
    QgsFillSymbol,

)

from qgis.PyQt.QtGui import (
    QFont,
    QColor,
)

class MetisLayout():

    def __init__(self, project):
        self.layout = QgsPrintLayout(project)

        # Init
        self.layout.initializeDefaults()


    def select_page(self, page):
        pagecolec = self.layout.pageCollection()
        selectedpage = pagecolec.page(page)

        return selectedpage

    def rename_layout(self, name):
        self.layout.setName(name)


    def change_page_settings(self, page, pagetype, orientation):
        """
            Set page settings
        """
        if orientation == 'portrait':
            self.select_page(page).setPageSize(pagetype, QgsLayoutItemPage.Portrait)

        elif orientation == 'landscape':
            self.select_page(page).setPageSize(pagetype, QgsLayoutItemPage.Landscape)


    def generate_label(self, id, text, movex, movey, resizex, resizey, font, *args, **kwargs):
        """
            Return a label ready to put in layout
        """
        if 'nbpage' in kwargs:
            nbpage = kwargs['nbpage']
        else:
            nbpage = 0

        label = QgsLayoutItemLabel(self.layout)
        label.setId(id)
        label.setText(text)
        label.attemptMove(QgsLayoutPoint(movex, movey, QgsUnitTypes.LayoutMillimeters), page=nbpage)
        label.attemptResize(QgsLayoutSize(*[resizex, resizey], QgsUnitTypes.LayoutMillimeters))
        label.setFont(font)
        if 'fontcolor' in kwargs:
            label.setFontColor(kwargs['fontcolor'])
        
        return label

    def generate_image(self, id, imgpath, movex, movey, resizex, resizey, *args, **kwargs):
        """
            Return image item to layout
        """
        if 'nbpage' in kwargs:
            nbpage = kwargs['nbpage']
        else:
            nbpage = 0

        image = QgsLayoutItemPicture(self.layout)
        image.setId(id)
        image.setPicturePath(imgpath)

        if 'resizemode' in kwargs:
            image.setResizeMode(kwargs['resizemode'])
        else:
            image.setResizeMode(QgsLayoutItemPicture.ZoomResizeFrame)

        if 'imgmode' in kwargs:
            image.setMode(kwargs['imgmode'])
        else:
            image.setMode(QgsLayoutItemPicture.FormatRaster)

        if 'imgmoveunits' in kwargs:
            image.attemptMove(QgsLayoutPoint(movex, movey, kwargs['imgmoveunits']), page=nbpage)
        else:
            image.attemptMove(QgsLayoutPoint(movex, movey, QgsUnitTypes.LayoutMillimeters), page=nbpage)

        if 'imgresizeunits' in kwargs:
            image.attemptResize(QgsLayoutSize(*[resizex, resizey], kwargs['imgresizeunits']))
        else:
            image.attemptResize(QgsLayoutSize(*[resizex, resizey], QgsUnitTypes.LayoutPixels))

        return image

    def generate_shape(self, id, shapetype, bgcolor, movex, movey, resizex, resizey, *args, **kwargs):
        props = {}
        props["color"] = "black"
        props["style"] = "solid"
        props["style_border"] = "solid"
        props["color_border"] = "black"
        props["width_border"] = "0"
        props["joinstyle"] = "miter"

        if 'nbpage' in kwargs:
            nbpage = kwargs['nbpage']
        else:
            nbpage = 0

        shape = QgsLayoutItemShape(self.layout)
        shape.setId(id)
        shape.setShapeType(shapetype)
        shape.setBackgroundColor(bgcolor)

        if 'shapemoveunits' in kwargs:
            shape.attemptMove(QgsLayoutPoint(movex, movey, kwargs['shapemoveunits']), page=nbpage)
        else:
            shape.attemptMove(QgsLayoutPoint(movex, movey, QgsUnitTypes.LayoutMillimeters), page=nbpage)


        if 'shaperesizeunits' in kwargs:
            shape.attemptResize(QgsLayoutSize(*[resizex, resizey], kwargs['shaperesizeunits']))
        else:
            shape.attemptResize(QgsLayoutSize(*[resizex, resizey], QgsUnitTypes.LayoutMillimeters))

        sm = QgsFillSymbol.createSimple(props)
        shape.setSymbol(sm)
        
        return shape
