# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 702)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_5.addWidget(self.widget)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 411, 606))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_5.addWidget(self.scrollArea)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_5 = QtWidgets.QWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_21 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setScaledContents(False)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_21)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_3.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem4)
        self.label_22 = QtWidgets.QLabel(self.widget_5)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_23 = QtWidgets.QLabel(self.widget_5)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_24 = QtWidgets.QLabel(self.widget_5)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.pushButton_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(10, QtWidgets.QFormLayout.SpanningRole, spacerItem5)
        self.label_25 = QtWidgets.QLabel(self.widget_5)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.label_25)
        self.label_26 = QtWidgets.QLabel(self.widget_5)
        self.label_26.setObjectName("label_26")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton_9)
        self.verticalLayout_9.addLayout(self.formLayout_3)
        self.horizontalLayout_11.addWidget(self.widget_5)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 411, 606))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableWidget_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_11.addWidget(self.scrollArea_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.tab_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.horizontalSlider = QtWidgets.QSlider(self.widget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Track"))
        self.label.setText(_translate("MainWindow", "??????????"))
        self.label_2.setText(_translate("MainWindow", "??????????"))
        self.label_3.setText(_translate("MainWindow", "????????"))
        self.pushButton.setText(_translate("MainWindow", "????????????????"))
        self.label_6.setText(_translate("MainWindow", "?????? ????????????????."))
        self.label_5.setText(_translate("MainWindow", "?????????? "))
        self.pushButton_2.setText(_translate("MainWindow", "??????????????"))
        self.label_8.setText(_translate("MainWindow", "??????f?????? ???????????????? ???????????????????? ?? ?????????????????? huba"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "??????????????"))
        self.label_21.setText(_translate("MainWindow", "HUB"))
        self.label_22.setText(_translate("MainWindow", "??????"))
        self.label_23.setText(_translate("MainWindow", "??????????????"))
        self.label_24.setText(_translate("MainWindow", "????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "????????????????"))
        self.label_25.setText(_translate("MainWindow", "?????? ????????????????."))
        self.label_26.setText(_translate("MainWindow", "?????????? "))
        self.pushButton_6.setText(_translate("MainWindow", "??????????????"))
        self.pushButton_7.setText(_translate("MainWindow", "?????????????? ??????"))
        self.pushButton_8.setText(_translate("MainWindow", "?????????????? ??????"))
        self.pushButton_9.setText(_translate("MainWindow", "?????????????????? ??????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "HUBs"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "??????????"))
