# ########################################################################### #
# 22 MODERN UI
# QT GUI BY SPINN TV(YOUTUBE)
# ########################################################################### #

# ########################################################################### #
# IMPORTS
# ########################################################################### #
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from time import sleep
from PyQt5 import QtCore, QtWidgets
from threading import Thread
import sys
import os
from codigo.functions_program import *

# ########################################################################### #
# IMPORT GUI GILE
from ui_interface_22_modern_tutorial import *
# ########################################################################### #


########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


# ########################################################################### #
# MAIN WINDOW CLASS
# ########################################################################### #


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(900, 600)

        #######################################################################
        # APPLY JSON STYLESHEET
        #######################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        #######################################################################

        # ################################################################### #
        # show window
        # ################################################################### #
        self.show()

        # EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingsBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET
        self.ui.closeCenterMenuBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(
            lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(
            lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(
            lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(
            lambda: self.ui.popupNotificationContainer.collapseMenu())

        # BUTTONS
        self.ui.importCsvOmieBtn.clicked.connect(
            lambda: thread_read_omie_sheet()
        )

        self.ui.exportCsvOmieToHdBtn.clicked.connect(
            lambda: thread_export_excel_sheet_omie()
        )

        self.ui.createTable_databaseBtn.clicked.connect(
            lambda: createTable_database_basic()
        )

        self.ui.createTableDatabaseFullBtn.clicked.connect(
            lambda: createTable_database_full()
        )

        self.ui.addEmptyCodeBtn.clicked.connect(
            lambda: createTable_database_basic()
        )

        self.ui.database_table.horizontalHeader().sectionResized.connect(
            self.ui.database_table.resizeColumnsToContents())

        self.ui.database_search.textChanged.connect(findName)

        self.ui.database_table.doubleClicked.connect(on_click)

        # CLOSE CADASTRO DE ITEM
        self.ui.closeCadastroItemBtn.clicked.connect(
            lambda: self.ui.addCodeContainer.collapseMenu())

        self.ui.saveCadastroItemBtn.clicked.connect(self.salvarCadastroSimples)

    def validaCadastroSimplesPreenchido(self):
        status = self.ui.addStatusEdit.text().strip().capitalize()
        codigo: str = self.ui.addCodigoEdit.text().strip()
        descricao_basico = self.ui.addBasicDescrEdit.text().strip()
        descricao_completa = self.ui.addFullDescrEdit.text().strip()
        quantidade = self.ui.addQuantidadeEdit.text().strip()
        caixa = self.ui.addCaixaEdit.text().strip()
        prateleira = self.ui.addPrateleiraEdit.text().strip()
        corredor = self.ui.addCorredorEdit.text().strip()

        # codigo_numerico = codigo.isnumeric()
        # codigo_tamanho = len(codigo) == 6

        if not (status == 'Ativo' or status == 'Inativo'):
            print(f'Problemas com Status: "{status}"')
            return None
        if not (codigo.isnumeric() and len(codigo) == 6):
            print(f'Problemas com codigo: "{codigo}"')
            return None
        if descricao_basico == '':
            print(f'Problemas com descricao_basico: "{descricao_basico}"')
            return None
        if descricao_completa == '':
            print(f'Problemas com descricao_completa: "{descricao_completa}"')
            return None
        if not quantidade.isnumeric():
            print(f'Problemas com quantidade: "{quantidade}"')
            return None
        if not caixa.isnumeric():
            print(f'Problemas com caixa: "{caixa}"')
            return None
        if not prateleira.isnumeric():
            print(f'Problemas com prateleira: "{prateleira}"')
            return None
        if not corredor.isnumeric():
            print(f'Problemas com corredor: "{corredor}"')
            return None
        return True

    def salvarCadastroSimples(self):
        if not self.validaCadastroSimplesPreenchido() == None:
            print('Todos os campos estao preenchidos corretamente.')
        else:
            ...
            # print('Possui erros em algum dos campos.')


# ########################################################################### #
# execute app
# ########################################################################### #
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.resize(500, 500)
    window.show()
    t = Thread(target=import_database_from_excel_backup, args=())
    t.start()

    sys.exit(app.exec_())


# ########################################################################### #
# END
# ########################################################################### #
