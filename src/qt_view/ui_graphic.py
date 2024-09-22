# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphic.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Graphic(object):
    def setupUi(self, Graphic):
        if not Graphic.objectName():
            Graphic.setObjectName(u"Graphic")
        Graphic.resize(740, 594)
        self.horizontalLayout_2 = QHBoxLayout(Graphic)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(Graphic)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plot = QWidget(self.frame_2)
        self.plot.setObjectName(u"plot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setMinimumSize(QSize(500, 500))

        self.verticalLayout_2.addWidget(self.plot)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.expression = QLabel(self.frame)
        self.expression.setObjectName(u"expression")
        self.expression.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.expression)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(Graphic)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.button_back = QPushButton(self.frame_3)
        self.button_back.setObjectName(u"button_back")
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setMinimumSize(QSize(60, 60))
        self.button_back.setMaximumSize(QSize(9999, 60))
        self.button_back.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.button_back)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.retranslateUi(Graphic)

        QMetaObject.connectSlotsByName(Graphic)
    # setupUi

    def retranslateUi(self, Graphic):
        Graphic.setWindowTitle(QCoreApplication.translate("Graphic", u"Form", None))
        self.expression.setText(QCoreApplication.translate("Graphic", u"None", None))
        self.checkBox.setText(QCoreApplication.translate("Graphic", u"AutoScale", None))
        self.button_back.setText(QCoreApplication.translate("Graphic", u"Back", None))
    # retranslateUi

