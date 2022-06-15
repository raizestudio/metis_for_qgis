from .stylesheets import (
    BUTTON_GENERAL
)
from qgis.PyQt.QtCore import (
    QThread,
    QObject,
    pyqtSignal,
    Qt,
)

from qgis.PyQt.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QComboBox,
    QCheckBox,
    QAbstractButton,

)

from qgis.PyQt.QtGui import (
    QColor,
    QFont,
    QDropEvent,
    QCursor,

)

CURSOR_POINTER = QCursor().setShape(Qt.PointingHandCursor)

class TableWidget(QTableWidget):

    reportchange = pyqtSignal(str)

    def __init(self, parent=None):
        super(self).__init__(parent)
        
        
    def set_table_settings(self):
        self.setDragDropOverwriteMode(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.setDefaultDropAction(Qt.IgnoreAction)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.clicked.connect(self.change_order)

    def change_order(self):
        self.reportchange.emit(str(self.item(self.currentItem().row(), 0).text()))

    # def dropEvent(self, e):
    #     e.accept()
    #     self.reportchange.emit(str(e))

    # def dragMoveEvent(self, e):
    #     e.accept()
    #     self.reportchange.emit(str(e.pos()))

    # def dragEnterEvent(self, e):
    #     e.accept()
    #     self.reportchange.emit(str(self.currentItem().row() + 1))

    def reset_table(self):
        self.setRowCount(0)
        self.setColumnCount(0)

class TableWidgetItem(QTableWidgetItem):

    def __init__(self, parent=None):
        super(self).__init__(parent)

class Frame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

class HorizontalLayout(QHBoxLayout):

    def __init__(self, parent=None):
        super().__init__(parent)

class VerticalLayout(QVBoxLayout):

    def __init__(self, parent=None):
        super().__init__(parent)

class Button(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(BUTTON_GENERAL)
        self.setCursor(Qt.PointingHandCursor)

class Label(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)

class ComboBox(QComboBox):

    def __init__(self, parent=None):
        super(self).__init__(parent)