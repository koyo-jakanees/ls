from builtins import object

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch_plotting.ui'
#
# Created: Sun Jan 04 11:08:15 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_BatchPlottingDialog(object):
    def setupUi(self, BatchPlottingDialog):
        BatchPlottingDialog.setObjectName(_fromUtf8("BatchPlottingDialog"))
        BatchPlottingDialog.resize(290, 390)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            BatchPlottingDialog.sizePolicy().hasHeightForWidth()
        )
        BatchPlottingDialog.setSizePolicy(sizePolicy)
        BatchPlottingDialog.setMinimumSize(QtCore.QSize(290, 390))
        BatchPlottingDialog.setMaximumSize(QtCore.QSize(290, 390))
        self.TemplateList = QtGui.QListWidget(BatchPlottingDialog)
        self.TemplateList.setGeometry(QtCore.QRect(10, 80, 271, 101))
        self.TemplateList.setObjectName(_fromUtf8("TemplateList"))
        self.TemplateLabel = QtGui.QLabel(BatchPlottingDialog)
        self.TemplateLabel.setGeometry(QtCore.QRect(10, 53, 111, 16))
        self.TemplateLabel.setObjectName(_fromUtf8("TemplateLabel"))
        self.PlotButton = QtGui.QPushButton(BatchPlottingDialog)
        self.PlotButton.setGeometry(QtCore.QRect(50, 360, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotButton.sizePolicy().hasHeightForWidth())
        self.PlotButton.setSizePolicy(sizePolicy)
        self.PlotButton.setObjectName(_fromUtf8("PlotButton"))
        self.CloseButton = QtGui.QPushButton(BatchPlottingDialog)
        self.CloseButton.setGeometry(QtCore.QRect(160, 360, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.ScaleLabel = QtGui.QLabel(BatchPlottingDialog)
        self.ScaleLabel.setGeometry(QtCore.QRect(10, 190, 91, 21))
        self.ScaleLabel.setObjectName(_fromUtf8("ScaleLabel"))
        self.ScaleCombo = QtGui.QComboBox(BatchPlottingDialog)
        self.ScaleCombo.setGeometry(QtCore.QRect(120, 190, 81, 22))
        self.ScaleCombo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.ScaleCombo.setEditable(True)
        self.ScaleCombo.setObjectName(_fromUtf8("ScaleCombo"))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.ScaleCombo.addItem(_fromUtf8(""))
        self.TempDirButton = QtGui.QPushButton(BatchPlottingDialog)
        self.TempDirButton.setGeometry(QtCore.QRect(170, 50, 111, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TempDirButton.sizePolicy().hasHeightForWidth()
        )
        self.TempDirButton.setSizePolicy(sizePolicy)
        self.TempDirButton.setObjectName(_fromUtf8("TempDirButton"))
        self.LayersLabel = QtGui.QLabel(BatchPlottingDialog)
        self.LayersLabel.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.LayersLabel.setObjectName(_fromUtf8("LayersLabel"))
        self.LayersComboBox = QtGui.QComboBox(BatchPlottingDialog)
        self.LayersComboBox.setGeometry(QtCore.QRect(120, 10, 161, 22))
        self.LayersComboBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.LayersComboBox.setEditable(False)
        self.LayersComboBox.setObjectName(_fromUtf8("LayersComboBox"))
        self.OutputTab = QtGui.QTabWidget(BatchPlottingDialog)
        self.OutputTab.setGeometry(QtCore.QRect(10, 230, 271, 121))
        self.OutputTab.setObjectName(_fromUtf8("OutputTab"))
        self.toPDF = QtGui.QWidget()
        self.toPDF.setObjectName(_fromUtf8("toPDF"))
        self.OutputPDFEdit = QtGui.QLineEdit(self.toPDF)
        self.OutputPDFEdit.setGeometry(QtCore.QRect(10, 60, 241, 20))
        self.OutputPDFEdit.setObjectName(_fromUtf8("OutputPDFEdit"))
        self.OutputPDFLabel = QtGui.QLabel(self.toPDF)
        self.OutputPDFLabel.setGeometry(QtCore.QRect(10, 40, 221, 16))
        self.OutputPDFLabel.setObjectName(_fromUtf8("OutputPDFLabel"))
        self.SingleFileCheckbox = QtGui.QCheckBox(self.toPDF)
        self.SingleFileCheckbox.setGeometry(QtCore.QRect(10, 10, 241, 17))
        self.SingleFileCheckbox.setObjectName(_fromUtf8("SingleFileCheckbox"))
        self.OutputTab.addTab(self.toPDF, _fromUtf8(""))
        self.toPrinter = QtGui.QWidget()
        self.toPrinter.setObjectName(_fromUtf8("toPrinter"))
        self.OutputTab.addTab(self.toPrinter, _fromUtf8(""))
        self.toComposerView = QtGui.QWidget()
        self.toComposerView.setObjectName(_fromUtf8("toComposerView"))
        self.ComposerLabel = QtGui.QLabel(self.toComposerView)
        self.ComposerLabel.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.ComposerLabel.setObjectName(_fromUtf8("ComposerLabel"))
        self.ComposerEdit = QtGui.QLineEdit(self.toComposerView)
        self.ComposerEdit.setGeometry(QtCore.QRect(10, 30, 241, 20))
        self.ComposerEdit.setObjectName(_fromUtf8("ComposerEdit"))
        self.ComposerEmptyLabel = QtGui.QLabel(self.toComposerView)
        self.ComposerEmptyLabel.setGeometry(QtCore.QRect(10, 50, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setStrikeOut(False)
        self.ComposerEmptyLabel.setFont(font)
        self.ComposerEmptyLabel.setObjectName(_fromUtf8("ComposerEmptyLabel"))
        self.OutputTab.addTab(self.toComposerView, _fromUtf8(""))
        self.ScaleLabel_2 = QtGui.QLabel(BatchPlottingDialog)
        self.ScaleLabel_2.setGeometry(QtCore.QRect(100, 190, 20, 21))
        self.ScaleLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ScaleLabel_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.ScaleLabel_2.setObjectName(_fromUtf8("ScaleLabel_2"))

        self.retranslateUi(BatchPlottingDialog)
        self.ScaleCombo.setCurrentIndex(3)
        self.LayersComboBox.setCurrentIndex(-1)
        self.OutputTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BatchPlottingDialog)
        BatchPlottingDialog.setTabOrder(self.LayersComboBox, self.TempDirButton)
        BatchPlottingDialog.setTabOrder(self.TempDirButton, self.TemplateList)
        BatchPlottingDialog.setTabOrder(self.TemplateList, self.ScaleCombo)
        BatchPlottingDialog.setTabOrder(self.ScaleCombo, self.PlotButton)
        BatchPlottingDialog.setTabOrder(self.PlotButton, self.CloseButton)

    def retranslateUi(self, BatchPlottingDialog):
        BatchPlottingDialog.setWindowTitle(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Batch Plotting",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.TemplateLabel.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Available templates:",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.PlotButton.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "Plot", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.CloseButton.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "Close", None, QtGui.QApplication.UnicodeUTF8
            )
        )
        self.ScaleLabel.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Map Scale:",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.ScaleCombo.setItemText(
            0,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "100", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            1,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "250", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            2,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "500", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            3,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "1000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            4,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "2000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            5,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "2500", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            6,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "5000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            7,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "10000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            8,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "20000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            9,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "25000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            10,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "50000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.ScaleCombo.setItemText(
            11,
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "100000", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.TempDirButton.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Change Dir ...",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.LayersLabel.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Polygon layers:",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.OutputPDFLabel.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Output filename pattern:",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.SingleFileCheckbox.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Single PDF file (multi-page)",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.OutputTab.setTabText(
            self.OutputTab.indexOf(self.toPDF),
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "To PDF", None, QtGui.QApplication.UnicodeUTF8
            ),
        )
        self.OutputTab.setTabText(
            self.OutputTab.indexOf(self.toPrinter),
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "To Printer",
                None,
                QtGui.QApplication.UnicodeUTF8,
            ),
        )
        self.ComposerLabel.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "Composer name:",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.ComposerEmptyLabel.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "If empty name will be genrated automatically.",
                None,
                QtGui.QApplication.UnicodeUTF8,
            )
        )
        self.OutputTab.setTabText(
            self.OutputTab.indexOf(self.toComposerView),
            QtGui.QApplication.translate(
                "BatchPlottingDialog",
                "To Composer View",
                None,
                QtGui.QApplication.UnicodeUTF8,
            ),
        )
        self.ScaleLabel_2.setText(
            QtGui.QApplication.translate(
                "BatchPlottingDialog", "1:", None, QtGui.QApplication.UnicodeUTF8
            )
        )
