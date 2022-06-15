from ..ui.metis_qgis_app_dialog import MetisQgisApdgcDialog
from .layout import (
    MetisLayout,
)
from .conts import (
    AUTHOR,
    AUTHOR_USER,
    GISNET_SHAPES,
    VERSION
)
import os
import math
import json
from .layout import (
    MetisLayout,
    
)
from .customwidgets import (
    TableWidget,
    Frame,
    VerticalLayout,
    HorizontalLayout,
    Button,
    Label,
)

from qgis.core import (
    QgsLayoutTableColumn,
    QgsLayoutTableStyle,
    QgsLayoutTable,
    QgsTextFormat,
    QgsLayoutFrame,
    QgsLayoutPoint,
    QgsUnitTypes,
    QgsLayoutSize,
    QgsLayoutItemMap,
    QgsRasterLayer,
    QgsRectangle,
    QgsLayoutItemShape,
    QgsFillSymbol,
    QgsLayoutItemPage,
    QgsLayoutItemAttributeTable,
    QgsLayoutItemTextTable,


)

from qgis.PyQt.QtCore import (
    QThread,
    QObject,
    pyqtSignal,
    QEvent,
    QRect,
    Qt,
    QSize,
)
from qgis.PyQt.QtWidgets import (
    QTableWidgetItem,
    QGraphicsDropShadowEffect,   
    QSpacerItem,
    QSizePolicy,
    QScrollArea,
    QComboBox,
    QLayout,
    QWidget,
)
from qgis.PyQt.QtGui import (
    QColor,
    QFont,
    QDropEvent,
    QPixmap,
    QCursor,
    QIcon,
    QPainter,
)


class Worker(QObject):

    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
    

    def init(self):
        pass


    def update_entities_list(self, settings):
        resentities = []
        projectentities = settings['layerpointstechnique'].getFeatures('"pt_typephy" = \'APPUI\'')
        
        for entitie in projectentities:
            resentities.append(entitie)

        return resentities
        
    def update_table(self, layer, table, filter):
        table.clear()
        table.setRowCount(0)
        
        feature = next(layer.getFeatures())
        attributes = next(layer.getFeatures()).attributes()
        columncount = len(attributes)
        
        headers = []
        for field in feature.fields():
            headers.append(field.displayName())

        table.setColumnCount(columncount)
        table.setHorizontalHeaderLabels(headers)

        # Generate rows 
        if filter == 'ALL':
            for layer in layer.getFeatures():
                currentrow = table.rowCount()
                table.setRowCount(currentrow + 1)
            
                col = 0
                for attr in layer.attributes():
                    cell = QTableWidgetItem(str(attr))
                    table.setItem(currentrow, col, cell)
                    col += 1

        elif filter == 'VDLF':
            for layer in layer.getFeatures('"pt_prop" = \'VDLN\' AND "pt_typephy" = \'APPUI\''):
                currentrow = table.rowCount()
                table.setRowCount(currentrow + 1)

                col = 0
                for attr in layer.attributes():
                    cell = QTableWidgetItem(str(attr))
                    table.setItem(currentrow, col, cell)
                    col += 1

        self.finished.emit()

