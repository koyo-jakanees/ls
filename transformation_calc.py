# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transformation_calc.ui'
#
# Created: Sun Nov 23 22:32:23 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TransformationCalcDialog(object):
    def setupUi(self, TransformationCalcDialog):
        TransformationCalcDialog.setObjectName(_fromUtf8("TransformationCalcDialog"))
        TransformationCalcDialog.resize(711, 471)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TransformationCalcDialog.sizePolicy().hasHeightForWidth())
        TransformationCalcDialog.setSizePolicy(sizePolicy)
        TransformationCalcDialog.setMinimumSize(QtCore.QSize(711, 471))
        TransformationCalcDialog.setMaximumSize(QtCore.QSize(711, 471))
        TransformationCalcDialog.setWindowTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Coordinate Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.LayersGroup = QtGui.QGroupBox(TransformationCalcDialog)
        self.LayersGroup.setGeometry(QtCore.QRect(10, 10, 181, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LayersGroup.sizePolicy().hasHeightForWidth())
        self.LayersGroup.setSizePolicy(sizePolicy)
        self.LayersGroup.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.LayersGroup.setObjectName(_fromUtf8("LayersGroup"))
        self.FromLayerComboBox = QtGui.QComboBox(self.LayersGroup)
        self.FromLayerComboBox.setGeometry(QtCore.QRect(10, 60, 161, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FromLayerComboBox.sizePolicy().hasHeightForWidth())
        self.FromLayerComboBox.setSizePolicy(sizePolicy)
        self.FromLayerComboBox.setObjectName(_fromUtf8("FromLayerComboBox"))
        self.FromLayerButton = QtGui.QToolButton(self.LayersGroup)
        self.FromLayerButton.setEnabled(False)
        self.FromLayerButton.setGeometry(QtCore.QRect(120, 100, 51, 20))
        self.FromLayerButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.FromLayerButton.setObjectName(_fromUtf8("FromLayerButton"))
        self.ToFileButton = QtGui.QToolButton(self.LayersGroup)
        self.ToFileButton.setGeometry(QtCore.QRect(120, 210, 51, 19))
        self.ToFileButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.ToFileButton.setObjectName(_fromUtf8("ToFileButton"))
        self.FromLayerLabel = QtGui.QLabel(self.LayersGroup)
        self.FromLayerLabel.setGeometry(QtCore.QRect(10, 30, 151, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FromLayerLabel.sizePolicy().hasHeightForWidth())
        self.FromLayerLabel.setSizePolicy(sizePolicy)
        self.FromLayerLabel.setText(QtGui.QApplication.translate("TransformationCalcDialog", "From Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.FromLayerLabel.setObjectName(_fromUtf8("FromLayerLabel"))
        self.ToLayerLabel = QtGui.QLabel(self.LayersGroup)
        self.ToLayerLabel.setGeometry(QtCore.QRect(10, 140, 151, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToLayerLabel.sizePolicy().hasHeightForWidth())
        self.ToLayerLabel.setSizePolicy(sizePolicy)
        self.ToLayerLabel.setText(QtGui.QApplication.translate("TransformationCalcDialog", "To Shape file", None, QtGui.QApplication.UnicodeUTF8))
        self.ToLayerLabel.setObjectName(_fromUtf8("ToLayerLabel"))
        self.ToShapeEdit = QtGui.QLineEdit(self.LayersGroup)
        self.ToShapeEdit.setEnabled(False)
        self.ToShapeEdit.setGeometry(QtCore.QRect(10, 160, 161, 31))
        self.ToShapeEdit.setObjectName(_fromUtf8("ToShapeEdit"))
        self.PointsGroup = QtGui.QGroupBox(TransformationCalcDialog)
        self.PointsGroup.setGeometry(QtCore.QRect(210, 10, 361, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsGroup.sizePolicy().hasHeightForWidth())
        self.PointsGroup.setSizePolicy(sizePolicy)
        self.PointsGroup.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.PointsGroup.setObjectName(_fromUtf8("PointsGroup"))
        self.RemoveButton = QtGui.QPushButton(self.PointsGroup)
        self.RemoveButton.setGeometry(QtCore.QRect(140, 190, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy)
        self.RemoveButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.RemoveButton.setObjectName(_fromUtf8("RemoveButton"))
        self.CommonPoints_Label = QtGui.QLabel(self.PointsGroup)
        self.CommonPoints_Label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CommonPoints_Label.sizePolicy().hasHeightForWidth())
        self.CommonPoints_Label.setSizePolicy(sizePolicy)
        self.CommonPoints_Label.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Common Points", None, QtGui.QApplication.UnicodeUTF8))
        self.CommonPoints_Label.setObjectName(_fromUtf8("CommonPoints_Label"))
        self.PointsofTrans_Label = QtGui.QLabel(self.PointsGroup)
        self.PointsofTrans_Label.setGeometry(QtCore.QRect(230, 20, 141, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PointsofTrans_Label.sizePolicy().hasHeightForWidth())
        self.PointsofTrans_Label.setSizePolicy(sizePolicy)
        self.PointsofTrans_Label.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Used Points", None, QtGui.QApplication.UnicodeUTF8))
        self.PointsofTrans_Label.setObjectName(_fromUtf8("PointsofTrans_Label"))
        self.AddButton = QtGui.QPushButton(self.PointsGroup)
        self.AddButton.setGeometry(QtCore.QRect(140, 60, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Add >", None, QtGui.QApplication.UnicodeUTF8))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.CommonList = QtGui.QListWidget(self.PointsGroup)
        self.CommonList.setGeometry(QtCore.QRect(10, 40, 121, 201))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CommonList.sizePolicy().hasHeightForWidth())
        self.CommonList.setSizePolicy(sizePolicy)
        self.CommonList.setObjectName(_fromUtf8("CommonList"))
        self.UsedList = QtGui.QListWidget(self.PointsGroup)
        self.UsedList.setGeometry(QtCore.QRect(230, 40, 121, 201))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UsedList.sizePolicy().hasHeightForWidth())
        self.UsedList.setSizePolicy(sizePolicy)
        self.UsedList.setObjectName(_fromUtf8("UsedList"))
        self.RadioGroup = QtGui.QGroupBox(TransformationCalcDialog)
        self.RadioGroup.setGeometry(QtCore.QRect(590, 10, 111, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadioGroup.sizePolicy().hasHeightForWidth())
        self.RadioGroup.setSizePolicy(sizePolicy)
        self.RadioGroup.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.RadioGroup.setObjectName(_fromUtf8("RadioGroup"))
        self.OrthogonalRadio = QtGui.QRadioButton(self.RadioGroup)
        self.OrthogonalRadio.setGeometry(QtCore.QRect(10, 30, 191, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrthogonalRadio.sizePolicy().hasHeightForWidth())
        self.OrthogonalRadio.setSizePolicy(sizePolicy)
        self.OrthogonalRadio.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Orthogonal", None, QtGui.QApplication.UnicodeUTF8))
        self.OrthogonalRadio.setObjectName(_fromUtf8("OrthogonalRadio"))
        self.AffineRadio = QtGui.QRadioButton(self.RadioGroup)
        self.AffineRadio.setGeometry(QtCore.QRect(10, 60, 191, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AffineRadio.sizePolicy().hasHeightForWidth())
        self.AffineRadio.setSizePolicy(sizePolicy)
        self.AffineRadio.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Affine", None, QtGui.QApplication.UnicodeUTF8))
        self.AffineRadio.setObjectName(_fromUtf8("AffineRadio"))
        self.ThirdRadio = QtGui.QRadioButton(self.RadioGroup)
        self.ThirdRadio.setGeometry(QtCore.QRect(10, 90, 171, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThirdRadio.sizePolicy().hasHeightForWidth())
        self.ThirdRadio.setSizePolicy(sizePolicy)
        self.ThirdRadio.setText(QtGui.QApplication.translate("TransformationCalcDialog", "3rd order", None, QtGui.QApplication.UnicodeUTF8))
        self.ThirdRadio.setObjectName(_fromUtf8("ThirdRadio"))
        self.FourthRradio = QtGui.QRadioButton(self.RadioGroup)
        self.FourthRradio.setGeometry(QtCore.QRect(10, 120, 151, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FourthRradio.sizePolicy().hasHeightForWidth())
        self.FourthRradio.setSizePolicy(sizePolicy)
        self.FourthRradio.setText(QtGui.QApplication.translate("TransformationCalcDialog", "4th order", None, QtGui.QApplication.UnicodeUTF8))
        self.FourthRradio.setObjectName(_fromUtf8("FourthRradio"))
        self.FifthRadio = QtGui.QRadioButton(self.RadioGroup)
        self.FifthRadio.setGeometry(QtCore.QRect(10, 150, 181, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FifthRadio.sizePolicy().hasHeightForWidth())
        self.FifthRadio.setSizePolicy(sizePolicy)
        self.FifthRadio.setText(QtGui.QApplication.translate("TransformationCalcDialog", "5th order", None, QtGui.QApplication.UnicodeUTF8))
        self.FifthRadio.setObjectName(_fromUtf8("FifthRadio"))
        self.CalcButton = QtGui.QPushButton(TransformationCalcDialog)
        self.CalcButton.setGeometry(QtCore.QRect(410, 440, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalcButton.sizePolicy().hasHeightForWidth())
        self.CalcButton.setSizePolicy(sizePolicy)
        self.CalcButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.CalcButton.setObjectName(_fromUtf8("CalcButton"))
        self.ResultGroup = QtGui.QGroupBox(TransformationCalcDialog)
        self.ResultGroup.setGeometry(QtCore.QRect(10, 270, 691, 151))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultGroup.sizePolicy().hasHeightForWidth())
        self.ResultGroup.setSizePolicy(sizePolicy)
        self.ResultGroup.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Result of Coordinate Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.ResultGroup.setObjectName(_fromUtf8("ResultGroup"))
        self.ResultTextBrowser = QtGui.QTextBrowser(self.ResultGroup)
        self.ResultTextBrowser.setGeometry(QtCore.QRect(10, 20, 671, 121))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultTextBrowser.sizePolicy().hasHeightForWidth())
        self.ResultTextBrowser.setSizePolicy(sizePolicy)
        self.ResultTextBrowser.setHtml(QtGui.QApplication.translate("TransformationCalcDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ResultTextBrowser.setObjectName(_fromUtf8("ResultTextBrowser"))
        self.HelpButton = QtGui.QPushButton(TransformationCalcDialog)
        self.HelpButton.setGeometry(QtCore.QRect(20, 440, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.HelpButton.setObjectName(_fromUtf8("HelpButton"))
        self.CloseButton = QtGui.QPushButton(TransformationCalcDialog)
        self.CloseButton.setGeometry(QtCore.QRect(610, 440, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.ResetButton = QtGui.QPushButton(TransformationCalcDialog)
        self.ResetButton.setGeometry(QtCore.QRect(510, 440, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))

        self.retranslateUi(TransformationCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(TransformationCalcDialog)
        TransformationCalcDialog.setTabOrder(self.FromLayerComboBox, self.FromLayerButton)
        TransformationCalcDialog.setTabOrder(self.FromLayerButton, self.ToFileButton)
        TransformationCalcDialog.setTabOrder(self.ToFileButton, self.AddButton)
        TransformationCalcDialog.setTabOrder(self.AddButton, self.RemoveButton)
        TransformationCalcDialog.setTabOrder(self.RemoveButton, self.OrthogonalRadio)
        TransformationCalcDialog.setTabOrder(self.OrthogonalRadio, self.AffineRadio)
        TransformationCalcDialog.setTabOrder(self.AffineRadio, self.ThirdRadio)
        TransformationCalcDialog.setTabOrder(self.ThirdRadio, self.FourthRradio)
        TransformationCalcDialog.setTabOrder(self.FourthRradio, self.FifthRadio)
        TransformationCalcDialog.setTabOrder(self.FifthRadio, self.ResultTextBrowser)
        TransformationCalcDialog.setTabOrder(self.ResultTextBrowser, self.HelpButton)
        TransformationCalcDialog.setTabOrder(self.HelpButton, self.CalcButton)
        TransformationCalcDialog.setTabOrder(self.CalcButton, self.ResetButton)
        TransformationCalcDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, TransformationCalcDialog):
        pass

