from builtins import object

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'traverse_calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets


class Ui_TraverseCalcDialog(object):
    def setupUi(self, TraverseCalcDialog):
        TraverseCalcDialog.setObjectName("TraverseCalcDialog")
        TraverseCalcDialog.resize(754, 456)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            TraverseCalcDialog.sizePolicy().hasHeightForWidth()
        )
        TraverseCalcDialog.setSizePolicy(sizePolicy)
        TraverseCalcDialog.setMinimumSize(QtCore.QSize(754, 456))
        TraverseCalcDialog.setMaximumSize(QtCore.QSize(754, 456))
        TraverseCalcDialog.setAccessibleName("")
        TraverseCalcDialog.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom)
        )
        self.EndpointsGroup = QtWidgets.QGroupBox(TraverseCalcDialog)
        self.EndpointsGroup.setGeometry(QtCore.QRect(180, 10, 151, 221))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.EndpointsGroup.sizePolicy().hasHeightForWidth()
        )
        self.EndpointsGroup.setSizePolicy(sizePolicy)
        self.EndpointsGroup.setObjectName("EndpointsGroup")
        self.StartPointComboBox = QtWidgets.QComboBox(self.EndpointsGroup)
        self.StartPointComboBox.setGeometry(QtCore.QRect(10, 40, 131, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.StartPointComboBox.sizePolicy().hasHeightForWidth()
        )
        self.StartPointComboBox.setSizePolicy(sizePolicy)
        self.StartPointComboBox.setObjectName("StartPointComboBox")
        self.StartPointLabel = QtWidgets.QLabel(self.EndpointsGroup)
        self.StartPointLabel.setGeometry(QtCore.QRect(10, 20, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.StartPointLabel.sizePolicy().hasHeightForWidth()
        )
        self.StartPointLabel.setSizePolicy(sizePolicy)
        self.StartPointLabel.setObjectName("StartPointLabel")
        self.EndPointLabel = QtWidgets.QLabel(self.EndpointsGroup)
        self.EndPointLabel.setGeometry(QtCore.QRect(10, 90, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.EndPointLabel.sizePolicy().hasHeightForWidth()
        )
        self.EndPointLabel.setSizePolicy(sizePolicy)
        self.EndPointLabel.setObjectName("EndPointLabel")
        self.EndPointComboBox = QtWidgets.QComboBox(self.EndpointsGroup)
        self.EndPointComboBox.setGeometry(QtCore.QRect(10, 110, 131, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.EndPointComboBox.sizePolicy().hasHeightForWidth()
        )
        self.EndPointComboBox.setSizePolicy(sizePolicy)
        self.EndPointComboBox.setObjectName("EndPointComboBox")
        self.PointsGroup = QtWidgets.QGroupBox(TraverseCalcDialog)
        self.PointsGroup.setGeometry(QtCore.QRect(350, 10, 391, 221))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsGroup.sizePolicy().hasHeightForWidth())
        self.PointsGroup.setSizePolicy(sizePolicy)
        self.PointsGroup.setObjectName("PointsGroup")
        self.AddButton = QtWidgets.QPushButton(self.PointsGroup)
        self.AddButton.setGeometry(QtCore.QRect(150, 50, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setObjectName("AddButton")
        self.RemoveButton = QtWidgets.QPushButton(self.PointsGroup)
        self.RemoveButton.setGeometry(QtCore.QRect(150, 180, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        self.RemoveButton.setObjectName("RemoveButton")
        self.TargetPointsLabel = QtWidgets.QLabel(self.PointsGroup)
        self.TargetPointsLabel.setGeometry(QtCore.QRect(10, 20, 161, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TargetPointsLabel.sizePolicy().hasHeightForWidth()
        )
        self.TargetPointsLabel.setSizePolicy(sizePolicy)
        self.TargetPointsLabel.setObjectName("TargetPointsLabel")
        self.OrderPointsLabel = QtWidgets.QLabel(self.PointsGroup)
        self.OrderPointsLabel.setGeometry(QtCore.QRect(250, 20, 151, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.OrderPointsLabel.sizePolicy().hasHeightForWidth()
        )
        self.OrderPointsLabel.setSizePolicy(sizePolicy)
        self.OrderPointsLabel.setObjectName("OrderPointsLabel")
        self.UpButton = QtWidgets.QPushButton(self.PointsGroup)
        self.UpButton.setGeometry(QtCore.QRect(180, 100, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UpButton.sizePolicy().hasHeightForWidth())
        self.UpButton.setSizePolicy(sizePolicy)
        self.UpButton.setObjectName("UpButton")
        self.DownButton = QtWidgets.QPushButton(self.PointsGroup)
        self.DownButton.setGeometry(QtCore.QRect(180, 130, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownButton.sizePolicy().hasHeightForWidth())
        self.DownButton.setSizePolicy(sizePolicy)
        self.DownButton.setObjectName("DownButton")
        self.TargetList = QtWidgets.QListWidget(self.PointsGroup)
        self.TargetList.setGeometry(QtCore.QRect(10, 40, 131, 171))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TargetList.sizePolicy().hasHeightForWidth())
        self.TargetList.setSizePolicy(sizePolicy)
        self.TargetList.setObjectName("TargetList")
        self.OrderList = QtWidgets.QListWidget(self.PointsGroup)
        self.OrderList.setGeometry(QtCore.QRect(250, 40, 131, 171))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrderList.sizePolicy().hasHeightForWidth())
        self.OrderList.setSizePolicy(sizePolicy)
        self.OrderList.setObjectName("OrderList")
        self.RadioGroup = QtWidgets.QGroupBox(TraverseCalcDialog)
        self.RadioGroup.setGeometry(QtCore.QRect(10, 10, 151, 221))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadioGroup.sizePolicy().hasHeightForWidth())
        self.RadioGroup.setSizePolicy(sizePolicy)
        self.RadioGroup.setFlat(False)
        self.RadioGroup.setCheckable(False)
        self.RadioGroup.setObjectName("RadioGroup")
        self.ClosedRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.ClosedRadio.setGeometry(QtCore.QRect(10, 30, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClosedRadio.sizePolicy().hasHeightForWidth())
        self.ClosedRadio.setSizePolicy(sizePolicy)
        self.ClosedRadio.setObjectName("ClosedRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(TraverseCalcDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.ClosedRadio)
        self.LinkRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.LinkRadio.setGeometry(QtCore.QRect(10, 60, 161, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinkRadio.sizePolicy().hasHeightForWidth())
        self.LinkRadio.setSizePolicy(sizePolicy)
        self.LinkRadio.setObjectName("LinkRadio")
        self.buttonGroup.addButton(self.LinkRadio)
        self.OpenRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.OpenRadio.setGeometry(QtCore.QRect(10, 90, 171, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenRadio.sizePolicy().hasHeightForWidth())
        self.OpenRadio.setSizePolicy(sizePolicy)
        self.OpenRadio.setObjectName("OpenRadio")
        self.buttonGroup.addButton(self.OpenRadio)
        self.CloseButton = QtWidgets.QPushButton(TraverseCalcDialog)
        self.CloseButton.setGeometry(QtCore.QRect(650, 420, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName("CloseButton")
        self.ResultGroup = QtWidgets.QGroupBox(TraverseCalcDialog)
        self.ResultGroup.setGeometry(QtCore.QRect(10, 240, 731, 161))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setObjectName("ResultGroup")
        self.ResultTextBrowser = QtWidgets.QTextBrowser(self.ResultGroup)
        self.ResultTextBrowser.setGeometry(QtCore.QRect(10, 20, 711, 131))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ResultTextBrowser.sizePolicy().hasHeightForWidth()
        )
        self.ResultTextBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.ResultTextBrowser.setFont(font)
        self.ResultTextBrowser.setObjectName("ResultTextBrowser")
        self.HelpButton = QtWidgets.QPushButton(TraverseCalcDialog)
        self.HelpButton.setGeometry(QtCore.QRect(20, 420, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setObjectName("HelpButton")
        self.CalcButton = QtWidgets.QPushButton(TraverseCalcDialog)
        self.CalcButton.setGeometry(QtCore.QRect(450, 420, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setObjectName("CalcButton")
        self.ResetButton = QtWidgets.QPushButton(TraverseCalcDialog)
        self.ResetButton.setGeometry(QtCore.QRect(550, 420, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName("ResetButton")

        self.retranslateUi(TraverseCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(TraverseCalcDialog)
        TraverseCalcDialog.setTabOrder(self.ClosedRadio, self.LinkRadio)
        TraverseCalcDialog.setTabOrder(self.LinkRadio, self.OpenRadio)
        TraverseCalcDialog.setTabOrder(self.OpenRadio, self.StartPointComboBox)
        TraverseCalcDialog.setTabOrder(self.StartPointComboBox, self.EndPointComboBox)
        TraverseCalcDialog.setTabOrder(self.EndPointComboBox, self.AddButton)
        TraverseCalcDialog.setTabOrder(self.AddButton, self.UpButton)
        TraverseCalcDialog.setTabOrder(self.UpButton, self.DownButton)
        TraverseCalcDialog.setTabOrder(self.DownButton, self.RemoveButton)
        TraverseCalcDialog.setTabOrder(self.RemoveButton, self.ResultTextBrowser)
        TraverseCalcDialog.setTabOrder(self.ResultTextBrowser, self.HelpButton)
        TraverseCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        TraverseCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        TraverseCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, TraverseCalcDialog):
        _translate = QtCore.QCoreApplication.translate
        TraverseCalcDialog.setWindowTitle(
            _translate("TraverseCalcDialog", "Traverse Calculations")
        )
        self.EndpointsGroup.setTitle(_translate("TraverseCalcDialog", "Endpoints"))
        self.StartPointLabel.setText(_translate("TraverseCalcDialog", "Start Point"))
        self.EndPointLabel.setText(_translate("TraverseCalcDialog", "End Point"))
        self.PointsGroup.setTitle(_translate("TraverseCalcDialog", "Points"))
        self.AddButton.setText(_translate("TraverseCalcDialog", "Add >"))
        self.RemoveButton.setText(_translate("TraverseCalcDialog", "< Remove"))
        self.TargetPointsLabel.setText(
            _translate("TraverseCalcDialog", "Target Points")
        )
        self.OrderPointsLabel.setText(
            _translate("TraverseCalcDialog", "Order of Points")
        )
        self.UpButton.setText(_translate("TraverseCalcDialog", "Up"))
        self.DownButton.setText(_translate("TraverseCalcDialog", "Down"))
        self.RadioGroup.setTitle(_translate("TraverseCalcDialog", "Type"))
        self.ClosedRadio.setToolTip(
            _translate(
                "TraverseCalcDialog",
                "Closed (polygonal or loop) traverse starts and finishes on the same known point.",
            )
        )
        self.ClosedRadio.setText(_translate("TraverseCalcDialog", "Closed Traverse"))
        self.LinkRadio.setToolTip(
            _translate(
                "TraverseCalcDialog", "A closed link traverse joins two known points."
            )
        )
        self.LinkRadio.setText(_translate("TraverseCalcDialog", "Link Traverse"))
        self.OpenRadio.setToolTip(
            _translate(
                "TraverseCalcDialog",
                "An open (free) traverse starts on a known point and finishes on an unknown point.",
            )
        )
        self.OpenRadio.setText(_translate("TraverseCalcDialog", "Open Traverse"))
        self.CloseButton.setText(_translate("TraverseCalcDialog", "Close"))
        self.ResultGroup.setTitle(
            _translate("TraverseCalcDialog", "Result of Traverse Calculations")
        )
        self.HelpButton.setText(_translate("TraverseCalcDialog", "Help"))
        self.CalcButton.setText(_translate("TraverseCalcDialog", "Calculate"))
        self.ResetButton.setText(_translate("TraverseCalcDialog", "Reset"))
