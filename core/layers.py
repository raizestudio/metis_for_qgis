from ..ui.metis_qgis_app_dialog import MetisQgisLayersDialog
from qgis.core import QgsRasterLayer
from PyQt5.QtCore import pyqtSignal


class MetisLayers():
    
    loadlayer = pyqtSignal(object)

    def __init__(self, parent=None):
        self.dlg = MetisQgisLayersDialog()
        self.dlg.setLayout(self.dlg.verticalLayout)
        self.dlg.pushButtonClose.clicked.connect(self.dlg.hide)
        self.dlg.pushButtonCadQU.clicked.connect(lambda: self.load_layer('41'))
        # self.dlg.pushButtonCadTS.clicked.connect(lambda: self.load_layer('37'))
        self.dlg.pushButtonOpenSM.clicked.connect(self.load_osm)
    

    def load_osm(self):
        uri = "type=xyz&url=https://tile.openstreetmap.org/\{z\}/\{x\}/\{y\}.png"
        rlayerosm = QgsRasterLayer(uri, "OpenStreetMap", "wms")
        self.project.addMapLayer(rlayerosm)

    def run(self):
        self.dlg.show()

    def close(self):
        self.dlg.hide()