class MetisApdgc():

    updated_selection = pyqtSignal(int)

    def __init__(self, settings, plugindir, stylepath):
        self.dlg = MetisQgisApdgcDialog()
        self.settings = settings
        self.plugindir = plugindir
        self.stylepath = stylepath
        self.currentfilter = 'VDLF'
        self.currentframe = 'info'
        self.selectedentities = []
        self.totalpages = 1
        self.totalentities = 0
        self.projectentities = []
        self.entitie = {
            'id': int(),
            'value': str(),
        }

        self.thread = QThread()
        self.worker = Worker()

        # styles
         # set shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(1, 1)

        
        self.dlg.lineEditSroname.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditCity.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditZipcode.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditInseecode.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditIndex.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditAuthor.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditAuthorDate.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditFci.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditTicketJira.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditCdc.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditCdcTel.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.lineEditCdcMail.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))
        self.dlg.comboBoxPhase.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=10, xOffset=1, yOffset=1))

        self.dlg.comboBoxPhase.setStyleSheet(
            
            "QComboBox {"
                "background-color: rgb(255, 255, 255);"
                "color: black;"
                "border: 0;"
                "border-radius: 5px;"
            "}"
            "QComboBox:focus {"
                "background-color: rgb(255, 255, 255);"
                "border: 1px solid rgb(50, 50, 50);"
            "}"
            "QComboBox:on {"
                "background-color: rgb(255, 255, 255);"
                "color: black;"
                "border: 1px solid rgb(50, 50, 50);"
            "}"
            "QComboBox:strong:focus {"
                "background-color: rgb(255, 255, 255);"
                "border: 1px solid rgb(50, 50, 50);"
            "}"
            "QComboBox:pressed {"
                "background-color: rgb(200, 200, 200);"
                "border: 0;"
            "}"
            "QComboBox:hover {"
                "background-color: rgb(255, 255, 255);"
                "color: black;"
                "border: 1px solid rgb(50, 50, 50);"
            "}"
            "QComboBox:disabled {"
                "background-color: rgb(150, 150, 150);"
                "border: 0;"
            "}"
            "QComboBox:down-arrow {"
                "background-color: rgb(255, 255, 255);"
                "border: 0;"
                # "padding: 5px;"
                "image: url(" + os.path.join(plugindir, 'images', 'icons', 'down_arrow.png') + ")"
            "}"
        )
        # init
        

        self.table = TableWidget()
        self.table.set_table_settings()
        self.table.reportchange.connect(lambda x: self.dlg.labelCurrentFilter.setText(x))

        self.dlg.setLayout(self.dlg.mainLayout)    
        self.dlg.frameListPoles.hide()
        self.dlg.frameListPoles.setLayout(self.dlg.verticalLayoutListPoles)
        
        self.dlg.frameInfo.setLayout(self.dlg.gridLayout)
        self.dlg.pushButtonInfo.clicked.connect(lambda: self.toogle_apdgc_frame('info'))
        self.dlg.pushButtonListPoles.clicked.connect(lambda: self.toogle_apdgc_frame('listpole'))
        self.dlg.pushButtonOrderPoles.clicked.connect(lambda: self.toogle_apdgc_frame('orderpole'))
    
        # self.thread.started.connect(lambda: self.worker.update_table(self.settings['layerpointstechnique'], self.table, self.currentfilter))
        self.thread.started.connect(lambda: self.worker.init)
        self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.update_label_current_filter)

        self.dlg.pushButtonFilterAll.clicked.connect(lambda: self.update_filter('ALL'))
        self.dlg.pushButtonFilterVDLF.clicked.connect(lambda: self.update_filter('VDLF'))

        # Replace icon back button
        icogoback = QIcon()
        imggoback = QPixmap(os.path.join(plugindir, 'images', 'icons', 'go-back.png'))
        icogoback.addPixmap(imggoback)
        imggoback.scaled(128, 64)
        self.dlg.pushButtonCancel.setText('')
        icosize = QSize()
        icosize.scale(32, 32, Qt.KeepAspectRatio)
        self.dlg.pushButtonCancel.setIconSize(icosize)
        self.dlg.pushButtonCancel.setIcon(icogoback)
        # Tests with new frame
        self.frameOrderPoles = Frame()
        self.frameOrderPoles.hide()
        self.frameOrderPoles.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.framelayout = VerticalLayout()
        self.pushButtonAddPole = Button()
        self.pushButtonAddPole.setObjectName('pushButtonAddPole')
        self.pushButtonAddPole.setText('Ajouter Entité')
        self.pushButtonAddPole.setMinimumHeight(35)

        self.vspacer = QSpacerItem(30, 30, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.vvspacer = QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.Expanding)
        

        self.scrollarea = QScrollArea()
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.scrollarea.setSizeAdjustPolicy(QScrollArea.AdjustToContents)

        self.scrollareawidget = QWidget()
        # self.scrollareawidget.setGeometry(QRect(100, 100, 1000, 100))
        self.scrollareawidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.scrollarealayout = VerticalLayout()
        self.scrollarealayout.addItem(self.vvspacer)
        self.scrollarea.setWidget(self.scrollareawidget)

        self.scrollareawidget.setLayout(self.scrollarealayout)

        self.framelayout.addWidget(self.scrollarea)
        self.framelayout.addItem(self.vspacer)
        self.framelayout.addWidget(self.pushButtonAddPole)
        
        self.frameOrderPoles.setLayout(self.framelayout)
        self.dlg.mainLayout.insertWidget(2, self.frameOrderPoles)

        self.pushButtonAddPole.clicked.connect(self.add_entitie_toscreen)
        
        # DEBUG
        self.labeldebug = Label()
        self.labeldebug.setText('DEBUG')
        self.dlg.mainLayout.insertWidget(1, self.labeldebug)

        self.thread.start()
        self.worker.moveToThread(self.thread)

        if settings['haspointstechnique']:
            self.projectentities = self.worker.update_entities_list(self.settings)


    # def dragEvent(self, e):
    #     e.accept()
    #     self.dlg.labelCurrentFilter.setText('Test')


    # def keyPressEvent(self, e):
    #     e.accept()
    #     self.dlg.labelCurrentFilter.setText('Test')
        
    def update_filter(self, filter):
        self.currentfilter = filter
        self.worker.update_table(self.settings['layerpointstechnique'], self.table, filter)

    # def update_entities_list(self):
    #     projectentities = self.settings['layerpointstechnique'].getFeatures('"pt_typephy" = \'APPUI\'')

    #     for entitie in projectentities:
    #         self.projectentities.append(entitie)

    def update_label_current_filter(self):
        self.dlg.labelCurrentFilter.setText('Selection en cours : ' + self.currentfilter)
    

    def update_selection(self, value):
        self.labeldebug.setText(str(value))
        childlayout = self.scrollarealayout.itemAt(value-1)
        cbbox = childlayout.itemAt(0)

        # self.labeldebug.setText(str(cbbox))

        
    def add_entitie_toscreen(self):
        """
            Adds new entitie that will go into the final layout
        """
        self.totalentities += 1
        self.totallayerentities = 0
        id = self.totalentities

        newentitielayout = HorizontalLayout()
        newentitielayout.setSizeConstraint(QLayout.SetFixedSize)


        labelimg = Label()
        imgdrag = QPixmap(os.path.join(self.plugindir, 'images', 'icons', 'drag.png'))
        # imgdrag.scaledToWidth(32, Qt.FastTransformation)
        labelimg.setPixmap(imgdrag)
        dragcursor = QCursor()
        dragcursor.setShape(Qt.OpenHandCursor)
        labelimg.setCursor(dragcursor)
        labelimg.setEnabled(False)

        label = Label()
        label.setText(str(self.totalentities))
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        label.setMinimumSize(20, 20)
        

        combobox = QComboBox()
        combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        combobox.setMinimumSize(30, 30)
        combobox.setMaximumHeight(32)
        combobox.setEditable(True)
        for entitie in self.projectentities:
            combobox.addItem(entitie.attributes()[0])

        combobox.activated.connect(lambda: self.update_selection(id))

        
        newentitielayout.addWidget(labelimg)
        newentitielayout.addWidget(label)
        newentitielayout.addWidget(combobox)
        
        self.scrollarealayout.insertLayout(self.totalentities-1, newentitielayout)
    

    def prepare_apdgc_data(self):
        data = {}

        data['project'] = self.dlg.lineEditSroname.text()
        data['phase'] = self.dlg.comboBoxPhase.currentText()
        data['city'] = self.dlg.lineEditCity.text()
        data['zipcode'] = self.dlg.lineEditZipcode.text()
        data['inseecode'] = self.dlg.lineEditInseecode.text()
        data['index'] = self.dlg.lineEditIndex.text()
        data['author'] = self.dlg.lineEditAuthor.text()
        data['authordate'] = self.dlg.lineEditAuthorDate.text()
        data['cdc'] = self.dlg.lineEditCdc.text()
        data['cdctel'] = self.dlg.lineEditCdcTel.text()
        data['cdcmail'] = self.dlg.lineEditCdcMail.text()

        if self.dlg.lineEditFci.text():
            data['fci'] = self.dlg.lineEditFci.text()
        else:
            data['fci'] = '___________________'
        data['ticketjira'] = self.dlg.lineEditTicketJira.text()

        if self.dlg.checkBoxBonComm.isChecked():
            data['boncom'] = 'Oui'
        else:
            data['boncom'] = 'Non'

        return data

    def toogle_apdgc_frame(self, frame):
        if frame == self.currentframe:
            return

        if frame == 'info':
            if self.currentframe == 'listpole':
                self.dlg.frameListPoles.hide()
            elif self.currentframe == 'orderpole':
                self.frameOrderPoles.hide()

            self.currentframe = 'info'
            self.dlg.frameInfo.show()

        elif frame == 'listpole':
            if self.currentframe == 'info':
                self.dlg.frameInfo.hide()
            elif self.currentframe == 'orderpole':
                self.frameOrderPoles.hide()

            self.currentframe = 'listpole'
            self.dlg.frameListPoles.show()

        elif frame == 'orderpole':
            if self.currentframe == 'info':
                self.dlg.frameInfo.hide()
            elif self.currentframe == 'listpole':
                self.dlg.frameListPoles.hide()

            self.currentframe = 'orderpole'
            self.frameOrderPoles.show()

    def init_dlg(self, layer):
        # add poles to table
            if self.settings['haspointstechnique']:
                feature = next(layer.getFeatures())
                attributes = next(layer.getFeatures()).attributes()
                columncount = len(attributes)
                
                headers = []
                for field in feature.fields():
                    headers.append(field.displayName())

                self.table.setColumnCount(columncount)
                self.table.setHorizontalHeaderLabels(headers)

                # Generate rows 
                for layer in layer.getFeatures('"pt_prop" = \'VDLN\' AND "pt_typephy" = \'APPUI\''):
                    currentrow = self.table.rowCount()
                    self.table.setRowCount(currentrow + 1)

                    col = 0
                    for attr in layer.attributes():
                        cell = QTableWidgetItem(str(attr))
                        self.table.setItem(currentrow, col, cell)
                        col += 1

                self.dlg.verticalLayoutMainListPoles.addWidget(self.table)
                self.dlg.labelCurrentFilter.setText('Sélection en cours : ' + self.currentfilter)
    
    def run(self):
        self.dlg.show()

    def close(self):
        self.dlg.hide()

    def generate_apdgc_layout(self,
        qgsproj,
        data,
        nbvdlf,
        iface,
        ):
        """
            Generate the apdgc layout
        """
        
        nlayout = MetisLayout(qgsproj)
        layout = nlayout.layout

        layout.setName(data['project'] + '_DTPGC')
        
        pathlogocgti = os.path.join(self.stylepath, 'logo_cgti.jpg')
        pathlogovdlf = os.path.join(self.stylepath , 'logo_vdlf.jpg')
        pathlogotdf = os.path.join(self.stylepath, 'logo_tdf.png')
        pathlogoqrcode = os.path.join(self.stylepath, 'qrcode.png')
        pathlogonorth = os.path.join(self.stylepath, 'logo_north.svg')
        pathpole = os.path.join(self.stylepath, 'pole.jpg')
        
        """
            Main page
        """

        nlayout.change_page_settings(0, 'A4', 'portrait')
        # Position CGTI logo
        logocgti = nlayout.generate_image('image_logo_cgti', pathlogocgti, 7, 8, 800, 320)
        layout.addLayoutItem(logocgti)

        # Position VDLF logo
        logovdlf = nlayout.generate_image('image_logo_vdlf', pathlogovdlf, 170.9, 8, 380, 205)
        layout.addLayoutItem(logovdlf)

        # Position TDF logo
        logotdf = nlayout.generate_image('image_logo_vdlf', pathlogotdf, 179.2, 25.5, 182, 181)
        layout.addLayoutItem(logotdf)

        # Position QR logo
        logoqrcode = nlayout.generate_image('image_logo_tdf', pathlogoqrcode, 80.1, 13.1, 197.2, 197.2)
        layout.addLayoutItem(logoqrcode)

        # Divisor
        divrect = nlayout.generate_shape('shape_diviseur', 1, QColor(0, 140, 0, 0), 34.6, 45.9, 140, 0.2)
        layout.addLayoutItem(divrect)

        """
            Main text
        """
        # Fonts

        # Big bold
        fontbigbold = QFont()
        fontbigbold.setFamily('Ubuntu')
        fontbigbold.setBold(True)
        fontbigbold.setPixelSize(80)

        # normam title
        fontbigregular = QFont()
        fontbigregular.setFamily('Ubuntu')
        fontbigregular.setPixelSize(80)

        # regular bold
        fontnormalbold = QFont()
        fontnormalbold.setFamily('Ubuntu')
        fontnormalbold.setBold(True)
        fontnormalbold.setPixelSize(40)

        # normam title
        fontnormal = QFont()
        fontnormal.setFamily('Ubuntu')
        fontnormal.setPixelSize(40)
        
        # small
        fontsmallbold = QFont()
        fontsmallbold.setFamily('Ubuntu')
        fontsmallbold.setBold(True)
        fontsmallbold.setPixelSize(30)

        # small
        fontsmall = QFont()
        fontsmall.setFamily('Ubuntu')
        fontsmall.setPixelSize(30)
        
        # smaller bold
        fontsmallerbold = QFont()
        fontsmallerbold.setFamily('Ubuntu')
        fontsmallerbold.setBold(True)
        fontsmallerbold.setPixelSize(25)

        # smaller
        fontsmaller = QFont()
        fontsmaller.setFamily('Ubuntu')
        fontsmaller.setPixelSize(25)

        # small opacity
        fontsmallopac = QFont()
        fontsmallopac.setFamily('Ubuntu')
        fontsmallopac.setPixelSize(30)
        


        # Label version / creator
        labelversioncreat = nlayout.generate_label('text_version_createur_page_de_garde', AUTHOR_USER + ' - ' + VERSION, 7, 4, 30, 5, fontsmallopac, fontcolor=QColor(0, 0, 0, 40))
        layout.addLayoutItem(labelversioncreat)

        # Label prompt project
        labelpromptproject = nlayout.generate_label('text_projet_page_garde', 'Projet :', 50.6, 50, 50, 10, fontbigbold)
        layout.addLayoutItem(labelpromptproject)

        # Label prompt project
        labelproject = nlayout.generate_label('text_projet_phase_page_garde', data['project'] + '-' + data['phase'], 79.6, 50, 80, 10, fontbigregular)
        layout.addLayoutItem(labelproject)

        # Label prompt city
        labelpromptcity = nlayout.generate_label('text_commune_avant_page_garde', 'Commune :', 34.6, 70, 22, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptcity)

        # Label city
        labelcity = nlayout.generate_label('text_commune_page_garde', data['city'], 58, 70, 30, 5, fontnormal)
        layout.addLayoutItem(labelcity)

        # Label prompt zipcode
        labelpromptzipcode = nlayout.generate_label('text_code_post_avant_page_garde', 'Code postal :', 34.6, 80, 26, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptzipcode)

        # Label zipcode
        labelzipcode = nlayout.generate_label('text_code_post_page_garde', data['zipcode'], 61, 80, 25, 5, fontnormal)
        layout.addLayoutItem(labelzipcode)

        # Label prompt inseecode
        labelpromptinseecode = nlayout.generate_label('text_code_insee_avant_page_garde', 'Code Insee :', 34.6, 90, 24, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptinseecode)

        # Label inseecode
        labelinseecode = nlayout.generate_label('text_code_insee_page_garde', data['inseecode'], 59.5, 90, 25, 5, fontnormal)
        layout.addLayoutItem(labelinseecode)

        # Label prompt indice
        labelpromptindice = nlayout.generate_label('text_indice_avant_page_garde', 'Indice :', 120.6, 70, 15, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptindice)

        # Label indice
        labelindice = nlayout.generate_label('text_indice_page_garde', data['index'], 135.2, 70, 10, 5, fontnormal)
        layout.addLayoutItem(labelindice)

        # Label prompt author
        labelpromptauthor = nlayout.generate_label('text_realis_avant_page_garde', 'Réalisé par :', 120.6, 80, 30, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptauthor)
        
        # Label author
        labelauthor = nlayout.generate_label('text_realis_page_garde', data['author'], 145.2, 80, 25, 5, fontnormal)
        layout.addLayoutItem(labelauthor)

        # Label prompt author date
        labelpromptauthordate = nlayout.generate_label('text_edit_avant_page_garde', 'Edité le :', 120.6, 90, 25, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptauthordate)

        # self.manager.addLayout(layout)

        # Label author date
        labelauthordate = nlayout.generate_label('text_edit_page_garde', data['authordate'], 138.6, 90, 18.1, 5, fontnormal)
        layout.addLayoutItem(labelauthordate)

        # Label prompt mark field date
        labelpromptmarkfield = nlayout.generate_label('text_marq_avant_page_garde', 'Marquage le :', 34.6, 110, 36, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptmarkfield)

        # Label mark field date
        labelmarkfield = nlayout.generate_label('text_marq_page_garde', '___ /___ /___', 62.6, 110, 35.5, 5, fontnormal)
        layout.addLayoutItem(labelmarkfield)

        # Label prompt work field date
        labelpromptworkfield = nlayout.generate_label('text_travaux_avant_page_garde', 'Travaux le :', 34.6, 120, 32, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptworkfield)

        # Label prompt work field date
        labelworkfield = nlayout.generate_label('text_travaux_page_garde', '___ /___ /___', 58, 120, 36, 5, fontnormal)
        layout.addLayoutItem(labelworkfield)

        # Label prompt cond work
        labelpromptcondwork = nlayout.generate_label('text_cdc_nom_avant_page_garde', 'Conducteur Travaux :', 120.6, 110, 80, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptcondwork)

        # Label prompt cond name
        labelcondname = nlayout.generate_label('text_cdc_nom_page_garde', data['cdc'], 120.6, 120, 80, 5, fontnormal)
        layout.addLayoutItem(labelcondname)

        # Label prompt cond tel
        labelcondtel = nlayout.generate_label('text_cdc_tel_page_garde', data['cdctel'], 120.6, 125, 80, 5, fontnormal)
        layout.addLayoutItem(labelcondtel)

        # Label cond mail
        labelcondmail = nlayout.generate_label('text_cdc_mail_page_garde', data['cdcmail'], 120.6, 130, 80, 5, fontnormal)
        layout.addLayoutItem(labelcondmail)
        
        # Label prompt total poles vdlf
        labelprompttotalvdlfpoles = nlayout.generate_label('text_appuis_vdlf_page_garde', 'Appuis VDLF :', 34.6, 144, 28, 5, fontnormalbold)
        layout.addLayoutItem(labelprompttotalvdlfpoles)

        # Label total poles vdlf
        labeltotalvdlfpoles = nlayout.generate_label('text_appuis_vdlf_page_garde', str(nbvdlf), 62.3, 144, 28, 5, fontnormal)
        layout.addLayoutItem(labeltotalvdlfpoles)

        # Table VDLF poles
        tablevdlfpoles = QgsLayoutItemTextTable(layout)

        layout.addMultiFrame(tablevdlfpoles)

        # Add columns       
        cols = [QgsLayoutTableColumn(),QgsLayoutTableColumn(),QgsLayoutTableColumn(), QgsLayoutTableColumn()]
        cols[0].setHeading("Nature")
        cols[0].setWidth(30)

        cols[1].setHeading("Hauteur")
        cols[1].setWidth(30)

        cols[2].setHeading("Unité")
        cols[2].setWidth(30)

        cols[3].setHeading("Quantité")
        cols[3].setWidth(30)

        tablevdlfpoles.setColumns(cols)

        # Add only 1 row
        tablevdlfpoles.setContents([['Bois', '7', 'U', '0'], ['Bois', '8', 'U', '0']])

        table_style = QgsLayoutTableStyle()
        table_style.enabled = True
        table_style.cellBackgroundColor = QColor(40, 40, 40, 255)
        tablevdlfpoles.setCellStyle(QgsLayoutTable.HeaderRow, table_style)

        headerformat = QgsTextFormat()
        headerformat.setColor(QColor(255, 255, 255, 255))
        headerformat.setFont(QFont('Ubuntu', 20, 100))

        tablevdlfpoles.setHeaderTextFormat(headerformat)
        tablevdlfpoles.setHeaderHAlignment(QgsLayoutTable.HeaderHAlignment.HeaderCenter)

        # Base class for frame items, which form a layout multiframe item.
        frame = QgsLayoutFrame(layout, tablevdlfpoles)
        frame.attemptMove(QgsLayoutPoint(34.6, 150, QgsUnitTypes.LayoutMillimeters))
        frame.attemptResize(QgsLayoutSize(20, 20), True)
        tablevdlfpoles.addFrame(frame)

        # Coordinate prompt label
        labelpromptcoordinate = nlayout.generate_label('text_sys_coord_avant_page_garde', 'Systéme coordonnées :', 7, 173.5, 27.3, 4, fontsmallerbold)
        layout.addLayoutItem(labelpromptcoordinate)

        # Coordinate label
        labelcoordinate = nlayout.generate_label('text_sys_coord_page_garde', '[%item_variables(\'fullview_map\')[\'map_crs_description\']%]', 35, 173.5, 27.3, 4, fontsmaller)
        layout.addLayoutItem(labelcoordinate)

        # Full view map
        fullviewmap = QgsLayoutItemMap(layout)
        
        layers = qgsproj.mapLayers().values()
        layerfvmap = []
        for layer in layers:
            if layer.name() in GISNET_SHAPES:
                layerfvmap.append(layer)
        
        # try:
        #     layerfvmap.append(qgsproj.mapLayersByName('OpenStreetMap')[0])
        # except IndexError as err:
        #     uri = "type=xyz&url=https://tile.openstreetmap.org/\{z\}/\{x\}/\{y\}.png"
        #     vlayer = QgsRasterLayer(uri, "OpenStreetMap", "wms")
        #     qgsproj.addMapLayer(vlayer)

        #     self.print_to_console('OpenStreetMap manquant')

        fullviewmap.setRect(20, 20, 20, 20)
        fullviewmap.setId('fullview_map')
        rectangle = QgsRectangle(1355502, -46398, 1734534, 137094)
        fullviewmap.setExtent(rectangle)
        fullviewmap.setLayers(layerfvmap)
        layout.addLayoutItem(fullviewmap)

        canvas = iface.mapCanvas()

        fullviewmap.setExtent(canvas.extent())
        # self.dlg.logTextEdit.appendPlainText(str(canvas.extent().center()))
        
        fullviewmap.setFrameEnabled(True)

        layout.addLayoutItem(fullviewmap)
        
        # fullviewmap.setExtent(canvas.extent().center())

        fullviewmap.attemptMove(QgsLayoutPoint(7, 177, QgsUnitTypes.LayoutMillimeters))
        fullviewmap.attemptResize(QgsLayoutSize(*[196, 100], QgsUnitTypes.LayoutMillimeters))
        
        # Position north logo
        logonorth = nlayout.generate_image('image_fleche_nord_page_garde', pathlogonorth, 15, 185, 151, 220)
        layout.addLayoutItem(logonorth)
        
        # bg scale
        props = {}
        props["color"] = QColor(0, 0, 0, 20)
        props["style"] = "solid"
        props["style_border"] = "no"
        props["color_border"] = "black"
        props["width_border"] = "0"
        props["joinstyle"] = "miter"

        divrect = QgsLayoutItemShape(layout)
        divrect.setShapeType(1)

        divrect.attemptMove(QgsLayoutPoint(163, 262.3, QgsUnitTypes.LayoutMillimeters))
        divrect.attemptResize(QgsLayoutSize(*[34, 10], QgsUnitTypes.LayoutMillimeters))
        divrect.setFrameEnabled(False)
        
        sm = QgsFillSymbol.createSimple(props)
        divrect.setSymbol(sm)
        layout.addLayoutItem(divrect)

        # label scale
        labelscale = nlayout.generate_label('text_echelle_page_garde', 'Echelle : [%round(item_variables(\'fullview_map\')[\'map_scale\'])%]', 166, 265, 32.6, 7.3, fontnormalbold)
        layout.addLayoutItem(labelscale)


        # Label nb pages
        labelnbpages = nlayout.generate_label('text_nb_page_page_garde', '[%@layout_page%] / [%@layout_numpages%]', 190.4, 284.5, 12.5, 5, fontnormal)
        layout.addLayoutItem(labelnbpages)

        # Label FCI prompt
        labelpromptfci = nlayout.generate_label('text_fci_avant_page_garde', 'FCI :', 7, 282, 10, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptfci)
        
        # Label FCI
        labelfci = nlayout.generate_label('text_fci_page_garde', data['fci'], 17, 282, 50, 5, fontnormal)
        layout.addLayoutItem(labelfci)

        # Label commande prompt
        labelpromptcom = nlayout.generate_label('text_bon_comm_avant_page_garde', 'Bon commande :', 65, 282, 37, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptcom)

        # Label commande
        labelcom = nlayout.generate_label('text_bon_comm_page_garde', data['boncom'], 102, 282, 10, 5, fontnormal)
        layout.addLayoutItem(labelcom)

        # Label jira ticket prompt
        labelpromptjira = nlayout.generate_label('text_jira_avant_page_garde', 'Ticket JIRA :', 7, 287, 25, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptjira)

        # Label jira ticket 
        labeljira = nlayout.generate_label('text_jira_page_garde', data['ticketjira'], 32, 287, 25, 5, fontnormal)
        layout.addLayoutItem(labeljira)

        # Label utilisateur prompt
        labelpromptuser = nlayout.generate_label('text_user_avant_page_garde', 'Utilisateur :', 60, 287, 23, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptuser)

        # Label utilisateur 
        labeluser = nlayout.generate_label('text_user_page_garde', '[%@user_full_name%]', 83, 287, 25, 5, fontnormal)
        layout.addLayoutItem(labeluser)

        # Label date prompt
        labelpromptdate = nlayout.generate_label('text_date_log_avant_page_garde', 'Date journal :', 100, 287, 30, 5, fontnormalbold)
        layout.addLayoutItem(labelpromptdate)

        # Label date 
        labeldate = nlayout.generate_label('text_date_log_page_garde', '[%format_date(now(), \'yyyy-MM-dd\')%]', 127, 287, 23, 5, fontnormal)
        layout.addLayoutItem(labeldate)
        
        # Calculate needed pages
        nbpolepages = math.ceil(nbvdlf / 3)
        features = qgsproj.mapLayersByName('pointstechnique')[0].getFeatures('"pt_prop" = \'VDLN\' AND "pt_typephy" = \'APPUI\'')
        # self.dlg.logTextEdit.appendPlainText(str(nbpolepages))
        
        polecounter = 0

        for nbpage in range(1, nbpolepages + 1):
            newpage = QgsLayoutItemPage(layout)
            newpage.setPageSize('A4', QgsLayoutItemPage.Portrait)
            layout.pageCollection().addPage(newpage)

            self.totalpages = self.totalpages + 1
            currentpage = layout.pageCollection().page(nbpage)

            # Position CGTI logo
            logocgtisec = nlayout.generate_image('image_logo_cgti_page' + str(nbpage), pathlogocgti, 7, 8, 500, 220, nbpage=nbpage)
            layout.addLayoutItem(logocgtisec)

            # SRO + phase
            labelprojectsec = nlayout.generate_label('text_projet_phase_page' + str(nbpage), data['project'] + '-' + data['phase'], 166, 8, 37, 6, fontnormal, nbpage=nbpage)
            layout.addLayoutItem(labelprojectsec)

            # Label nb pages
            labelnbpages = nlayout.generate_label('text_nbpage_page' + str(nbpage), '[%@layout_page%] / [%@layout_numpages%]', 190.4, 284.5, 12.5, 5, fontnormal, nbpage=nbpage)
            layout.addLayoutItem(labelnbpages)

            # Maybe use the QgsFeatureIterator to get 3 poles each time
        
            
            """
                VDLF POLES
            """
            START_POSX = 7
            START_POSY = 35
            
            for i in range(3):
                
                try:
                    currentfeature = next(features)
                except StopIteration:
                    break
                
                if i == 1:
                    calcposx = START_POSX
                    calcposy = START_POSY + 80
                elif i == 2:
                    calcposx = START_POSX
                    calcposy = START_POSY + 160
                else:
                    calcposx = START_POSX
                    calcposy = START_POSY

                # Label prompt gisnet code
                labelpromptgisnetcode = nlayout.generate_label('text_appui' + str(i) + '_ptcode_avant_page' + str(nbpage), 'Code gisnet :', calcposx, calcposy, 25, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelpromptgisnetcode)

                # Label gisnet code
                labelpromptgisnetcode = nlayout.generate_label('text_appui' + str(i) + '_ptcode_page' + str(nbpage), str(currentfeature.attributes()[0]), calcposx + 20, calcposy, 36, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labelpromptgisnetcode)
        
                # Label prompt adress
                labelpromptadress = nlayout.generate_label('text_appui' + str(i) + '_adresse_avant_page' + str(nbpage), 'Adresse :', calcposx + 59.1, calcposy, 15.1, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelpromptadress)

                # Label adress
                labeladress = nlayout.generate_label('text_appui' + str(i) + '_adresse_page' + str(nbpage), str(currentfeature.attributes()[20]), calcposx + 73, calcposy, 100, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labeladress)

                # Label prompt X
                labelpromptx = nlayout.generate_label('text_appui' + str(i) + '_x_avant_page' + str(nbpage), 'X :', calcposx, calcposy + 5, 10.1, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelpromptx)
                
                coordinates = json.loads(currentfeature.geometry().asJson())['coordinates']

                # Label X
                labelx = nlayout.generate_label('text_appui' + str(i) + '_coord_avant_page' + str(nbpage), str(coordinates[0]), calcposx + 4, calcposy + 5, 20, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labelx)
                
                # Label Y prompt description
                labelprompty = nlayout.generate_label('text_appui' + str(i) + '_y_avant_page' + str(nbpage), 'Y :', calcposx + 24, calcposy + 5, 10.1, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelprompty)
                
                # Label Y
                labely = nlayout.generate_label('text_appui' + str(i) + '_y_page' + str(nbpage), str(coordinates[1]), calcposx + 28, calcposy + 5, 20, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labely)

                # Label prompt description
                labelpromptdescript = nlayout.generate_label('text_appui' + str(i) + 'descript_avant_page' + str(nbpage), 'Description :', calcposx + 50, calcposy + 5, 20.1, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelpromptdescript)
                
                # Label description
                labeldescript = nlayout.generate_label('text_appui' + str(i) + '_descript_page' + str(nbpage), 'Bois 7m', calcposx + 69.3, calcposy + 5, 20, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labeldescript)

                # Label prompt noeud
                labelpromptnoeud = nlayout.generate_label('text_appui' + str(i) + '_noeud_avant_page' + str(nbpage), 'Noeud :', calcposx + 84, calcposy + 5, 12.1, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelpromptnoeud)
                
                # Label noeud
                labelnoeud = nlayout.generate_label('text_appui' + str(i) + '_noeud_page' + str(nbpage), 'BDI-00', calcposx + 95.6, calcposy + 5, 10, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labelnoeud)
                
                # Label prompt reason
                labelpromptreason = nlayout.generate_label('text_appui' + str(i) + '_motif_avant_page' + str(nbpage), 'Motif :', calcposx + 109, calcposy + 5, 12.1, 5, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelpromptreason)
                
                # Label reason
                labelreason = nlayout.generate_label('text_appui' + str(i) + '_motif_page' + str(nbpage), 'Création', calcposx + 118.7, calcposy + 5, 13, 5, fontsmall, nbpage=nbpage)
                layout.addLayoutItem(labelreason)

                # Position pole photo
                polephoto = nlayout.generate_image('image_appui' + str(i) + '_page' + str(nbpage), pathpole, calcposx, calcposy + 13, 567, 674, nbpage=nbpage)
                layout.addLayoutItem(polephoto)

                # Per pole map
                perpolemap = QgsLayoutItemMap(layout)
                perpolemap.setRect(20, 20, 20, 20)
                perpolemap.setId('perpole_map' + str(polecounter))
                perpolemap.setFrameEnabled(True)

                rectangle = QgsRectangle(1355502, -46398, 1734534, 137094)
                perpolemap.setExtent(rectangle)

                layout.addLayoutItem(perpolemap)

                canvas = iface.mapCanvas()

                perpolemap.setExtent(canvas.extent())


                layout.addLayoutItem(perpolemap)
            
                # perpolemap.setExtent(canvas.extent().center())

                perpolemap.attemptMove(QgsLayoutPoint(calcposx + 48, calcposy + 13, QgsUnitTypes.LayoutMillimeters), page=nbpage)
                perpolemap.attemptResize(QgsLayoutSize(*[148, 57], QgsUnitTypes.LayoutMillimeters))

                # Position north logo per pole
                logonorthperpole = nlayout.generate_image('image_appui' + str(i) + '_flech_nord_page' + str(nbpage), pathlogonorth, calcposx + 50, calcposy + 15, 70, 140, nbpage=nbpage)
                layout.addLayoutItem(logonorthperpole)

                # bg scale per pole 
                props = {}
                props["color"] = QColor(0, 0, 0, 20)
                props["style"] = "solid"
                props["style_border"] = "no"
                props["color_border"] = "black"
                props["width_border"] = "0"
                props["joinstyle"] = "miter"

                divrectperpole = QgsLayoutItemShape(layout)
                divrectperpole.setShapeType(1)

                divrectperpole.attemptMove(QgsLayoutPoint(calcposx + 164.5, calcposy + 59.5, QgsUnitTypes.LayoutMillimeters), page=nbpage)
                divrectperpole.attemptResize(QgsLayoutSize(*[24.4, 6.6], QgsUnitTypes.LayoutMillimeters))
                divrectperpole.setFrameEnabled(False)
                
                sm = QgsFillSymbol.createSimple(props)
                divrectperpole.setSymbol(sm)
                layout.addLayoutItem(divrectperpole)

                # label scale per pole 
                labelscaleperpole = nlayout.generate_label('text_appui' + str(i) + '_echelle_page' + str(nbpage), 'Echelle : [%round(item_variables(\'perpole_map' + str(polecounter) + '\')[\'map_scale\'])%]', calcposx + 166.4, calcposy + 61.1, 32.6, 7.3, fontsmallbold, nbpage=nbpage)
                layout.addLayoutItem(labelscaleperpole)

                polecounter += 1

            

        newpage = QgsLayoutItemPage(layout)
        newpage.setPageSize('A4', QgsLayoutItemPage.Portrait)
        layout.pageCollection().addPage(newpage)

        self.totalpages = self.totalpages 
        currentpage = layout.pageCollection().page(self.totalpages)

        # Position CGTI logo
        logocgtisec = nlayout.generate_image('image_logo_cgti_page' + str(self.totalpages), pathlogocgti, 7, 8, 500, 220, nbpage=self.totalpages)
        layout.addLayoutItem(logocgtisec)

        # SRO + phase
        labelprojectsec = nlayout.generate_label('text_project_phase_page' + str(self.totalpages), data['project'] + '-' + data['phase'], 166, 8, 37, 6, fontnormal, nbpage=self.totalpages)
        layout.addLayoutItem(labelprojectsec)

        # Label nb pages
        labelnbpages = nlayout.generate_label('text_nbpages_page' + str(self.totalpages), '[%@layout_page%] / [%@layout_numpages%]', 190.4, 284.5, 12.5, 5, fontnormal, nbpage=self.totalpages)
        layout.addLayoutItem(labelnbpages)
        
        # VDLF pole table
        attrtable = QgsLayoutItemAttributeTable(layout)
    
        layout.addMultiFrame(attrtable)
        attrtable.setVectorLayer(qgsproj.mapLayersByName('pointstechnique')[0])
        attrtable.setMaximumNumberOfFeatures(45)
        attrtable.setDisplayedFields(["pt_code", "pt_codeext", "pt_nbboites", "pt_statut", "pt_adresse"])
        attrtable.setFeatureFilter('"pt_prop" = \'VDLN\' AND "pt_typephy" = \'APPUI\'')
        attrtable.setFilterFeatures(True)

        table_style = QgsLayoutTableStyle()
        table_style.enabled = True
        table_style.cellBackgroundColor = QColor(40, 40, 40, 255)
        attrtable.setCellStyle(QgsLayoutTable.HeaderRow, table_style)

        headerformat = QgsTextFormat()
        headerformat.setColor(QColor(255, 255, 255, 255))
        headerformat.setFont(QFont('Ubuntu', 20, 100))

        attrtable.setHeaderTextFormat(headerformat)
        attrtable.setHeaderHAlignment(QgsLayoutTable.HeaderHAlignment.HeaderCenter)

        frame = QgsLayoutFrame(layout, attrtable)
        frame.attemptMove(QgsLayoutPoint(7, 25.7, QgsUnitTypes.LayoutMillimeters), page=self.totalpages)
        frame.attemptResize(QgsLayoutSize(634.2, 249.6), True)

        attrtable.addFrame(frame)
        
        # self.dlg.logTextEdit.appendPlainText(str(attrtable.setMaximumNumberOfFeatures()))
        # calculateMaxRowHeights()

        # nattrtable = attrtable.create(layout)

        # layout.add(nattrtable)
        # Generate layout per city then
            
        # Add layout
        return layout