import os

from qgis.PyQt.QtCore import (
    Qt,

)
from qgis.PyQt.QtWidgets import (
    QFileDialog,
)

class CustomFileDialog():

    def __init__(self):
        self.dlg = QFileDialog()
        # self.dlg.setModal(False)
        self.dlg.setFileMode(QFileDialog.ExistingFile)
        self.dlg.setNameFilter('pointstechnique.shp')
        self.dlg.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
    
    def run(self):
        self.dlg.exec()
        files = self.dlg.selectedFiles()

        return files