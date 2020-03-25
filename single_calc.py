from builtins import object

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets


class Ui_SingleCalcDialog(object):
    def setupUi(self, SingleCalcDialog):
        SingleCalcDialog.setObjectName("SingleCalcDialog")
        SingleCalcDialog.resize(720, 463)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SingleCalcDialog.sizePolicy().hasHeightForWidth())
        SingleCalcDialog.setSizePolicy(sizePolicy)
        SingleCalcDialog.setMinimumSize(QtCore.QSize(720, 463))
        SingleCalcDialog.setMaximumSize(QtCore.QSize(720, 463))
        self.RadioGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        self.RadioGroup.setGeometry(QtCore.QRect(10, 10, 141, 191))
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
        self.OrientRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.OrientRadio.setGeometry(QtCore.QRect(10, 30, 151, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrientRadio.sizePolicy().hasHeightForWidth())
        self.OrientRadio.setSizePolicy(sizePolicy)
        self.OrientRadio.setObjectName("OrientRadio")
        self.radioButtonGroup = QtWidgets.QButtonGroup(SingleCalcDialog)
        self.radioButtonGroup.setObjectName("radioButtonGroup")
        self.radioButtonGroup.addButton(self.OrientRadio)
        self.RadialRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.RadialRadio.setGeometry(QtCore.QRect(10, 60, 161, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadialRadio.sizePolicy().hasHeightForWidth())
        self.RadialRadio.setSizePolicy(sizePolicy)
        self.RadialRadio.setObjectName("RadialRadio")
        self.radioButtonGroup.addButton(self.RadialRadio)
        self.IntersectRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.IntersectRadio.setGeometry(QtCore.QRect(10, 90, 151, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.IntersectRadio.sizePolicy().hasHeightForWidth()
        )
        self.IntersectRadio.setSizePolicy(sizePolicy)
        self.IntersectRadio.setObjectName("IntersectRadio")
        self.radioButtonGroup.addButton(self.IntersectRadio)
        self.ResectionRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.ResectionRadio.setGeometry(QtCore.QRect(10, 120, 141, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ResectionRadio.sizePolicy().hasHeightForWidth()
        )
        self.ResectionRadio.setSizePolicy(sizePolicy)
        self.ResectionRadio.setObjectName("ResectionRadio")
        self.radioButtonGroup.addButton(self.ResectionRadio)
        self.FreeRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.FreeRadio.setGeometry(QtCore.QRect(10, 150, 141, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreeRadio.sizePolicy().hasHeightForWidth())
        self.FreeRadio.setSizePolicy(sizePolicy)
        self.FreeRadio.setObjectName("FreeRadio")
        self.radioButtonGroup.addButton(self.FreeRadio)
        self.PointsGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        self.PointsGroup.setGeometry(QtCore.QRect(330, 10, 381, 191))
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
        self.AddAllButton = QtWidgets.QPushButton(self.PointsGroup)
        self.AddAllButton.setGeometry(QtCore.QRect(150, 80, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAllButton.sizePolicy().hasHeightForWidth())
        self.AddAllButton.setSizePolicy(sizePolicy)
        self.AddAllButton.setObjectName("AddAllButton")
        self.RemoveButton = QtWidgets.QPushButton(self.PointsGroup)
        self.RemoveButton.setGeometry(QtCore.QRect(150, 120, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        self.RemoveButton.setObjectName("RemoveButton")
        self.RemoveAllButton = QtWidgets.QPushButton(self.PointsGroup)
        self.RemoveAllButton.setGeometry(QtCore.QRect(150, 150, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RemoveAllButton.sizePolicy().hasHeightForWidth()
        )
        self.RemoveAllButton.setSizePolicy(sizePolicy)
        self.RemoveAllButton.setObjectName("RemoveAllButton")
        self.TargetPointsLabel = QtWidgets.QLabel(self.PointsGroup)
        self.TargetPointsLabel.setGeometry(QtCore.QRect(10, 20, 121, 16))
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
        self.UsedPointsLabel = QtWidgets.QLabel(self.PointsGroup)
        self.UsedPointsLabel.setGeometry(QtCore.QRect(250, 20, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.UsedPointsLabel.sizePolicy().hasHeightForWidth()
        )
        self.UsedPointsLabel.setSizePolicy(sizePolicy)
        self.UsedPointsLabel.setObjectName("UsedPointsLabel")
        self.SourceList = QtWidgets.QListWidget(self.PointsGroup)
        self.SourceList.setGeometry(QtCore.QRect(10, 40, 121, 141))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SourceList.sizePolicy().hasHeightForWidth())
        self.SourceList.setSizePolicy(sizePolicy)
        self.SourceList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.SourceList.setObjectName("SourceList")
        self.TargetList = QtWidgets.QListWidget(self.PointsGroup)
        self.TargetList.setGeometry(QtCore.QRect(250, 40, 121, 141))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TargetList.sizePolicy().hasHeightForWidth())
        self.TargetList.setSizePolicy(sizePolicy)
        self.TargetList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TargetList.setObjectName("TargetList")
        self.ResultGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        self.ResultGroup.setGeometry(QtCore.QRect(10, 210, 701, 201))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setObjectName("ResultGroup")
        self.ResultTextBrowser = QtWidgets.QTextBrowser(self.ResultGroup)
        self.ResultTextBrowser.setGeometry(QtCore.QRect(10, 20, 681, 171))
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
        self.StationGroup = QtWidgets.QGroupBox(SingleCalcDialog)
        self.StationGroup.setGeometry(QtCore.QRect(170, 10, 141, 191))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StationGroup.sizePolicy().hasHeightForWidth())
        self.StationGroup.setSizePolicy(sizePolicy)
        self.StationGroup.setObjectName("StationGroup")
        self.Station1Combo = QtWidgets.QComboBox(self.StationGroup)
        self.Station1Combo.setGeometry(QtCore.QRect(10, 50, 121, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Station1Combo.sizePolicy().hasHeightForWidth()
        )
        self.Station1Combo.setSizePolicy(sizePolicy)
        self.Station1Combo.setObjectName("Station1Combo")
        self.Station1Label = QtWidgets.QLabel(self.StationGroup)
        self.Station1Label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Station1Label.sizePolicy().hasHeightForWidth()
        )
        self.Station1Label.setSizePolicy(sizePolicy)
        self.Station1Label.setObjectName("Station1Label")
        self.Station2Label = QtWidgets.QLabel(self.StationGroup)
        self.Station2Label.setGeometry(QtCore.QRect(10, 90, 111, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Station2Label.sizePolicy().hasHeightForWidth()
        )
        self.Station2Label.setSizePolicy(sizePolicy)
        self.Station2Label.setObjectName("Station2Label")
        self.Station2Combo = QtWidgets.QComboBox(self.StationGroup)
        self.Station2Combo.setGeometry(QtCore.QRect(10, 120, 121, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Station2Combo.sizePolicy().hasHeightForWidth()
        )
        self.Station2Combo.setSizePolicy(sizePolicy)
        self.Station2Combo.setObjectName("Station2Combo")
        self.CalcButton = QtWidgets.QPushButton(SingleCalcDialog)
        self.CalcButton.setGeometry(QtCore.QRect(420, 430, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setObjectName("CalcButton")
        self.HelpButton = QtWidgets.QPushButton(SingleCalcDialog)
        self.HelpButton.setGeometry(QtCore.QRect(20, 430, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setObjectName("HelpButton")
        self.ResetButton = QtWidgets.QPushButton(SingleCalcDialog)
        self.ResetButton.setGeometry(QtCore.QRect(520, 430, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName("ResetButton")
        self.CloseButton = QtWidgets.QPushButton(SingleCalcDialog)
        self.CloseButton.setGeometry(QtCore.QRect(620, 430, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName("CloseButton")

        self.retranslateUi(SingleCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(SingleCalcDialog)
        SingleCalcDialog.setTabOrder(self.OrientRadio, self.RadialRadio)
        SingleCalcDialog.setTabOrder(self.RadialRadio, self.IntersectRadio)
        SingleCalcDialog.setTabOrder(self.IntersectRadio, self.ResectionRadio)
        SingleCalcDialog.setTabOrder(self.ResectionRadio, self.FreeRadio)
        SingleCalcDialog.setTabOrder(self.FreeRadio, self.Station1Combo)
        SingleCalcDialog.setTabOrder(self.Station1Combo, self.Station2Combo)
        SingleCalcDialog.setTabOrder(self.Station2Combo, self.AddButton)
        SingleCalcDialog.setTabOrder(self.AddButton, self.AddAllButton)
        SingleCalcDialog.setTabOrder(self.AddAllButton, self.RemoveButton)
        SingleCalcDialog.setTabOrder(self.RemoveButton, self.RemoveAllButton)
        SingleCalcDialog.setTabOrder(self.RemoveAllButton, self.HelpButton)
        SingleCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        SingleCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        SingleCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, SingleCalcDialog):
        _translate = QtCore.QCoreApplication.translate
        SingleCalcDialog.setWindowTitle(
            _translate("SingleCalcDialog", "Single Point Calculations")
        )
        self.RadioGroup.setTitle(_translate("SingleCalcDialog", "Calculation"))
        self.OrientRadio.setToolTip(
            _translate("SingleCalcDialog", "Calculate orientation angle  on stations")
        )
        self.OrientRadio.setText(_translate("SingleCalcDialog", "Orientation"))
        self.RadialRadio.setText(_translate("SingleCalcDialog", "Radial Survey"))
        self.IntersectRadio.setText(_translate("SingleCalcDialog", "Intersection"))
        self.ResectionRadio.setText(_translate("SingleCalcDialog", "Resection"))
        self.FreeRadio.setText(_translate("SingleCalcDialog", "Free Station"))
        self.PointsGroup.setTitle(_translate("SingleCalcDialog", "Points"))
        self.AddButton.setText(_translate("SingleCalcDialog", "Add >"))
        self.AddAllButton.setText(_translate("SingleCalcDialog", "Add all"))
        self.RemoveButton.setText(_translate("SingleCalcDialog", "< Remove"))
        self.RemoveAllButton.setText(_translate("SingleCalcDialog", "Remove all"))
        self.TargetPointsLabel.setText(_translate("SingleCalcDialog", "Target Points"))
        self.UsedPointsLabel.setText(_translate("SingleCalcDialog", "Used Points"))
        self.ResultGroup.setTitle(
            _translate("SingleCalcDialog", "Result of Calculations")
        )
        self.StationGroup.setTitle(_translate("SingleCalcDialog", "Station"))
        self.Station1Label.setText(_translate("SingleCalcDialog", "Station (1)"))
        self.Station2Label.setText(_translate("SingleCalcDialog", "Station (2)"))
        self.CalcButton.setText(_translate("SingleCalcDialog", "Calculate"))
        self.HelpButton.setText(_translate("SingleCalcDialog", "Help"))
        self.ResetButton.setText(_translate("SingleCalcDialog", "Reset"))
        self.CloseButton.setText(_translate("SingleCalcDialog", "Close"))
