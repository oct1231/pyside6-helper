# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ProjectWidget(object):
    def setupUi(self, ProjectWidget):
        if not ProjectWidget.objectName():
            ProjectWidget.setObjectName(u"ProjectWidget")
        ProjectWidget.resize(682, 410)
        self.verticalLayout = QVBoxLayout(ProjectWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(ProjectWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_32 = QPushButton(self.widget_3)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_32)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_9 = QPushButton(self.widget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.pushButton_10 = QPushButton(self.widget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_12 = QPushButton(self.widget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_6.addWidget(self.pushButton_12)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addWidget(self.widget_3)

        self.groupBox = QGroupBox(ProjectWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.label_16, 1, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.groupBox)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_22, 1, 3, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 1, 5, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.label_14, 0, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 0, 5, 1, 1)

        self.pushButton_21 = QPushButton(self.groupBox)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_21, 0, 3, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 1, 8, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 0, 8, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.label_19, 1, 4, 1, 1)

        self.pushButton_26 = QPushButton(self.groupBox)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_26, 0, 6, 1, 1)

        self.pushButton_29 = QPushButton(self.groupBox)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMaximumSize(QSize(545445, 16777215))

        self.gridLayout.addWidget(self.pushButton_29, 1, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.groupBox)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_27, 1, 6, 1, 1)

        self.pushButton_28 = QPushButton(self.groupBox)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.pushButton_28, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 2, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 7, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 7, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(ProjectWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 1, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 2, 4, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_2.addWidget(self.lineEdit_12, 1, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(111, 0))

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.pushButton_48 = QPushButton(self.groupBox_2)
        self.pushButton_48.setObjectName(u"pushButton_48")

        self.gridLayout_2.addWidget(self.pushButton_48, 2, 3, 1, 1)

        self.pushButton_49 = QPushButton(self.groupBox_2)
        self.pushButton_49.setObjectName(u"pushButton_49")

        self.gridLayout_2.addWidget(self.pushButton_49, 1, 3, 1, 1)

        self.pushButton_43 = QPushButton(self.groupBox_2)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_43, 2, 2, 1, 1)

        self.pushButton_45 = QPushButton(self.groupBox_2)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_45, 1, 2, 1, 1)

        self.lineEdit_16 = QLineEdit(self.groupBox_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_2.addWidget(self.lineEdit_16, 2, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(111, 0))

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.pushButton_46 = QPushButton(self.groupBox_2)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_46, 0, 2, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_2.addWidget(self.lineEdit_15, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 0, 4, 1, 1)

        self.pushButton_44 = QPushButton(self.groupBox_2)
        self.pushButton_44.setObjectName(u"pushButton_44")

        self.gridLayout_2.addWidget(self.pushButton_44, 0, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(111, 0))

        self.gridLayout_2.addWidget(self.label_25, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.listWidget_2 = QListWidget(ProjectWidget)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout.addWidget(self.listWidget_2)

        self.verticalSpacer = QSpacerItem(373, 14, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ProjectWidget)

        QMetaObject.connectSlotsByName(ProjectWidget)
    # setupUi

    def retranslateUi(self, ProjectWidget):
        ProjectWidget.setWindowTitle(QCoreApplication.translate("ProjectWidget", u"Form", None))
        self.pushButton_32.setText(QCoreApplication.translate("ProjectWidget", u"running", None))
        self.pushButton_6.setText(QCoreApplication.translate("ProjectWidget", u"run", None))
        self.pushButton_9.setText(QCoreApplication.translate("ProjectWidget", u"setting", None))
        self.pushButton_10.setText(QCoreApplication.translate("ProjectWidget", u"ok", None))
        self.pushButton_12.setText(QCoreApplication.translate("ProjectWidget", u"cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("ProjectWidget", u"Dir Observers", None))
        self.label_16.setText(QCoreApplication.translate("ProjectWidget", u"rcc", None))
        self.pushButton_22.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.label_14.setText(QCoreApplication.translate("ProjectWidget", u"output", None))
        self.label_4.setText(QCoreApplication.translate("ProjectWidget", u"uic", None))
        self.pushButton_21.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.pushButton_11.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.pushButton_7.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.label_19.setText(QCoreApplication.translate("ProjectWidget", u"output", None))
        self.pushButton_26.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.pushButton_29.setText(QCoreApplication.translate("ProjectWidget", u"error", None))
        self.pushButton_27.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.pushButton_28.setText(QCoreApplication.translate("ProjectWidget", u"invalid", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("ProjectWidget", u"Tools", None))
        self.label_20.setText(QCoreApplication.translate("ProjectWidget", u"designer", None))
        self.pushButton_48.setText(QCoreApplication.translate("ProjectWidget", u"start", None))
        self.pushButton_49.setText(QCoreApplication.translate("ProjectWidget", u"start", None))
        self.pushButton_43.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.pushButton_45.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.label_23.setText(QCoreApplication.translate("ProjectWidget", u"qt assistant ", None))
        self.pushButton_46.setText(QCoreApplication.translate("ProjectWidget", u"...", None))
        self.pushButton_44.setText(QCoreApplication.translate("ProjectWidget", u"start", None))
        self.label_25.setText(QCoreApplication.translate("ProjectWidget", u"linguist", None))
    # retranslateUi

