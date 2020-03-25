from builtins import object

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network_calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets


class Ui_NetworkCalcDialog(object):
    def setupUi(self, NetworkCalcDialog):
        NetworkCalcDialog.setObjectName("NetworkCalcDialog")
        NetworkCalcDialog.resize(638, 542)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NetworkCalcDialog.sizePolicy().hasHeightForWidth())
        NetworkCalcDialog.setSizePolicy(sizePolicy)
        NetworkCalcDialog.setMinimumSize(QtCore.QSize(638, 542))
        NetworkCalcDialog.setMaximumSize(QtCore.QSize(638, 542))
        NetworkCalcDialog.setAccessibleName("")
        NetworkCalcDialog.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom)
        )
        self.PointsGroup = QtWidgets.QGroupBox(NetworkCalcDialog)
        self.PointsGroup.setGeometry(QtCore.QRect(10, 10, 401, 311))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsGroup.sizePolicy().hasHeightForWidth())
        self.PointsGroup.setSizePolicy(sizePolicy)
        self.PointsGroup.setObjectName("PointsGroup")
        self.AddFixButton = QtWidgets.QPushButton(self.PointsGroup)
        self.AddFixButton.setGeometry(QtCore.QRect(160, 50, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddFixButton.sizePolicy().hasHeightForWidth())
        self.AddFixButton.setSizePolicy(sizePolicy)
        self.AddFixButton.setObjectName("AddFixButton")
        self.AddAdjButton = QtWidgets.QPushButton(self.PointsGroup)
        self.AddAdjButton.setGeometry(QtCore.QRect(160, 200, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAdjButton.sizePolicy().hasHeightForWidth())
        self.AddAdjButton.setSizePolicy(sizePolicy)
        self.AddAdjButton.setObjectName("AddAdjButton")
        self.RemoveFixButton = QtWidgets.QPushButton(self.PointsGroup)
        self.RemoveFixButton.setGeometry(QtCore.QRect(160, 90, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RemoveFixButton.sizePolicy().hasHeightForWidth()
        )
        self.RemoveFixButton.setSizePolicy(sizePolicy)
        self.RemoveFixButton.setObjectName("RemoveFixButton")
        self.PointsLabel = QtWidgets.QLabel(self.PointsGroup)
        self.PointsLabel.setGeometry(QtCore.QRect(10, 20, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsLabel.sizePolicy().hasHeightForWidth())
        self.PointsLabel.setSizePolicy(sizePolicy)
        self.PointsLabel.setObjectName("PointsLabel")
        self.FixLabel = QtWidgets.QLabel(self.PointsGroup)
        self.FixLabel.setGeometry(QtCore.QRect(260, 20, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FixLabel.sizePolicy().hasHeightForWidth())
        self.FixLabel.setSizePolicy(sizePolicy)
        self.FixLabel.setObjectName("FixLabel")
        self.RemoveAdjButton = QtWidgets.QPushButton(self.PointsGroup)
        self.RemoveAdjButton.setGeometry(QtCore.QRect(160, 240, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RemoveAdjButton.sizePolicy().hasHeightForWidth()
        )
        self.RemoveAdjButton.setSizePolicy(sizePolicy)
        self.RemoveAdjButton.setObjectName("RemoveAdjButton")
        self.AdjustedLabel = QtWidgets.QLabel(self.PointsGroup)
        self.AdjustedLabel.setGeometry(QtCore.QRect(260, 170, 141, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.AdjustedLabel.sizePolicy().hasHeightForWidth()
        )
        self.AdjustedLabel.setSizePolicy(sizePolicy)
        self.AdjustedLabel.setObjectName("AdjustedLabel")
        self.PointsList = QtWidgets.QListWidget(self.PointsGroup)
        self.PointsList.setGeometry(QtCore.QRect(10, 40, 131, 261))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsList.sizePolicy().hasHeightForWidth())
        self.PointsList.setSizePolicy(sizePolicy)
        self.PointsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.PointsList.setObjectName("PointsList")
        self.FixList = QtWidgets.QListWidget(self.PointsGroup)
        self.FixList.setGeometry(QtCore.QRect(260, 40, 131, 111))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FixList.sizePolicy().hasHeightForWidth())
        self.FixList.setSizePolicy(sizePolicy)
        self.FixList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.FixList.setObjectName("FixList")
        self.AdjustedList = QtWidgets.QListWidget(self.PointsGroup)
        self.AdjustedList.setGeometry(QtCore.QRect(260, 190, 131, 111))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdjustedList.sizePolicy().hasHeightForWidth())
        self.AdjustedList.setSizePolicy(sizePolicy)
        self.AdjustedList.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.AdjustedList.setObjectName("AdjustedList")
        self.ResetButton = QtWidgets.QPushButton(NetworkCalcDialog)
        self.ResetButton.setGeometry(QtCore.QRect(440, 510, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName("ResetButton")
        self.CloseButton = QtWidgets.QPushButton(NetworkCalcDialog)
        self.CloseButton.setGeometry(QtCore.QRect(540, 510, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName("CloseButton")
        self.ResultGroup = QtWidgets.QGroupBox(NetworkCalcDialog)
        self.ResultGroup.setGeometry(QtCore.QRect(10, 330, 621, 161))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setObjectName("ResultGroup")
        self.ResultTextBrowser = QtWidgets.QTextBrowser(self.ResultGroup)
        self.ResultTextBrowser.setGeometry(QtCore.QRect(10, 20, 601, 131))
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
        font.setPointSize(8)
        self.ResultTextBrowser.setFont(font)
        self.ResultTextBrowser.setObjectName("ResultTextBrowser")
        self.HelpButton = QtWidgets.QPushButton(NetworkCalcDialog)
        self.HelpButton.setGeometry(QtCore.QRect(20, 510, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setObjectName("HelpButton")
        self.CalcButton = QtWidgets.QPushButton(NetworkCalcDialog)
        self.CalcButton.setGeometry(QtCore.QRect(340, 510, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setObjectName("CalcButton")
        self.ParametersGroup = QtWidgets.QGroupBox(NetworkCalcDialog)
        self.ParametersGroup.setGeometry(QtCore.QRect(420, 10, 201, 311))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ParametersGroup.sizePolicy().hasHeightForWidth()
        )
        self.ParametersGroup.setSizePolicy(sizePolicy)
        self.ParametersGroup.setObjectName("ParametersGroup")
        self.ConfidenceComboBox = QtWidgets.QComboBox(self.ParametersGroup)
        self.ConfidenceComboBox.setGeometry(QtCore.QRect(30, 270, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ConfidenceComboBox.sizePolicy().hasHeightForWidth()
        )
        self.ConfidenceComboBox.setSizePolicy(sizePolicy)
        self.ConfidenceComboBox.setObjectName("ConfidenceComboBox")
        self.ConfidenceComboBox.addItem("")
        self.ConfidenceComboBox.addItem("")
        self.ConfidenceLabel = QtWidgets.QLabel(self.ParametersGroup)
        self.ConfidenceLabel.setGeometry(QtCore.QRect(10, 250, 151, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ConfidenceLabel.sizePolicy().hasHeightForWidth()
        )
        self.ConfidenceLabel.setSizePolicy(sizePolicy)
        self.ConfidenceLabel.setObjectName("ConfidenceLabel")
        self.DistDevLabel = QtWidgets.QLabel(self.ParametersGroup)
        self.DistDevLabel.setGeometry(QtCore.QRect(10, 160, 191, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DistDevLabel.sizePolicy().hasHeightForWidth())
        self.DistDevLabel.setSizePolicy(sizePolicy)
        self.DistDevLabel.setObjectName("DistDevLabel")
        self.DistDevMMLabel = QtWidgets.QLabel(self.ParametersGroup)
        self.DistDevMMLabel.setGeometry(QtCore.QRect(50, 190, 51, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DistDevMMLabel.sizePolicy().hasHeightForWidth()
        )
        self.DistDevMMLabel.setSizePolicy(sizePolicy)
        self.DistDevMMLabel.setObjectName("DistDevMMLabel")
        self.DistDevMMKMLabel = QtWidgets.QLabel(self.ParametersGroup)
        self.DistDevMMKMLabel.setGeometry(QtCore.QRect(140, 190, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DistDevMMKMLabel.sizePolicy().hasHeightForWidth()
        )
        self.DistDevMMKMLabel.setSizePolicy(sizePolicy)
        self.DistDevMMKMLabel.setObjectName("DistDevMMKMLabel")
        self.ZenitDevLabel = QtWidgets.QLabel(self.ParametersGroup)
        self.ZenitDevLabel.setGeometry(QtCore.QRect(10, 100, 181, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ZenitDevLabel.sizePolicy().hasHeightForWidth()
        )
        self.ZenitDevLabel.setSizePolicy(sizePolicy)
        self.ZenitDevLabel.setObjectName("ZenitDevLabel")
        self.DistDevMMLabel_2 = QtWidgets.QLabel(self.ParametersGroup)
        self.DistDevMMLabel_2.setGeometry(QtCore.QRect(60, 130, 61, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DistDevMMLabel_2.sizePolicy().hasHeightForWidth()
        )
        self.DistDevMMLabel_2.setSizePolicy(sizePolicy)
        self.DistDevMMLabel_2.setObjectName("DistDevMMLabel_2")
        self.DimensionComboBox = QtWidgets.QComboBox(self.ParametersGroup)
        self.DimensionComboBox.setGeometry(QtCore.QRect(10, 60, 51, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DimensionComboBox.sizePolicy().hasHeightForWidth()
        )
        self.DimensionComboBox.setSizePolicy(sizePolicy)
        self.DimensionComboBox.setObjectName("DimensionComboBox")
        self.DimensionComboBox.addItem("")
        self.DimensionComboBox.addItem("")
        self.DimensionComboBox.addItem("")
        self.ZenitDevLabel_2 = QtWidgets.QLabel(self.ParametersGroup)
        self.ZenitDevLabel_2.setGeometry(QtCore.QRect(10, 40, 181, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ZenitDevLabel_2.sizePolicy().hasHeightForWidth()
        )
        self.ZenitDevLabel_2.setSizePolicy(sizePolicy)
        self.ZenitDevLabel_2.setObjectName("ZenitDevLabel_2")
        self.AngleDevLineEdit = QtWidgets.QLineEdit(self.ParametersGroup)
        self.AngleDevLineEdit.setGeometry(QtCore.QRect(10, 120, 41, 31))
        self.AngleDevLineEdit.setObjectName("AngleDevLineEdit")
        self.DistDevMMLineEdit = QtWidgets.QLineEdit(self.ParametersGroup)
        self.DistDevMMLineEdit.setGeometry(QtCore.QRect(10, 180, 41, 31))
        self.DistDevMMLineEdit.setObjectName("DistDevMMLineEdit")
        self.DistDevMMKMLineEdit = QtWidgets.QLineEdit(self.ParametersGroup)
        self.DistDevMMKMLineEdit.setGeometry(QtCore.QRect(100, 180, 41, 31))
        self.DistDevMMKMLineEdit.setObjectName("DistDevMMKMLineEdit")

        self.retranslateUi(NetworkCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(NetworkCalcDialog)
        NetworkCalcDialog.setTabOrder(self.PointsList, self.AddFixButton)
        NetworkCalcDialog.setTabOrder(self.AddFixButton, self.RemoveFixButton)
        NetworkCalcDialog.setTabOrder(self.RemoveFixButton, self.AddAdjButton)
        NetworkCalcDialog.setTabOrder(self.AddAdjButton, self.RemoveAdjButton)
        NetworkCalcDialog.setTabOrder(self.RemoveAdjButton, self.FixList)
        NetworkCalcDialog.setTabOrder(self.FixList, self.AdjustedList)
        NetworkCalcDialog.setTabOrder(self.AdjustedList, self.DimensionComboBox)
        NetworkCalcDialog.setTabOrder(self.DimensionComboBox, self.ConfidenceComboBox)
        NetworkCalcDialog.setTabOrder(self.ConfidenceComboBox, self.ResultTextBrowser)
        NetworkCalcDialog.setTabOrder(self.ResultTextBrowser, self.HelpButton)
        NetworkCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        NetworkCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        NetworkCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, NetworkCalcDialog):
        _translate = QtCore.QCoreApplication.translate
        NetworkCalcDialog.setWindowTitle(
            _translate("NetworkCalcDialog", "Network Adjustment")
        )
        self.PointsGroup.setTitle(_translate("NetworkCalcDialog", "Points"))
        self.AddFixButton.setText(_translate("NetworkCalcDialog", "Add >"))
        self.AddAdjButton.setText(_translate("NetworkCalcDialog", "Add >"))
        self.RemoveFixButton.setText(_translate("NetworkCalcDialog", "< Remove"))
        self.PointsLabel.setText(_translate("NetworkCalcDialog", "List of Points"))
        self.FixLabel.setText(_translate("NetworkCalcDialog", "Fix Points"))
        self.RemoveAdjButton.setText(_translate("NetworkCalcDialog", "< Remove"))
        self.AdjustedLabel.setText(_translate("NetworkCalcDialog", "Adjusted Points"))
        self.ResetButton.setText(_translate("NetworkCalcDialog", "Reset"))
        self.CloseButton.setText(_translate("NetworkCalcDialog", "Close"))
        self.ResultGroup.setTitle(
            _translate("NetworkCalcDialog", "Result of Calculations")
        )
        self.HelpButton.setText(_translate("NetworkCalcDialog", "Help"))
        self.CalcButton.setText(_translate("NetworkCalcDialog", "Calculate"))
        self.ParametersGroup.setTitle(_translate("NetworkCalcDialog", "Parameters"))
        self.ConfidenceComboBox.setItemText(0, _translate("NetworkCalcDialog", "0.95"))
        self.ConfidenceComboBox.setItemText(1, _translate("NetworkCalcDialog", "0.997"))
        self.ConfidenceLabel.setText(
            _translate("NetworkCalcDialog", "Confidence Level")
        )
        self.DistDevLabel.setText(
            _translate("NetworkCalcDialog", "Distance standard deviation")
        )
        self.DistDevMMLabel.setText(_translate("NetworkCalcDialog", "[mm] +"))
        self.DistDevMMKMLabel.setText(_translate("NetworkCalcDialog", "[mm/km]"))
        self.ZenitDevLabel.setText(
            _translate("NetworkCalcDialog", "Angle standard deviation")
        )
        self.DistDevMMLabel_2.setText(_translate("NetworkCalcDialog", "[cc]"))
        self.DimensionComboBox.setItemText(0, _translate("NetworkCalcDialog", "2"))
        self.DimensionComboBox.setItemText(1, _translate("NetworkCalcDialog", "1"))
        self.DimensionComboBox.setItemText(2, _translate("NetworkCalcDialog", "3"))
        self.ZenitDevLabel_2.setText(_translate("NetworkCalcDialog", "Dimension"))
        self.AngleDevLineEdit.setText(_translate("NetworkCalcDialog", "3"))
        self.DistDevMMLineEdit.setText(_translate("NetworkCalcDialog", "3"))
        self.DistDevMMKMLineEdit.setText(_translate("NetworkCalcDialog", "3"))
