from builtins import object

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_settings.ui'
#
# Created: Mon Jun 29 21:32:02 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from qgis.PyQt import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)


except AttributeError:

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_PluginSettingsDialog(object):
    def setupUi(self, PluginSettingsDialog):
        PluginSettingsDialog.setObjectName(_fromUtf8("PluginSettingsDialog"))
        PluginSettingsDialog.resize(388, 296)
        self.SettingsTab = QtWidgets.QTabWidget(PluginSettingsDialog)
        self.SettingsTab.setGeometry(QtCore.QRect(10, 10, 371, 241))
        self.SettingsTab.setObjectName(_fromUtf8("SettingsTab"))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.HomeDirEdit = QtWidgets.QLineEdit(self.tab)
        self.HomeDirEdit.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.HomeDirEdit.setReadOnly(True)
        self.HomeDirEdit.setObjectName(_fromUtf8("HomeDirEdit"))
        self.LogPathLabel = QtWidgets.QLabel(self.tab)
        self.LogPathLabel.setGeometry(QtCore.QRect(10, 60, 351, 21))
        self.LogPathLabel.setObjectName(_fromUtf8("LogPathLabel"))
        self.HomeDirLabel = QtWidgets.QLabel(self.tab)
        self.HomeDirLabel.setGeometry(QtCore.QRect(10, 10, 351, 21))
        self.HomeDirLabel.setObjectName(_fromUtf8("HomeDirLabel"))
        self.LogPathButton = QtWidgets.QPushButton(self.tab)
        self.LogPathButton.setGeometry(QtCore.QRect(330, 80, 31, 23))
        self.LogPathButton.setObjectName(_fromUtf8("LogPathButton"))
        self.HomeDirButton = QtWidgets.QPushButton(self.tab)
        self.HomeDirButton.setGeometry(QtCore.QRect(330, 30, 31, 23))
        self.HomeDirButton.setObjectName(_fromUtf8("HomeDirButton"))
        self.LogPathEdit = QtWidgets.QLineEdit(self.tab)
        self.LogPathEdit.setGeometry(QtCore.QRect(10, 80, 321, 20))
        self.LogPathEdit.setReadOnly(True)
        self.LogPathEdit.setObjectName(_fromUtf8("LogPathEdit"))
        self.LogPathLabel_2 = QtWidgets.QLabel(self.tab)
        self.LogPathLabel_2.setGeometry(QtCore.QRect(10, 110, 351, 21))
        self.LogPathLabel_2.setObjectName(_fromUtf8("LogPathLabel_2"))
        self.GamaPathEdit = QtWidgets.QLineEdit(self.tab)
        self.GamaPathEdit.setGeometry(QtCore.QRect(10, 130, 321, 20))
        self.GamaPathEdit.setReadOnly(True)
        self.GamaPathEdit.setObjectName(_fromUtf8("GamaPathEdit"))
        self.GamaPathButton = QtWidgets.QPushButton(self.tab)
        self.GamaPathButton.setGeometry(QtCore.QRect(330, 130, 31, 23))
        self.GamaPathButton.setObjectName(_fromUtf8("GamaPathButton"))
        self.PlotTemplateDirEdit = QtWidgets.QLineEdit(self.tab)
        self.PlotTemplateDirEdit.setGeometry(QtCore.QRect(10, 180, 321, 20))
        self.PlotTemplateDirEdit.setReadOnly(True)
        self.PlotTemplateDirEdit.setObjectName(_fromUtf8("PlotTemplateDirEdit"))
        self.PlotTemplateDirButton = QtWidgets.QPushButton(self.tab)
        self.PlotTemplateDirButton.setGeometry(QtCore.QRect(330, 180, 31, 23))
        self.PlotTemplateDirButton.setObjectName(_fromUtf8("PlotTemplateDirButton"))
        self.LogPathLabel_3 = QtWidgets.QLabel(self.tab)
        self.LogPathLabel_3.setGeometry(QtCore.QRect(10, 160, 351, 21))
        self.LogPathLabel_3.setObjectName(_fromUtf8("LogPathLabel_3"))
        self.SettingsTab.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.FontLabel = QtWidgets.QLabel(self.tab_3)
        self.FontLabel.setGeometry(QtCore.QRect(10, 10, 351, 41))
        self.FontLabel.setScaledContents(False)
        self.FontLabel.setWordWrap(True)
        self.FontLabel.setObjectName(_fromUtf8("FontLabel"))
        self.FontNameLabel = QtWidgets.QLabel(self.tab_3)
        self.FontNameLabel.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.FontNameLabel.setObjectName(_fromUtf8("FontNameLabel"))
        self.FontNameCombo = QtWidgets.QFontComboBox(self.tab_3)
        self.FontNameCombo.setGeometry(QtCore.QRect(90, 60, 156, 21))
        self.FontNameCombo.setEditable(False)
        self.FontNameCombo.setFontFilters(QtWidgets.QFontComboBox.MonospacedFonts)
        font = QtWidgets.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        self.FontNameCombo.setCurrentFont(font)
        self.FontNameCombo.setObjectName(_fromUtf8("FontNameCombo"))
        self.FontSizeLabel = QtWidgets.QLabel(self.tab_3)
        self.FontSizeLabel.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.FontSizeLabel.setObjectName(_fromUtf8("FontSizeLabel"))
        self.FontSizeCombo = QtWidgets.QComboBox(self.tab_3)
        self.FontSizeCombo.setGeometry(QtCore.QRect(90, 90, 41, 22))
        self.FontSizeCombo.setObjectName(_fromUtf8("FontSizeCombo"))
        self.SettingsTab.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.LineToleranceLabel = QtWidgets.QLabel(self.tab_2)
        self.LineToleranceLabel.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.LineToleranceLabel.setObjectName(_fromUtf8("LineToleranceLabel"))
        self.LineToleranceEdit = QtWidgets.QLineEdit(self.tab_2)
        self.LineToleranceEdit.setGeometry(QtCore.QRect(140, 10, 121, 20))
        self.LineToleranceEdit.setObjectName(_fromUtf8("LineToleranceEdit"))
        self.AreaToleranceLabel = QtWidgets.QLabel(self.tab_2)
        self.AreaToleranceLabel.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.AreaToleranceLabel.setObjectName(_fromUtf8("AreaToleranceLabel"))
        self.AreaToleranceEdit = QtWidgets.QLineEdit(self.tab_2)
        self.AreaToleranceEdit.setGeometry(QtCore.QRect(140, 40, 121, 20))
        self.AreaToleranceEdit.setObjectName(_fromUtf8("AreaToleranceEdit"))
        self.MaxIterationLabel = QtWidgets.QLabel(self.tab_2)
        self.MaxIterationLabel.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.MaxIterationLabel.setObjectName(_fromUtf8("MaxIterationLabel"))
        self.MaxIterationEdit = QtWidgets.QLineEdit(self.tab_2)
        self.MaxIterationEdit.setGeometry(QtCore.QRect(140, 70, 121, 20))
        self.MaxIterationEdit.setObjectName(_fromUtf8("MaxIterationEdit"))
        self.SettingsTab.addTab(self.tab_2, _fromUtf8(""))
        self.OKButton = QtWidgets.QPushButton(PluginSettingsDialog)
        self.OKButton.setGeometry(QtCore.QRect(190, 260, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OKButton.sizePolicy().hasHeightForWidth())
        self.OKButton.setSizePolicy(sizePolicy)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.CancelButton = QtWidgets.QPushButton(PluginSettingsDialog)
        self.CancelButton.setGeometry(QtCore.QRect(290, 260, 81, 23))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(PluginSettingsDialog)
        self.SettingsTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PluginSettingsDialog)
        PluginSettingsDialog.setTabOrder(self.SettingsTab, self.HomeDirEdit)
        PluginSettingsDialog.setTabOrder(self.HomeDirEdit, self.HomeDirButton)
        PluginSettingsDialog.setTabOrder(self.HomeDirButton, self.LogPathEdit)
        PluginSettingsDialog.setTabOrder(self.LogPathEdit, self.LogPathButton)
        PluginSettingsDialog.setTabOrder(self.LogPathButton, self.GamaPathEdit)
        PluginSettingsDialog.setTabOrder(self.GamaPathEdit, self.GamaPathButton)
        PluginSettingsDialog.setTabOrder(self.GamaPathButton, self.PlotTemplateDirEdit)
        PluginSettingsDialog.setTabOrder(
            self.PlotTemplateDirEdit, self.PlotTemplateDirButton
        )
        PluginSettingsDialog.setTabOrder(self.PlotTemplateDirButton, self.FontNameCombo)
        PluginSettingsDialog.setTabOrder(self.FontNameCombo, self.FontSizeCombo)
        PluginSettingsDialog.setTabOrder(self.FontSizeCombo, self.LineToleranceEdit)
        PluginSettingsDialog.setTabOrder(self.LineToleranceEdit, self.AreaToleranceEdit)
        PluginSettingsDialog.setTabOrder(self.AreaToleranceEdit, self.MaxIterationEdit)
        PluginSettingsDialog.setTabOrder(self.MaxIterationEdit, self.OKButton)
        PluginSettingsDialog.setTabOrder(self.OKButton, self.CancelButton)

    def retranslateUi(self, PluginSettingsDialog):
        PluginSettingsDialog.setWindowTitle(
            _translate("PluginSettingsDialog", "Plugin Settings", None)
        )
        self.HomeDirEdit.setToolTip(
            _translate(
                "PluginSettingsDialog",
                "Default directory for loading fieldbooks.",
                None,
            )
        )
        self.LogPathLabel.setToolTip(
            _translate("PluginSettingsDialog", "Directory for log file.", None)
        )
        self.LogPathLabel.setText(
            _translate("PluginSettingsDialog", "Path to Log File:", None)
        )
        self.HomeDirLabel.setToolTip(
            _translate(
                "PluginSettingsDialog",
                "Default directory for loading fieldbooks.",
                None,
            )
        )
        self.HomeDirLabel.setText(
            _translate("PluginSettingsDialog", "Home directory:", None)
        )
        self.LogPathButton.setText(_translate("PluginSettingsDialog", "...", None))
        self.HomeDirButton.setText(_translate("PluginSettingsDialog", "...", None))
        self.LogPathEdit.setToolTip(
            _translate("PluginSettingsDialog", "Path for log file.", None)
        )
        self.LogPathLabel_2.setToolTip(
            _translate("PluginSettingsDialog", "Directory for log file.", None)
        )
        self.LogPathLabel_2.setText(
            _translate("PluginSettingsDialog", "Path to GNU Gama executable:", None)
        )
        self.GamaPathEdit.setToolTip(
            _translate(
                "PluginSettingsDialog", "Full path to gama-local executable.", None
            )
        )
        self.GamaPathButton.setText(_translate("PluginSettingsDialog", "...", None))
        self.PlotTemplateDirEdit.setToolTip(
            _translate(
                "PluginSettingsDialog",
                "Path to template files for batch plotting.",
                None,
            )
        )
        self.PlotTemplateDirButton.setText(
            _translate("PluginSettingsDialog", "...", None)
        )
        self.LogPathLabel_3.setToolTip(
            _translate("PluginSettingsDialog", "Directory for log file.", None)
        )
        self.LogPathLabel_3.setText(
            _translate("PluginSettingsDialog", "Plot Template directory:", None)
        )
        self.SettingsTab.setTabText(
            self.SettingsTab.indexOf(self.tab),
            _translate("PluginSettingsDialog", "Directories", None),
        )
        self.FontLabel.setText(
            _translate(
                "PluginSettingsDialog",
                "Monospace font used in the calculation results widgets on Linux. On Windows it is courier font.",
                None,
            )
        )
        self.FontNameLabel.setText(
            _translate("PluginSettingsDialog", "Font name:", None)
        )
        self.FontSizeLabel.setText(
            _translate("PluginSettingsDialog", "Font size:", None)
        )
        self.SettingsTab.setTabText(
            self.SettingsTab.indexOf(self.tab_3),
            _translate("PluginSettingsDialog", "Font", None),
        )
        self.LineToleranceLabel.setText(
            _translate("PluginSettingsDialog", "Snap tolerance:", None)
        )
        self.LineToleranceEdit.setToolTip(
            _translate("PluginSettingsDialog", "Snapping tolerance to line tool.", None)
        )
        self.AreaToleranceLabel.setText(
            _translate("PluginSettingsDialog", "Area tolerance:", None)
        )
        self.AreaToleranceEdit.setToolTip(
            _translate(
                "PluginSettingsDialog", "Area tolerance for area division.", None
            )
        )
        self.MaxIterationLabel.setText(
            _translate("PluginSettingsDialog", "Max. iterations:", None)
        )
        self.MaxIterationEdit.setToolTip(
            _translate(
                "PluginSettingsDialog",
                "Maximal number of iterations for area division.",
                None,
            )
        )
        self.SettingsTab.setTabText(
            self.SettingsTab.indexOf(self.tab_2),
            _translate("PluginSettingsDialog", "Area division", None),
        )
        self.OKButton.setText(_translate("PluginSettingsDialog", "OK", None))
        self.CancelButton.setText(_translate("PluginSettingsDialog", "Cancel", None))
