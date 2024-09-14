# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 401)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setMaximumSize(QSize(684, 412))
        MainWindow.setStyleSheet(u"* {\n"
"	background-color: #2e2e2e;\n"
"	color: #ffffff;\n"
"	font-family: 'Open Sans';\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #bf3b3b;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #d4d4d4;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #d45c5c;\n"
"    border-style: inset;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #8a2828;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #d4d4d4;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"#button_0, #button_1, #button_2, #button_3, #button_4, \n"
"#button_5, #button_6, #button_7, #button_8, #button_9 {\n"
"    background-color: #8f0d23;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
""
                        "\n"
"#button_0:hover, #button_1:hover, #button_2:hover, #button_3:hover, #button_4:hover, #button_5:hover, #button_6:hover, #button_7:hover, #button_8:hover, #button_9:hover {\n"
"    background-color: #99182e;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"#button_0:pressed, #button_1:pressed, #button_2:pressed, #button_3:pressed, #button_4:pressed, #button_5:pressed, #button_6:pressed, #button_7:pressed, #button_8:pressed, #button_9:pressed {\n"
"    background-color: #3b050e;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy1)
        self.input.setMinimumSize(QSize(500, 50))
        self.input.setMaximumSize(QSize(16777215, 50))
        self.input.setStyleSheet(u"")
        self.input.setMaxLength(255)
        self.input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.input)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_equal = QPushButton(self.frame)
        self.button_equal.setObjectName(u"button_equal")
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        self.button_equal.setMinimumSize(QSize(120, 60))
        self.button_equal.setMaximumSize(QSize(120, 60))
        self.button_equal.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_equal, 0, 11, 1, 1)

        self.button_log = QPushButton(self.frame)
        self.button_log.setObjectName(u"button_log")
        sizePolicy.setHeightForWidth(self.button_log.sizePolicy().hasHeightForWidth())
        self.button_log.setSizePolicy(sizePolicy)
        self.button_log.setMinimumSize(QSize(60, 60))
        self.button_log.setMaximumSize(QSize(60, 60))
        self.button_log.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_log, 2, 5, 1, 1)

        self.button_1 = QPushButton(self.frame)
        self.button_1.setObjectName(u"button_1")
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QSize(60, 60))
        self.button_1.setMaximumSize(QSize(60, 60))
        self.button_1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_1, 0, 6, 1, 1)

        self.button_asin = QPushButton(self.frame)
        self.button_asin.setObjectName(u"button_asin")
        sizePolicy.setHeightForWidth(self.button_asin.sizePolicy().hasHeightForWidth())
        self.button_asin.setSizePolicy(sizePolicy)
        self.button_asin.setMinimumSize(QSize(60, 60))
        self.button_asin.setMaximumSize(QSize(60, 60))
        self.button_asin.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_asin, 1, 3, 1, 1)

        self.button_2 = QPushButton(self.frame)
        self.button_2.setObjectName(u"button_2")
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QSize(60, 60))
        self.button_2.setMaximumSize(QSize(60, 60))
        self.button_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_2, 0, 7, 1, 1)

        self.button_rigth_bracket = QPushButton(self.frame)
        self.button_rigth_bracket.setObjectName(u"button_rigth_bracket")
        sizePolicy.setHeightForWidth(self.button_rigth_bracket.sizePolicy().hasHeightForWidth())
        self.button_rigth_bracket.setSizePolicy(sizePolicy)
        self.button_rigth_bracket.setMinimumSize(QSize(60, 60))
        self.button_rigth_bracket.setMaximumSize(QSize(60, 60))
        self.button_rigth_bracket.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_rigth_bracket, 2, 12, 1, 1)

        self.button_atan = QPushButton(self.frame)
        self.button_atan.setObjectName(u"button_atan")
        sizePolicy.setHeightForWidth(self.button_atan.sizePolicy().hasHeightForWidth())
        self.button_atan.setSizePolicy(sizePolicy)
        self.button_atan.setMinimumSize(QSize(60, 60))
        self.button_atan.setMaximumSize(QSize(60, 60))
        self.button_atan.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_atan, 1, 5, 1, 1)

        self.button_6 = QPushButton(self.frame)
        self.button_6.setObjectName(u"button_6")
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QSize(60, 60))
        self.button_6.setMaximumSize(QSize(60, 60))
        self.button_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_6, 1, 8, 1, 1)

        self.button_plus = QPushButton(self.frame)
        self.button_plus.setObjectName(u"button_plus")
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setMinimumSize(QSize(60, 60))
        self.button_plus.setMaximumSize(QSize(60, 60))
        self.button_plus.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_plus, 0, 10, 1, 1)

        self.button_4 = QPushButton(self.frame)
        self.button_4.setObjectName(u"button_4")
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QSize(60, 60))
        self.button_4.setMaximumSize(QSize(60, 60))
        self.button_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_4, 1, 6, 1, 1)

        self.button_ac = QPushButton(self.frame)
        self.button_ac.setObjectName(u"button_ac")
        sizePolicy.setHeightForWidth(self.button_ac.sizePolicy().hasHeightForWidth())
        self.button_ac.setSizePolicy(sizePolicy)
        self.button_ac.setMinimumSize(QSize(60, 60))
        self.button_ac.setMaximumSize(QSize(60, 60))
        self.button_ac.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_ac, 1, 12, 1, 1)

        self.button_mult = QPushButton(self.frame)
        self.button_mult.setObjectName(u"button_mult")
        sizePolicy.setHeightForWidth(self.button_mult.sizePolicy().hasHeightForWidth())
        self.button_mult.setSizePolicy(sizePolicy)
        self.button_mult.setMinimumSize(QSize(60, 60))
        self.button_mult.setMaximumSize(QSize(60, 60))
        self.button_mult.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_mult, 2, 10, 1, 1)

        self.button_00 = QPushButton(self.frame)
        self.button_00.setObjectName(u"button_00")
        sizePolicy.setHeightForWidth(self.button_00.sizePolicy().hasHeightForWidth())
        self.button_00.setSizePolicy(sizePolicy)
        self.button_00.setMinimumSize(QSize(60, 60))
        self.button_00.setMaximumSize(QSize(60, 60))
        self.button_00.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_00, 3, 6, 1, 1)

        self.button_3 = QPushButton(self.frame)
        self.button_3.setObjectName(u"button_3")
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QSize(60, 60))
        self.button_3.setMaximumSize(QSize(60, 60))
        self.button_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_3, 0, 8, 1, 1)

        self.button_div = QPushButton(self.frame)
        self.button_div.setObjectName(u"button_div")
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        self.button_div.setMinimumSize(QSize(60, 60))
        self.button_div.setMaximumSize(QSize(60, 60))
        self.button_div.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_div, 3, 10, 1, 1)

        self.button_0 = QPushButton(self.frame)
        self.button_0.setObjectName(u"button_0")
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setMinimumSize(QSize(60, 60))
        self.button_0.setMaximumSize(QSize(60, 60))
        self.button_0.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_0, 3, 7, 1, 1)

        self.button_pow = QPushButton(self.frame)
        self.button_pow.setObjectName(u"button_pow")
        sizePolicy.setHeightForWidth(self.button_pow.sizePolicy().hasHeightForWidth())
        self.button_pow.setSizePolicy(sizePolicy)
        self.button_pow.setMinimumSize(QSize(60, 60))
        self.button_pow.setMaximumSize(QSize(60, 60))
        self.button_pow.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_pow, 3, 12, 1, 1)

        self.button_ln = QPushButton(self.frame)
        self.button_ln.setObjectName(u"button_ln")
        sizePolicy.setHeightForWidth(self.button_ln.sizePolicy().hasHeightForWidth())
        self.button_ln.setSizePolicy(sizePolicy)
        self.button_ln.setMinimumSize(QSize(60, 60))
        self.button_ln.setMaximumSize(QSize(60, 60))
        self.button_ln.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_ln, 2, 4, 1, 1)

        self.button_sin = QPushButton(self.frame)
        self.button_sin.setObjectName(u"button_sin")
        sizePolicy.setHeightForWidth(self.button_sin.sizePolicy().hasHeightForWidth())
        self.button_sin.setSizePolicy(sizePolicy)
        self.button_sin.setMinimumSize(QSize(60, 60))
        self.button_sin.setMaximumSize(QSize(60, 60))
        self.button_sin.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_sin, 0, 3, 1, 1)

        self.button_9 = QPushButton(self.frame)
        self.button_9.setObjectName(u"button_9")
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QSize(60, 60))
        self.button_9.setMaximumSize(QSize(60, 60))
        self.button_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_9, 2, 8, 1, 1)

        self.button_left_bracket = QPushButton(self.frame)
        self.button_left_bracket.setObjectName(u"button_left_bracket")
        sizePolicy.setHeightForWidth(self.button_left_bracket.sizePolicy().hasHeightForWidth())
        self.button_left_bracket.setSizePolicy(sizePolicy)
        self.button_left_bracket.setMinimumSize(QSize(60, 60))
        self.button_left_bracket.setMaximumSize(QSize(60, 60))
        self.button_left_bracket.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_left_bracket, 2, 11, 1, 1)

        self.button_8 = QPushButton(self.frame)
        self.button_8.setObjectName(u"button_8")
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QSize(60, 60))
        self.button_8.setMaximumSize(QSize(60, 60))
        self.button_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_8, 2, 7, 1, 1)

        self.button_cos = QPushButton(self.frame)
        self.button_cos.setObjectName(u"button_cos")
        sizePolicy.setHeightForWidth(self.button_cos.sizePolicy().hasHeightForWidth())
        self.button_cos.setSizePolicy(sizePolicy)
        self.button_cos.setMinimumSize(QSize(60, 60))
        self.button_cos.setMaximumSize(QSize(60, 60))
        self.button_cos.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_cos, 0, 4, 1, 1)

        self.button_tan = QPushButton(self.frame)
        self.button_tan.setObjectName(u"button_tan")
        sizePolicy.setHeightForWidth(self.button_tan.sizePolicy().hasHeightForWidth())
        self.button_tan.setSizePolicy(sizePolicy)
        self.button_tan.setMinimumSize(QSize(60, 60))
        self.button_tan.setMaximumSize(QSize(60, 60))
        self.button_tan.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_tan, 0, 5, 1, 1)

        self.button_minus = QPushButton(self.frame)
        self.button_minus.setObjectName(u"button_minus")
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setMinimumSize(QSize(60, 60))
        self.button_minus.setMaximumSize(QSize(60, 60))
        self.button_minus.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_minus, 1, 10, 1, 1)

        self.button_c = QPushButton(self.frame)
        self.button_c.setObjectName(u"button_c")
        sizePolicy.setHeightForWidth(self.button_c.sizePolicy().hasHeightForWidth())
        self.button_c.setSizePolicy(sizePolicy)
        self.button_c.setMinimumSize(QSize(60, 60))
        self.button_c.setMaximumSize(QSize(60, 60))
        self.button_c.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_c, 1, 11, 1, 1)

        self.button_acos = QPushButton(self.frame)
        self.button_acos.setObjectName(u"button_acos")
        sizePolicy.setHeightForWidth(self.button_acos.sizePolicy().hasHeightForWidth())
        self.button_acos.setSizePolicy(sizePolicy)
        self.button_acos.setMinimumSize(QSize(60, 60))
        self.button_acos.setMaximumSize(QSize(60, 60))
        self.button_acos.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_acos, 1, 4, 1, 1)

        self.button_7 = QPushButton(self.frame)
        self.button_7.setObjectName(u"button_7")
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QSize(60, 60))
        self.button_7.setMaximumSize(QSize(60, 60))
        self.button_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_7, 2, 6, 1, 1)

        self.button_sqrt = QPushButton(self.frame)
        self.button_sqrt.setObjectName(u"button_sqrt")
        sizePolicy.setHeightForWidth(self.button_sqrt.sizePolicy().hasHeightForWidth())
        self.button_sqrt.setSizePolicy(sizePolicy)
        self.button_sqrt.setMinimumSize(QSize(60, 60))
        self.button_sqrt.setMaximumSize(QSize(60, 60))
        self.button_sqrt.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_sqrt, 2, 3, 1, 1)

        self.button_dot = QPushButton(self.frame)
        self.button_dot.setObjectName(u"button_dot")
        sizePolicy.setHeightForWidth(self.button_dot.sizePolicy().hasHeightForWidth())
        self.button_dot.setSizePolicy(sizePolicy)
        self.button_dot.setMinimumSize(QSize(60, 60))
        self.button_dot.setMaximumSize(QSize(60, 60))
        self.button_dot.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_dot, 3, 8, 1, 1)

        self.button_mod = QPushButton(self.frame)
        self.button_mod.setObjectName(u"button_mod")
        sizePolicy.setHeightForWidth(self.button_mod.sizePolicy().hasHeightForWidth())
        self.button_mod.setSizePolicy(sizePolicy)
        self.button_mod.setMinimumSize(QSize(60, 60))
        self.button_mod.setMaximumSize(QSize(60, 60))
        self.button_mod.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_mod, 3, 11, 1, 1)

        self.button_5 = QPushButton(self.frame)
        self.button_5.setObjectName(u"button_5")
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QSize(60, 60))
        self.button_5.setMaximumSize(QSize(60, 60))
        self.button_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_5, 1, 7, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 605, 31))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.button_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_asin.setText(QCoreApplication.translate("MainWindow", u"asin", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_rigth_bracket.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.button_atan.setText(QCoreApplication.translate("MainWindow", u"atan", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_ac.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.button_mult.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.button_00.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_pow.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.button_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.button_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_left_bracket.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.button_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.button_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_acos.setText(QCoreApplication.translate("MainWindow", u"acos", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_sqrt.setText(QCoreApplication.translate("MainWindow", u"sqrt", None))
        self.button_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.button_mod.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

