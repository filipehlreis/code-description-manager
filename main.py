# ########################################################################### #
# 22 MODERN UI
# QT GUI BY SPINN TV(YOUTUBE)
# ########################################################################### #

# ########################################################################### #
# IMPORTS
# ########################################################################### #
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

        self.ui.database_table.horizontalHeader().sectionResized.connect(
            self.ui.database_table.resizeColumnsToContents())

    # def create_table_widget(self, rowPosition, columnPosition, text, tableName):
    #     qtablewidgetitem = QTableWidgetItem()

    #     # USER getattr() METHOD
    #     getattr(self.ui, tableName).setItem(
    #         rowPosition, columnPosition, qtablewidgetitem)
    #     qtablewidgetitem = getattr(self.ui, tableName).item(
    #         rowPosition, columnPosition)

    #     qtablewidgetitem.setText(text)

    # def createTable_database_basic(self):
    #     for x in range(10):
    #         rowPosition = self.ui.database_table.rowCount()
    #         self.ui.database_table.insertRow(rowPosition)

    #         self.create_table_widget(
    #             rowPosition, 0, f'Teste {x}', 'database_table')
    #         self.create_table_widget(
    #             rowPosition, 1, f'Teste {x}', 'database_table')
    #         self.create_table_widget(
    #             rowPosition, 2, f'Teste {x}', 'database_table')
    #         self.create_table_widget(
    #             rowPosition, 3, f'Teste {x}', 'database_table')


# ########################################################################### #
# execute app
# ########################################################################### #
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    t = Thread(target=import_database_from_excel_backup, args=())
    t.start()
    sys.exit(app.exec_())


# ########################################################################### #
# END
# ########################################################################### #
