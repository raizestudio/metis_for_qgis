from ..ui.metis_qgis_app_dialog import MetisQgisLoadingDialog

from PyQt5.QtCore import (
    QEventLoop,
    QTimer,
    QThread,
    QObject,
    pyqtSignal,
    Qt,
    

)
from PyQt5.QtGui import (
    QPixmap,
)

from PyQt5.QtWidgets import (
    QGraphicsDropShadowEffect,

)
import os
from time import sleep

# import openpyxl

class Worker(QObject):

    finished = pyqtSignal()
    progress = pyqtSignal(int)
    opacity = pyqtSignal(float)
    progressmsg = pyqtSignal(str, name="progressmsg")
    settingchanged = pyqtSignal(dict)

    def __init__(self, project, parent=None):
        super(Worker, self).__init__(parent)
        self.project = project

    def boot(self):
        """
            Boot procedure
        """
        setting = {}
        self.progressmsg.emit('Chargement des données...')

        # openpyxl.Workbook()

        # Checking layers
        self.progressmsg.emit('Identification projet en cours...')
        layers = self.project.mapLayers()

        if layers:
            self.settingchanged.emit({'haslayers': True})
            layerpointstechnique = self.project.mapLayersByName('pointstechnique')
            if layerpointstechnique:
                self.settingchanged.emit({'haspointstechnique': True, 'layerpointstechnique': layerpointstechnique[0]})

            else:
                self.settingchanged.emit({'haspointstechnique': False})
        else:
            self.settingchanged.emit({'haslayers': False})
        
        # Gather user information
        self.progressmsg.emit('Reconnaissance utilisateur...')

        self.progressmsg.emit('Initialization interface utilsateur...')
        for i in range(1, 100):
            sleep(0.01)
            self.progress.emit(i)
            self.opacity.emit(i/50)
        self.finished.emit()

class MetisLoading():
    
    def __init__(self, project, plugin_dir, version, parent=None):
        self.dlg = MetisQgisLoadingDialog()
        self.dlg.setWindowFlag(Qt.FramelessWindowHint)

        # self.dlg.setAttribute(Qt.WA_TranslucentBackground)
        self.dlg.setLayout(self.dlg.mainLayout)
        self.dlg.labelAuthor.setText('Joel PINHO ' + version)
        img = QPixmap(os.path.join(plugin_dir, 'icon64x64.png'))
        self.dlg.labelRaizeLogo.setPixmap(img)
        self.thread = QThread()
        self.worker = Worker(project)

        # set shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(5, 5)
    
        # self.dlg.labelRaizeLogo.setGraphicsEffect(shadow)
        
    def update_progress(self, value):
        self.dlg.progressBar.setValue(value)


    def run(self):
        self.dlg.show()
        self.dlg.setWindowOpacity(0)
        self.worker.moveToThread(self.thread)

        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.boot)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_progress)
        self.worker.opacity.connect(lambda opacity: self.update_window_opacity(opacity))
        # Step 6: Start the thread
        self.thread.start()

        
            
    def update_window_opacity(self, opacity):
        self.dlg.setWindowOpacity(opacity)

    def close(self):
        self.dlg.hide()
        
