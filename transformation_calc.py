from builtins import object

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transformation_calc.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtGui, QtWidgets


class Ui_TransformationCalcDialog(object):
    def setupUi(self, TransformationCalcDialog):
        TransformationCalcDialog.setObjectName("TransformationCalcDialog")
        TransformationCalcDialog.resize(711, 471)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            TransformationCalcDialog.sizePolicy().hasHeightForWidth()
        )
        TransformationCalcDialog.setSizePolicy(sizePolicy)
        TransformationCalcDialog.setMinimumSize(QtCore.QSize(711, 471))
        TransformationCalcDialog.setMaximumSize(QtCore.QSize(711, 471))
        self.LayersGroup = QtWidgets.QGroupBox(TransformationCalcDialog)
        self.LayersGroup.setGeometry(QtCore.QRect(10, 10, 181, 251))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LayersGroup.sizePolicy().hasHeightForWidth())
        self.LayersGroup.setSizePolicy(sizePolicy)
        self.LayersGroup.setObjectName("LayersGroup")
        self.FromLayerComboBox = QtWidgets.QComboBox(self.LayersGroup)
        self.FromLayerComboBox.setGeometry(QtCore.QRect(10, 60, 161, 22))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FromLayerComboBox.sizePolicy().hasHeightForWidth()
        )
        self.FromLayerComboBox.setSizePolicy(sizePolicy)
        self.FromLayerComboBox.setObjectName("FromLayerComboBox")
        self.FromLayerButton = QtWidgets.QToolButton(self.LayersGroup)
        self.FromLayerButton.setEnabled(False)
        self.FromLayerButton.setGeometry(QtCore.QRect(120, 100, 51, 20))
        self.FromLayerButton.setObjectName("FromLayerButton")
        self.ToFileButton = QtWidgets.QToolButton(self.LayersGroup)
        self.ToFileButton.setGeometry(QtCore.QRect(120, 210, 51, 19))
        self.ToFileButton.setObjectName("ToFileButton")
        self.FromLayerLabel = QtWidgets.QLabel(self.LayersGroup)
        self.FromLayerLabel.setGeometry(QtCore.QRect(10, 30, 151, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FromLayerLabel.sizePolicy().hasHeightForWidth()
        )
        self.FromLayerLabel.setSizePolicy(sizePolicy)
        self.FromLayerLabel.setObjectName("FromLayerLabel")
        self.ToLayerLabel = QtWidgets.QLabel(self.LayersGroup)
        self.ToLayerLabel.setGeometry(QtCore.QRect(10, 140, 151, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToLayerLabel.sizePolicy().hasHeightForWidth())
        self.ToLayerLabel.setSizePolicy(sizePolicy)
        self.ToLayerLabel.setObjectName("ToLayerLabel")
        self.ToShapeEdit = QtWidgets.QLineEdit(self.LayersGroup)
        self.ToShapeEdit.setEnabled(False)
        self.ToShapeEdit.setGeometry(QtCore.QRect(10, 160, 161, 31))
        self.ToShapeEdit.setObjectName("ToShapeEdit")
        self.PointsGroup = QtWidgets.QGroupBox(TransformationCalcDialog)
        self.PointsGroup.setGeometry(QtCore.QRect(210, 10, 361, 251))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsGroup.sizePolicy().hasHeightForWidth())
        self.PointsGroup.setSizePolicy(sizePolicy)
        self.PointsGroup.setObjectName("PointsGroup")
        self.RemoveButton = QtWidgets.QPushButton(self.PointsGroup)
        self.RemoveButton.setGeometry(QtCore.QRect(140, 190, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        self.RemoveButton.setObjectName("RemoveButton")
        self.CommonPoints_Label = QtWidgets.QLabel(self.PointsGroup)
        self.CommonPoints_Label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CommonPoints_Label.sizePolicy().hasHeightForWidth()
        )
        self.CommonPoints_Label.setSizePolicy(sizePolicy)
        self.CommonPoints_Label.setObjectName("CommonPoints_Label")
        self.PointsofTrans_Label = QtWidgets.QLabel(self.PointsGroup)
        self.PointsofTrans_Label.setGeometry(QtCore.QRect(230, 20, 141, 16))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.PointsofTrans_Label.sizePolicy().hasHeightForWidth()
        )
        self.PointsofTrans_Label.setSizePolicy(sizePolicy)
        self.PointsofTrans_Label.setObjectName("PointsofTrans_Label")
        self.AddButton = QtWidgets.QPushButton(self.PointsGroup)
        self.AddButton.setGeometry(QtCore.QRect(140, 60, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setObjectName("AddButton")
        self.CommonList = QtWidgets.QListWidget(self.PointsGroup)
        self.CommonList.setGeometry(QtCore.QRect(10, 40, 121, 201))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CommonList.sizePolicy().hasHeightForWidth())
        self.CommonList.setSizePolicy(sizePolicy)
        self.CommonList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.CommonList.setObjectName("CommonList")
        self.UsedList = QtWidgets.QListWidget(self.PointsGroup)
        self.UsedList.setGeometry(QtCore.QRect(230, 40, 121, 201))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UsedList.sizePolicy().hasHeightForWidth())
        self.UsedList.setSizePolicy(sizePolicy)
        self.UsedList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.UsedList.setObjectName("UsedList")
        self.RadioGroup = QtWidgets.QGroupBox(TransformationCalcDialog)
        self.RadioGroup.setGeometry(QtCore.QRect(590, 10, 111, 251))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadioGroup.sizePolicy().hasHeightForWidth())
        self.RadioGroup.setSizePolicy(sizePolicy)
        self.RadioGroup.setObjectName("RadioGroup")
        self.OrthogonalRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.OrthogonalRadio.setGeometry(QtCore.QRect(10, 30, 191, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.OrthogonalRadio.sizePolicy().hasHeightForWidth()
        )
        self.OrthogonalRadio.setSizePolicy(sizePolicy)
        self.OrthogonalRadio.setObjectName("OrthogonalRadio")
        self.AffineRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.AffineRadio.setGeometry(QtCore.QRect(10, 60, 191, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AffineRadio.sizePolicy().hasHeightForWidth())
        self.AffineRadio.setSizePolicy(sizePolicy)
        self.AffineRadio.setObjectName("AffineRadio")
        self.ThirdRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.ThirdRadio.setGeometry(QtCore.QRect(10, 90, 171, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThirdRadio.sizePolicy().hasHeightForWidth())
        self.ThirdRadio.setSizePolicy(sizePolicy)
        self.ThirdRadio.setObjectName("ThirdRadio")
        self.FourthRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.FourthRadio.setGeometry(QtCore.QRect(10, 120, 151, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FourthRadio.sizePolicy().hasHeightForWidth())
        self.FourthRadio.setSizePolicy(sizePolicy)
        self.FourthRadio.setObjectName("FourthRadio")
        self.FifthRadio = QtWidgets.QRadioButton(self.RadioGroup)
        self.FifthRadio.setGeometry(QtCore.QRect(10, 150, 181, 17))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FifthRadio.sizePolicy().hasHeightForWidth())
        self.FifthRadio.setSizePolicy(sizePolicy)
        self.FifthRadio.setObjectName("FifthRadio")
        self.CalcButton = QtWidgets.QPushButton(TransformationCalcDialog)
        self.CalcButton.setGeometry(QtCore.QRect(410, 440, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setObjectName("CalcButton")
        self.ResultGroup = QtWidgets.QGroupBox(TransformationCalcDialog)
        self.ResultGroup.setGeometry(QtCore.QRect(10, 270, 691, 151))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setObjectName("ResultGroup")
        self.ResultTextBrowser = QtWidgets.QTextBrowser(self.ResultGroup)
        self.ResultTextBrowser.setGeometry(QtCore.QRect(10, 20, 671, 121))
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
        self.HelpButton = QtWidgets.QPushButton(TransformationCalcDialog)
        self.HelpButton.setGeometry(QtCore.QRect(20, 440, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setObjectName("HelpButton")
        self.CloseButton = QtWidgets.QPushButton(TransformationCalcDialog)
        self.CloseButton.setGeometry(QtCore.QRect(610, 440, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName("CloseButton")
        self.ResetButton = QtWidgets.QPushButton(TransformationCalcDialog)
        self.ResetButton.setGeometry(QtCore.QRect(510, 440, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setObjectName("ResetButton")

        self.retranslateUi(TransformationCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(TransformationCalcDialog)
        TransformationCalcDialog.setTabOrder(
            self.FromLayerComboBox, self.FromLayerButton
        )
        TransformationCalcDialog.setTabOrder(self.FromLayerButton, self.ToFileButton)
        TransformationCalcDialog.setTabOrder(self.ToFileButton, self.AddButton)
        TransformationCalcDialog.setTabOrder(self.AddButton, self.RemoveButton)
        TransformationCalcDialog.setTabOrder(self.RemoveButton, self.OrthogonalRadio)
        TransformationCalcDialog.setTabOrder(self.OrthogonalRadio, self.AffineRadio)
        TransformationCalcDialog.setTabOrder(self.AffineRadio, self.ThirdRadio)
        TransformationCalcDialog.setTabOrder(self.ThirdRadio, self.FourthRadio)
        TransformationCalcDialog.setTabOrder(self.FourthRadio, self.FifthRadio)
        TransformationCalcDialog.setTabOrder(self.FifthRadio, self.ResultTextBrowser)
        TransformationCalcDialog.setTabOrder(self.ResultTextBrowser, self.HelpButton)
        TransformationCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        TransformationCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        TransformationCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, TransformationCalcDialog):
        _translate = QtCore.QCoreApplication.translate
        TransformationCalcDialog.setWindowTitle(
            _translate("TransformationCalcDialog", "Coordinate Transformation")
        )
        self.LayersGroup.setTitle(_translate("TransformationCalcDialog", "Layers"))
        self.FromLayerButton.setText(_translate("TransformationCalcDialog", "..."))
        self.ToFileButton.setText(_translate("TransformationCalcDialog", "..."))
        self.FromLayerLabel.setText(
            _translate("TransformationCalcDialog", "From Layer")
        )
        self.ToLayerLabel.setText(
            _translate("TransformationCalcDialog", "To Shape file")
        )
        self.PointsGroup.setTitle(_translate("TransformationCalcDialog", "Points"))
        self.RemoveButton.setText(_translate("TransformationCalcDialog", "< Remove"))
        self.CommonPoints_Label.setText(
            _translate("TransformationCalcDialog", "Common Points")
        )
        self.PointsofTrans_Label.setText(
            _translate("TransformationCalcDialog", "Used Points")
        )
        self.AddButton.setText(_translate("TransformationCalcDialog", "Add >"))
        self.RadioGroup.setTitle(_translate("TransformationCalcDialog", "Type"))
        self.OrthogonalRadio.setText(
            _translate("TransformationCalcDialog", "Orthogonal")
        )
        self.AffineRadio.setText(_translate("TransformationCalcDialog", "Affine"))
        self.ThirdRadio.setText(_translate("TransformationCalcDialog", "3rd order"))
        self.FourthRadio.setText(_translate("TransformationCalcDialog", "4th order"))
        self.FifthRadio.setText(_translate("TransformationCalcDialog", "5th order"))
        self.CalcButton.setText(_translate("TransformationCalcDialog", "Calculate"))
        self.ResultGroup.setTitle(
            _translate(
                "TransformationCalcDialog", "Result of Coordinate Transformation"
            )
        )
        self.ResultTextBrowser.setHtml(
            _translate(
                "TransformationCalcDialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Courier New'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>",
            )
        )
        self.HelpButton.setText(_translate("TransformationCalcDialog", "Help"))
        self.CloseButton.setText(_translate("TransformationCalcDialog", "Close"))
        self.ResetButton.setText(_translate("TransformationCalcDialog", "Reset"))
