from ..ui.metis_qgis_app_dialog import MetisQgisApdDialog


class MetisApd():

    def __init__(self):
        self.dlg = MetisQgisApdDialog()
        self.dlg.setLayout(self.dlg.mainLayout)

    def run(self):
        self.dlg.show()

    def close(self):
        self.dlg.hide()

