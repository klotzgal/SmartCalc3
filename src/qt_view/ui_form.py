# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(600, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View.sizePolicy().hasHeightForWidth())
        View.setSizePolicy(sizePolicy)
        View.setMinimumSize(QSize(600, 500))
        View.setMaximumSize(QSize(687, 500))
        View.setStyleSheet(u"* {\n"
"	background-color: #1c1c1e; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439, \u0431\u043b\u0438\u0436\u0435 \u043a \u0447\u0435\u0440\u043d\u043e\u043c\u0443 */\n"
"	color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	font-family: 'Open Sans';\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #445566; /* \u0413\u043b\u0443\u0431\u043e\u043a\u0438\u0439 \u0441\u0438\u043d\u0435-\u0441\u0435\u0440\u044b\u0439 */\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
""
                        "    border-style: inset;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #2a3b4c; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"#button_0, #button_1, #button_2, #button_3, #button_4, \n"
"#button_5, #button_6, #button_7, #button_8, #button_9 {\n"
"    background-color: #556b2f; /* \u0422\u0435\u043c\u043d\u043e-\u043e\u043b\u0438\u0432\u043a\u043e\u0432\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 */\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #dcdcdc; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435"
                        "\u0440\u044b\u0439 */\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"#button_0:hover, #button_1:hover, #button_2:hover, #button_3:hover, #button_4:hover, #button_5:hover, #button_6:hover, #button_7:hover, #button_8:hover, #button_9:hover {\n"
"    background-color: #6b8e23; /* \u0411\u043e\u043b\u0435\u0435 \u044f\u0440\u043a\u0438\u0439 \u043e\u043b\u0438\u0432\u043a\u043e\u0432\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border-style: inset;\n"
"}\n"
"\n"
"#button_0:pressed, #button_1:pressed, #button_2:pressed, #button_3:pressed, #button_4:pressed, #button_5:pressed, #button_6:pressed, #button_7:pressed, #button_8:pressed, #button_9:pressed {\n"
"    background-color: #3b4b1e; /* \u0422\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-style: inset;\n"
"}\n"
"")
        self.centralwidget = QWidget(View)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_c = QPushButton(self.frame)
        self.button_c.setObjectName(u"button_c")
        sizePolicy.setHeightForWidth(self.button_c.sizePolicy().hasHeightForWidth())
        self.button_c.setSizePolicy(sizePolicy)
        self.button_c.setMinimumSize(QSize(60, 60))
        self.button_c.setMaximumSize(QSize(60, 60))
        self.button_c.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_c, 1, 8, 1, 1)

        self.button_3 = QPushButton(self.frame)
        self.input_buttons = QButtonGroup(View)
        self.input_buttons.setObjectName(u"input_buttons")
        self.input_buttons.addButton(self.button_3)
        self.button_3.setObjectName(u"button_3")
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QSize(60, 60))
        self.button_3.setMaximumSize(QSize(60, 60))
        self.button_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_3, 0, 6, 1, 1)

        self.button_8 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_8)
        self.button_8.setObjectName(u"button_8")
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QSize(60, 60))
        self.button_8.setMaximumSize(QSize(60, 60))
        self.button_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_8, 2, 5, 1, 1)

        self.button_2 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_2)
        self.button_2.setObjectName(u"button_2")
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QSize(60, 60))
        self.button_2.setMaximumSize(QSize(60, 60))
        self.button_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_2, 0, 5, 1, 1)

        self.button_7 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_7)
        self.button_7.setObjectName(u"button_7")
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QSize(60, 60))
        self.button_7.setMaximumSize(QSize(60, 60))
        self.button_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_7, 2, 4, 1, 1)

        self.button_6 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_6)
        self.button_6.setObjectName(u"button_6")
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QSize(60, 60))
        self.button_6.setMaximumSize(QSize(60, 60))
        self.button_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_6, 1, 6, 1, 1)

        self.button_log = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_log)
        self.button_log.setObjectName(u"button_log")
        sizePolicy.setHeightForWidth(self.button_log.sizePolicy().hasHeightForWidth())
        self.button_log.setSizePolicy(sizePolicy)
        self.button_log.setMinimumSize(QSize(60, 60))
        self.button_log.setMaximumSize(QSize(60, 60))
        self.button_log.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_log, 2, 3, 1, 1)

        self.button_left_bracket = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_left_bracket)
        self.button_left_bracket.setObjectName(u"button_left_bracket")
        sizePolicy.setHeightForWidth(self.button_left_bracket.sizePolicy().hasHeightForWidth())
        self.button_left_bracket.setSizePolicy(sizePolicy)
        self.button_left_bracket.setMinimumSize(QSize(60, 60))
        self.button_left_bracket.setMaximumSize(QSize(60, 60))
        self.button_left_bracket.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_left_bracket, 2, 8, 1, 1)

        self.button_5 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_5)
        self.button_5.setObjectName(u"button_5")
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QSize(60, 60))
        self.button_5.setMaximumSize(QSize(60, 60))
        self.button_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_5, 1, 5, 1, 1)

        self.button_9 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_9)
        self.button_9.setObjectName(u"button_9")
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QSize(60, 60))
        self.button_9.setMaximumSize(QSize(60, 60))
        self.button_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_9, 2, 6, 1, 1)

        self.button_tan = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_tan)
        self.button_tan.setObjectName(u"button_tan")
        sizePolicy.setHeightForWidth(self.button_tan.sizePolicy().hasHeightForWidth())
        self.button_tan.setSizePolicy(sizePolicy)
        self.button_tan.setMinimumSize(QSize(60, 60))
        self.button_tan.setMaximumSize(QSize(60, 60))
        self.button_tan.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_tan, 0, 3, 1, 1)

        self.button_acos = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_acos)
        self.button_acos.setObjectName(u"button_acos")
        sizePolicy.setHeightForWidth(self.button_acos.sizePolicy().hasHeightForWidth())
        self.button_acos.setSizePolicy(sizePolicy)
        self.button_acos.setMinimumSize(QSize(60, 60))
        self.button_acos.setMaximumSize(QSize(60, 60))
        self.button_acos.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_acos, 1, 1, 1, 1)

        self.button_sqrt = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_sqrt)
        self.button_sqrt.setObjectName(u"button_sqrt")
        sizePolicy.setHeightForWidth(self.button_sqrt.sizePolicy().hasHeightForWidth())
        self.button_sqrt.setSizePolicy(sizePolicy)
        self.button_sqrt.setMinimumSize(QSize(60, 60))
        self.button_sqrt.setMaximumSize(QSize(60, 60))
        self.button_sqrt.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_sqrt, 2, 0, 1, 1)

        self.button_4 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_4)
        self.button_4.setObjectName(u"button_4")
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QSize(60, 60))
        self.button_4.setMaximumSize(QSize(60, 60))
        self.button_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_4, 1, 4, 1, 1)

        self.button_mult = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_mult)
        self.button_mult.setObjectName(u"button_mult")
        sizePolicy.setHeightForWidth(self.button_mult.sizePolicy().hasHeightForWidth())
        self.button_mult.setSizePolicy(sizePolicy)
        self.button_mult.setMinimumSize(QSize(60, 60))
        self.button_mult.setMaximumSize(QSize(60, 60))
        self.button_mult.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_mult, 2, 7, 1, 1)

        self.button_equal = QPushButton(self.frame)
        self.button_equal.setObjectName(u"button_equal")
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        self.button_equal.setMinimumSize(QSize(123, 60))
        self.button_equal.setMaximumSize(QSize(123, 60))
        self.button_equal.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_equal, 0, 8, 1, 2)

        self.button_asin = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_asin)
        self.button_asin.setObjectName(u"button_asin")
        sizePolicy.setHeightForWidth(self.button_asin.sizePolicy().hasHeightForWidth())
        self.button_asin.setSizePolicy(sizePolicy)
        self.button_asin.setMinimumSize(QSize(60, 60))
        self.button_asin.setMaximumSize(QSize(60, 60))
        self.button_asin.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_asin, 1, 0, 1, 1)

        self.button_ln = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_ln)
        self.button_ln.setObjectName(u"button_ln")
        sizePolicy.setHeightForWidth(self.button_ln.sizePolicy().hasHeightForWidth())
        self.button_ln.setSizePolicy(sizePolicy)
        self.button_ln.setMinimumSize(QSize(60, 60))
        self.button_ln.setMaximumSize(QSize(60, 60))
        self.button_ln.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_ln, 2, 1, 1, 1)

        self.button_sin = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_sin)
        self.button_sin.setObjectName(u"button_sin")
        sizePolicy.setHeightForWidth(self.button_sin.sizePolicy().hasHeightForWidth())
        self.button_sin.setSizePolicy(sizePolicy)
        self.button_sin.setMinimumSize(QSize(60, 60))
        self.button_sin.setMaximumSize(QSize(60, 60))
        self.button_sin.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_sin, 0, 0, 1, 1)

        self.button_ac = QPushButton(self.frame)
        self.button_ac.setObjectName(u"button_ac")
        sizePolicy.setHeightForWidth(self.button_ac.sizePolicy().hasHeightForWidth())
        self.button_ac.setSizePolicy(sizePolicy)
        self.button_ac.setMinimumSize(QSize(60, 60))
        self.button_ac.setMaximumSize(QSize(60, 60))
        self.button_ac.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_ac, 1, 9, 1, 1)

        self.button_atan = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_atan)
        self.button_atan.setObjectName(u"button_atan")
        sizePolicy.setHeightForWidth(self.button_atan.sizePolicy().hasHeightForWidth())
        self.button_atan.setSizePolicy(sizePolicy)
        self.button_atan.setMinimumSize(QSize(60, 60))
        self.button_atan.setMaximumSize(QSize(60, 60))
        self.button_atan.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_atan, 1, 3, 1, 1)

        self.button_1 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_1)
        self.button_1.setObjectName(u"button_1")
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QSize(60, 60))
        self.button_1.setMaximumSize(QSize(60, 60))
        self.button_1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_1, 0, 4, 1, 1)

        self.button_rigth_bracket = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_rigth_bracket)
        self.button_rigth_bracket.setObjectName(u"button_rigth_bracket")
        sizePolicy.setHeightForWidth(self.button_rigth_bracket.sizePolicy().hasHeightForWidth())
        self.button_rigth_bracket.setSizePolicy(sizePolicy)
        self.button_rigth_bracket.setMinimumSize(QSize(60, 60))
        self.button_rigth_bracket.setMaximumSize(QSize(60, 60))
        self.button_rigth_bracket.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_rigth_bracket, 2, 9, 1, 1)

        self.button_plus = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_plus)
        self.button_plus.setObjectName(u"button_plus")
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setMinimumSize(QSize(60, 60))
        self.button_plus.setMaximumSize(QSize(60, 60))
        self.button_plus.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_plus, 0, 7, 1, 1)

        self.button_cos = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_cos)
        self.button_cos.setObjectName(u"button_cos")
        sizePolicy.setHeightForWidth(self.button_cos.sizePolicy().hasHeightForWidth())
        self.button_cos.setSizePolicy(sizePolicy)
        self.button_cos.setMinimumSize(QSize(60, 60))
        self.button_cos.setMaximumSize(QSize(60, 60))
        self.button_cos.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_cos, 0, 1, 1, 1)

        self.button_minus = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_minus)
        self.button_minus.setObjectName(u"button_minus")
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setMinimumSize(QSize(60, 60))
        self.button_minus.setMaximumSize(QSize(60, 60))
        self.button_minus.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_minus, 1, 7, 1, 1)

        self.button_x = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_x)
        self.button_x.setObjectName(u"button_x")
        sizePolicy.setHeightForWidth(self.button_x.sizePolicy().hasHeightForWidth())
        self.button_x.setSizePolicy(sizePolicy)
        self.button_x.setMinimumSize(QSize(60, 60))
        self.button_x.setMaximumSize(QSize(60, 60))
        self.button_x.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_x, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(123, 60))
        self.lineEdit.setMaximumSize(QSize(123, 60))
        self.lineEdit.setSizeIncrement(QSize(123, 0))
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.button_00 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_00)
        self.button_00.setObjectName(u"button_00")
        sizePolicy.setHeightForWidth(self.button_00.sizePolicy().hasHeightForWidth())
        self.button_00.setSizePolicy(sizePolicy)
        self.button_00.setMinimumSize(QSize(60, 60))
        self.button_00.setMaximumSize(QSize(60, 60))
        self.button_00.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_00, 3, 4, 1, 1)

        self.button_0 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_0)
        self.button_0.setObjectName(u"button_0")
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setMinimumSize(QSize(60, 60))
        self.button_0.setMaximumSize(QSize(60, 60))
        self.button_0.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_0, 3, 5, 1, 1)

        self.button_dot = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_dot)
        self.button_dot.setObjectName(u"button_dot")
        sizePolicy.setHeightForWidth(self.button_dot.sizePolicy().hasHeightForWidth())
        self.button_dot.setSizePolicy(sizePolicy)
        self.button_dot.setMinimumSize(QSize(60, 60))
        self.button_dot.setMaximumSize(QSize(60, 60))
        self.button_dot.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_dot, 3, 6, 1, 1)

        self.button_div = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_div)
        self.button_div.setObjectName(u"button_div")
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        self.button_div.setMinimumSize(QSize(60, 60))
        self.button_div.setMaximumSize(QSize(60, 60))
        self.button_div.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_div, 3, 7, 1, 1)

        self.button_mod = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_mod)
        self.button_mod.setObjectName(u"button_mod")
        sizePolicy.setHeightForWidth(self.button_mod.sizePolicy().hasHeightForWidth())
        self.button_mod.setSizePolicy(sizePolicy)
        self.button_mod.setMinimumSize(QSize(60, 60))
        self.button_mod.setMaximumSize(QSize(60, 60))
        self.button_mod.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_mod, 3, 8, 1, 1)

        self.button_pow = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_pow)
        self.button_pow.setObjectName(u"button_pow")
        sizePolicy.setHeightForWidth(self.button_pow.sizePolicy().hasHeightForWidth())
        self.button_pow.setSizePolicy(sizePolicy)
        self.button_pow.setMinimumSize(QSize(60, 60))
        self.button_pow.setMaximumSize(QSize(60, 60))
        self.button_pow.setStyleSheet(u"")

        self.gridLayout.addWidget(self.button_pow, 3, 9, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        View.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(View)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 31))
        View.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(View)
        self.statusbar.setObjectName(u"statusbar")
        View.setStatusBar(self.statusbar)

        self.retranslateUi(View)

        QMetaObject.connectSlotsByName(View)
    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate("View", u"View", None))
        self.input.setText(QCoreApplication.translate("View", u"0", None))
        self.button_c.setText(QCoreApplication.translate("View", u"C", None))
        self.button_3.setText(QCoreApplication.translate("View", u"3", None))
        self.button_8.setText(QCoreApplication.translate("View", u"8", None))
        self.button_2.setText(QCoreApplication.translate("View", u"2", None))
        self.button_7.setText(QCoreApplication.translate("View", u"7", None))
        self.button_6.setText(QCoreApplication.translate("View", u"6", None))
        self.button_log.setText(QCoreApplication.translate("View", u"log", None))
        self.button_left_bracket.setText(QCoreApplication.translate("View", u"(", None))
        self.button_5.setText(QCoreApplication.translate("View", u"5", None))
        self.button_9.setText(QCoreApplication.translate("View", u"9", None))
        self.button_tan.setText(QCoreApplication.translate("View", u"tan", None))
        self.button_acos.setText(QCoreApplication.translate("View", u"acos", None))
        self.button_sqrt.setText(QCoreApplication.translate("View", u"sqrt", None))
        self.button_4.setText(QCoreApplication.translate("View", u"4", None))
        self.button_mult.setText(QCoreApplication.translate("View", u"*", None))
        self.button_equal.setText(QCoreApplication.translate("View", u"=", None))
        self.button_asin.setText(QCoreApplication.translate("View", u"asin", None))
        self.button_ln.setText(QCoreApplication.translate("View", u"ln", None))
        self.button_sin.setText(QCoreApplication.translate("View", u"sin", None))
        self.button_ac.setText(QCoreApplication.translate("View", u"AC", None))
        self.button_atan.setText(QCoreApplication.translate("View", u"atan", None))
        self.button_1.setText(QCoreApplication.translate("View", u"1", None))
        self.button_rigth_bracket.setText(QCoreApplication.translate("View", u")", None))
        self.button_plus.setText(QCoreApplication.translate("View", u"+", None))
        self.button_cos.setText(QCoreApplication.translate("View", u"cos", None))
        self.button_minus.setText(QCoreApplication.translate("View", u"-", None))
        self.button_x.setText(QCoreApplication.translate("View", u"x", None))
        self.lineEdit.setText(QCoreApplication.translate("View", u"0", None))
        self.button_00.setText(QCoreApplication.translate("View", u"00", None))
        self.button_0.setText(QCoreApplication.translate("View", u"0", None))
        self.button_dot.setText(QCoreApplication.translate("View", u".", None))
        self.button_div.setText(QCoreApplication.translate("View", u"/", None))
        self.button_mod.setText(QCoreApplication.translate("View", u"%", None))
        self.button_pow.setText(QCoreApplication.translate("View", u"^", None))
    # retranslateUi

