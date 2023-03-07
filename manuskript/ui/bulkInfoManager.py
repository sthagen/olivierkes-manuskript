# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\OpensourceWork\manuskript\manuskript\ui\bulkInfoManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BulkInfoManager(object):
    def setupUi(self, BulkInfoManager):
        BulkInfoManager.setObjectName("BulkInfoManager")
        BulkInfoManager.setWindowModality(QtCore.Qt.WindowModal)
        BulkInfoManager.resize(548, 556)
        self.verticalLayout = QtWidgets.QVBoxLayout(BulkInfoManager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblStaticMessage = QtWidgets.QLabel(BulkInfoManager)
        self.lblStaticMessage.setObjectName("lblStaticMessage")
        self.verticalLayout.addWidget(self.lblStaticMessage)
        self.lblCharactersDynamic = QtWidgets.QLabel(BulkInfoManager)
        self.lblCharactersDynamic.setObjectName("lblCharactersDynamic")
        self.verticalLayout.addWidget(self.lblCharactersDynamic)
        self.tableView = QtWidgets.QTableView(BulkInfoManager)
        self.tableView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPersoBulkAddInfo = QtWidgets.QPushButton(BulkInfoManager)
        self.btnPersoBulkAddInfo.setObjectName("btnPersoBulkAddInfo")
        self.horizontalLayout.addWidget(self.btnPersoBulkAddInfo)
        self.btnPersoBulkRmInfo = QtWidgets.QPushButton(BulkInfoManager)
        self.btnPersoBulkRmInfo.setObjectName("btnPersoBulkRmInfo")
        self.horizontalLayout.addWidget(self.btnPersoBulkRmInfo)
        self.btnPersoBulkApply = QtWidgets.QPushButton(BulkInfoManager)
        self.btnPersoBulkApply.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.btnPersoBulkApply.setObjectName("btnPersoBulkApply")
        self.horizontalLayout.addWidget(self.btnPersoBulkApply)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(BulkInfoManager)
        QtCore.QMetaObject.connectSlotsByName(BulkInfoManager)

    def retranslateUi(self, BulkInfoManager):
        _translate = QtCore.QCoreApplication.translate
        BulkInfoManager.setWindowTitle(_translate("BulkInfoManager", "Form"))
        self.lblStaticMessage.setText(_translate("BulkInfoManager", "Affected Characters:"))
        self.lblCharactersDynamic.setText(_translate("BulkInfoManager", "NONE"))
        self.btnPersoBulkAddInfo.setText(_translate("BulkInfoManager", "Add Entry"))
        self.btnPersoBulkRmInfo.setText(_translate("BulkInfoManager", "Remove Entry"))
        self.btnPersoBulkApply.setText(_translate("BulkInfoManager", "Apply Changes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BulkInfoManager = QtWidgets.QWidget()
    ui = Ui_BulkInfoManager()
    ui.setupUi(BulkInfoManager)
    BulkInfoManager.show()
    sys.exit(app.exec_())
