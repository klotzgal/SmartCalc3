# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName('View')
        View.resize(600, 555)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View.sizePolicy().hasHeightForWidth())
        View.setSizePolicy(sizePolicy)
        View.setMinimumSize(QSize(600, 555))
        View.setMaximumSize(QSize(600, 555))
        View.setStyleSheet(
            '* {\n'
            '	background-color: #1c1c1e; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439, \u0431\u043b\u0438\u0436\u0435 \u043a \u0447\u0435\u0440\u043d\u043e\u043c\u0443 */\n'
            '	color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n'
            "	font-family: 'Open Sans';\n"
            '	font: bold 14px;\n'
            '}\n'
            '\n'
            'QPushButton {\n'
            '	background-color: #445566; /* \u0413\u043b\u0443\u0431\u043e\u043a\u0438\u0439 \u0441\u0438\u043d\u0435-\u0441\u0435\u0440\u044b\u0439 */\n'
            '    border-style: outset;\n'
            '    border-width: 2px;\n'
            '    border-radius: 10px;\n'
            '    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
            '    font: bold 14px;\n'
            '    padding: 6px;\n'
            '}\n'
            'QPushButton:hover {\n'
            '	background-color: #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d'
            '\u0438\u0438 */\n'
            '    border-style: inset;\n'
            '}\n'
            'QPushButton:pressed {\n'
            '	background-color: #2a3b4c; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n'
            '    border-style: inset;\n'
            '}\n'
            '\n'
            'QLineEdit{\n'
            '	border-style: outset;\n'
            '    border-width: 2px;\n'
            '    border-radius: 10px;\n'
            '    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
            '    padding: 6px;\n'
            '}\n'
            '\n'
            '#button_0, #button_1, #button_2, #button_3, #button_4, \n'
            '#button_5, #button_6, #button_7, #button_8, #button_9 {\n'
            '    background-color: #556b2f; /* \u0422\u0435\u043c\u043d\u043e-\u043e\u043b\u0438\u0432\u043a\u043e\u0432\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 */\n'
            '    border-style: outset;\n'
            '    border-width: 2px;\n'
            '    border-radius: 10px;\n'
            '    border-color: #dcdcdc; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440'
            '\u044b\u0439 */\n'
            '    font: bold 14px;\n'
            '    padding: 6px;\n'
            '}\n'
            '\n'
            '#button_0:hover, #button_1:hover, #button_2:hover, #button_3:hover, #button_4:hover, #button_5:hover, #button_6:hover, #button_7:hover, #button_8:hover, #button_9:hover {\n'
            '    background-color: #6b8e23; /* \u0411\u043e\u043b\u0435\u0435 \u044f\u0440\u043a\u0438\u0439 \u043e\u043b\u0438\u0432\u043a\u043e\u0432\u044b\u0439 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n'
            '    border-style: inset;\n'
            '}\n'
            '\n'
            '#button_0:pressed, #button_1:pressed, #button_2:pressed, #button_3:pressed, #button_4:pressed, #button_5:pressed, #button_6:pressed, #button_7:pressed, #button_8:pressed, #button_9:pressed {\n'
            '    background-color: #3b4b1e; /* \u0422\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n'
            '    border-style: inset;\n'
            '}\n'
            ''
        )
        self.centralwidget = QWidget(View)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.input = QLineEdit(self.centralwidget)
        self.input.setObjectName('input')
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy1)
        self.input.setMinimumSize(QSize(500, 50))
        self.input.setMaximumSize(QSize(16777215, 50))
        self.input.setStyleSheet('')
        self.input.setMaxLength(255)
        self.input.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.input)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName('frame_3')
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.history_prev = QPushButton(self.frame_3)
        self.history_prev.setObjectName('history_prev')
        sizePolicy.setHeightForWidth(self.history_prev.sizePolicy().hasHeightForWidth())
        self.history_prev.setSizePolicy(sizePolicy)
        self.history_prev.setMinimumSize(QSize(60, 60))
        self.history_prev.setMaximumSize(QSize(60, 60))
        self.history_prev.setStyleSheet('')

        self.horizontalLayout_2.addWidget(self.history_prev)

        self.history_next = QPushButton(self.frame_3)
        self.history_next.setObjectName('history_next')
        sizePolicy.setHeightForWidth(self.history_next.sizePolicy().hasHeightForWidth())
        self.history_next.setSizePolicy(sizePolicy)
        self.history_next.setMinimumSize(QSize(60, 60))
        self.history_next.setMaximumSize(QSize(60, 60))
        self.history_next.setStyleSheet('')

        self.horizontalLayout_2.addWidget(self.history_next)

        self.history_clear = QPushButton(self.frame_3)
        self.history_clear.setObjectName('history_clear')
        sizePolicy.setHeightForWidth(
            self.history_clear.sizePolicy().hasHeightForWidth()
        )
        self.history_clear.setSizePolicy(sizePolicy)
        self.history_clear.setMinimumSize(QSize(60, 60))
        self.history_clear.setMaximumSize(QSize(60, 60))
        self.history_clear.setStyleSheet('')

        self.horizontalLayout_2.addWidget(self.history_clear)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName('label')
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName('frame')
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet('')
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName('gridLayout')
        self.button_c = QPushButton(self.frame)
        self.button_c.setObjectName('button_c')
        sizePolicy.setHeightForWidth(self.button_c.sizePolicy().hasHeightForWidth())
        self.button_c.setSizePolicy(sizePolicy)
        self.button_c.setMinimumSize(QSize(60, 60))
        self.button_c.setMaximumSize(QSize(60, 60))
        self.button_c.setStyleSheet('')

        self.gridLayout.addWidget(self.button_c, 1, 8, 1, 1)

        self.button_3 = QPushButton(self.frame)
        self.input_buttons = QButtonGroup(View)
        self.input_buttons.setObjectName('input_buttons')
        self.input_buttons.addButton(self.button_3)
        self.button_3.setObjectName('button_3')
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QSize(60, 60))
        self.button_3.setMaximumSize(QSize(60, 60))
        self.button_3.setStyleSheet('')

        self.gridLayout.addWidget(self.button_3, 0, 6, 1, 1)

        self.button_8 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_8)
        self.button_8.setObjectName('button_8')
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QSize(60, 60))
        self.button_8.setMaximumSize(QSize(60, 60))
        self.button_8.setStyleSheet('')

        self.gridLayout.addWidget(self.button_8, 2, 5, 1, 1)

        self.button_2 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_2)
        self.button_2.setObjectName('button_2')
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QSize(60, 60))
        self.button_2.setMaximumSize(QSize(60, 60))
        self.button_2.setStyleSheet('')

        self.gridLayout.addWidget(self.button_2, 0, 5, 1, 1)

        self.button_7 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_7)
        self.button_7.setObjectName('button_7')
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QSize(60, 60))
        self.button_7.setMaximumSize(QSize(60, 60))
        self.button_7.setStyleSheet('')

        self.gridLayout.addWidget(self.button_7, 2, 4, 1, 1)

        self.button_6 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_6)
        self.button_6.setObjectName('button_6')
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QSize(60, 60))
        self.button_6.setMaximumSize(QSize(60, 60))
        self.button_6.setStyleSheet('')

        self.gridLayout.addWidget(self.button_6, 1, 6, 1, 1)

        self.button_log = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_log)
        self.button_log.setObjectName('button_log')
        sizePolicy.setHeightForWidth(self.button_log.sizePolicy().hasHeightForWidth())
        self.button_log.setSizePolicy(sizePolicy)
        self.button_log.setMinimumSize(QSize(60, 60))
        self.button_log.setMaximumSize(QSize(60, 60))
        self.button_log.setStyleSheet('')

        self.gridLayout.addWidget(self.button_log, 2, 3, 1, 1)

        self.button_left_bracket = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_left_bracket)
        self.button_left_bracket.setObjectName('button_left_bracket')
        sizePolicy.setHeightForWidth(
            self.button_left_bracket.sizePolicy().hasHeightForWidth()
        )
        self.button_left_bracket.setSizePolicy(sizePolicy)
        self.button_left_bracket.setMinimumSize(QSize(60, 60))
        self.button_left_bracket.setMaximumSize(QSize(60, 60))
        self.button_left_bracket.setStyleSheet('')

        self.gridLayout.addWidget(self.button_left_bracket, 2, 8, 1, 1)

        self.button_5 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_5)
        self.button_5.setObjectName('button_5')
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QSize(60, 60))
        self.button_5.setMaximumSize(QSize(60, 60))
        self.button_5.setStyleSheet('')

        self.gridLayout.addWidget(self.button_5, 1, 5, 1, 1)

        self.button_9 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_9)
        self.button_9.setObjectName('button_9')
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QSize(60, 60))
        self.button_9.setMaximumSize(QSize(60, 60))
        self.button_9.setStyleSheet('')

        self.gridLayout.addWidget(self.button_9, 2, 6, 1, 1)

        self.button_tan = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_tan)
        self.button_tan.setObjectName('button_tan')
        sizePolicy.setHeightForWidth(self.button_tan.sizePolicy().hasHeightForWidth())
        self.button_tan.setSizePolicy(sizePolicy)
        self.button_tan.setMinimumSize(QSize(60, 60))
        self.button_tan.setMaximumSize(QSize(60, 60))
        self.button_tan.setStyleSheet('')

        self.gridLayout.addWidget(self.button_tan, 0, 3, 1, 1)

        self.button_acos = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_acos)
        self.button_acos.setObjectName('button_acos')
        sizePolicy.setHeightForWidth(self.button_acos.sizePolicy().hasHeightForWidth())
        self.button_acos.setSizePolicy(sizePolicy)
        self.button_acos.setMinimumSize(QSize(60, 60))
        self.button_acos.setMaximumSize(QSize(60, 60))
        self.button_acos.setStyleSheet('')

        self.gridLayout.addWidget(self.button_acos, 1, 1, 1, 1)

        self.button_sqrt = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_sqrt)
        self.button_sqrt.setObjectName('button_sqrt')
        sizePolicy.setHeightForWidth(self.button_sqrt.sizePolicy().hasHeightForWidth())
        self.button_sqrt.setSizePolicy(sizePolicy)
        self.button_sqrt.setMinimumSize(QSize(60, 60))
        self.button_sqrt.setMaximumSize(QSize(60, 60))
        self.button_sqrt.setStyleSheet('')

        self.gridLayout.addWidget(self.button_sqrt, 2, 0, 1, 1)

        self.button_4 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_4)
        self.button_4.setObjectName('button_4')
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QSize(60, 60))
        self.button_4.setMaximumSize(QSize(60, 60))
        self.button_4.setStyleSheet('')

        self.gridLayout.addWidget(self.button_4, 1, 4, 1, 1)

        self.button_mult = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_mult)
        self.button_mult.setObjectName('button_mult')
        sizePolicy.setHeightForWidth(self.button_mult.sizePolicy().hasHeightForWidth())
        self.button_mult.setSizePolicy(sizePolicy)
        self.button_mult.setMinimumSize(QSize(60, 60))
        self.button_mult.setMaximumSize(QSize(60, 60))
        self.button_mult.setStyleSheet('')

        self.gridLayout.addWidget(self.button_mult, 2, 7, 1, 1)

        self.button_equal = QPushButton(self.frame)
        self.button_equal.setObjectName('button_equal')
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        self.button_equal.setMinimumSize(QSize(123, 60))
        self.button_equal.setMaximumSize(QSize(123, 60))
        self.button_equal.setStyleSheet('')

        self.gridLayout.addWidget(self.button_equal, 0, 8, 1, 2)

        self.button_asin = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_asin)
        self.button_asin.setObjectName('button_asin')
        sizePolicy.setHeightForWidth(self.button_asin.sizePolicy().hasHeightForWidth())
        self.button_asin.setSizePolicy(sizePolicy)
        self.button_asin.setMinimumSize(QSize(60, 60))
        self.button_asin.setMaximumSize(QSize(60, 60))
        self.button_asin.setStyleSheet('')

        self.gridLayout.addWidget(self.button_asin, 1, 0, 1, 1)

        self.button_ln = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_ln)
        self.button_ln.setObjectName('button_ln')
        sizePolicy.setHeightForWidth(self.button_ln.sizePolicy().hasHeightForWidth())
        self.button_ln.setSizePolicy(sizePolicy)
        self.button_ln.setMinimumSize(QSize(60, 60))
        self.button_ln.setMaximumSize(QSize(60, 60))
        self.button_ln.setStyleSheet('')

        self.gridLayout.addWidget(self.button_ln, 2, 1, 1, 1)

        self.button_sin = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_sin)
        self.button_sin.setObjectName('button_sin')
        sizePolicy.setHeightForWidth(self.button_sin.sizePolicy().hasHeightForWidth())
        self.button_sin.setSizePolicy(sizePolicy)
        self.button_sin.setMinimumSize(QSize(60, 60))
        self.button_sin.setMaximumSize(QSize(60, 60))
        self.button_sin.setStyleSheet('')

        self.gridLayout.addWidget(self.button_sin, 0, 0, 1, 1)

        self.button_ac = QPushButton(self.frame)
        self.button_ac.setObjectName('button_ac')
        sizePolicy.setHeightForWidth(self.button_ac.sizePolicy().hasHeightForWidth())
        self.button_ac.setSizePolicy(sizePolicy)
        self.button_ac.setMinimumSize(QSize(60, 60))
        self.button_ac.setMaximumSize(QSize(60, 60))
        self.button_ac.setStyleSheet('')

        self.gridLayout.addWidget(self.button_ac, 1, 9, 1, 1)

        self.button_atan = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_atan)
        self.button_atan.setObjectName('button_atan')
        sizePolicy.setHeightForWidth(self.button_atan.sizePolicy().hasHeightForWidth())
        self.button_atan.setSizePolicy(sizePolicy)
        self.button_atan.setMinimumSize(QSize(60, 60))
        self.button_atan.setMaximumSize(QSize(60, 60))
        self.button_atan.setStyleSheet('')

        self.gridLayout.addWidget(self.button_atan, 1, 3, 1, 1)

        self.button_1 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_1)
        self.button_1.setObjectName('button_1')
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QSize(60, 60))
        self.button_1.setMaximumSize(QSize(60, 60))
        self.button_1.setStyleSheet('')

        self.gridLayout.addWidget(self.button_1, 0, 4, 1, 1)

        self.button_rigth_bracket = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_rigth_bracket)
        self.button_rigth_bracket.setObjectName('button_rigth_bracket')
        sizePolicy.setHeightForWidth(
            self.button_rigth_bracket.sizePolicy().hasHeightForWidth()
        )
        self.button_rigth_bracket.setSizePolicy(sizePolicy)
        self.button_rigth_bracket.setMinimumSize(QSize(60, 60))
        self.button_rigth_bracket.setMaximumSize(QSize(60, 60))
        self.button_rigth_bracket.setStyleSheet('')

        self.gridLayout.addWidget(self.button_rigth_bracket, 2, 9, 1, 1)

        self.button_plus = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_plus)
        self.button_plus.setObjectName('button_plus')
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setMinimumSize(QSize(60, 60))
        self.button_plus.setMaximumSize(QSize(60, 60))
        self.button_plus.setStyleSheet('')

        self.gridLayout.addWidget(self.button_plus, 0, 7, 1, 1)

        self.button_cos = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_cos)
        self.button_cos.setObjectName('button_cos')
        sizePolicy.setHeightForWidth(self.button_cos.sizePolicy().hasHeightForWidth())
        self.button_cos.setSizePolicy(sizePolicy)
        self.button_cos.setMinimumSize(QSize(60, 60))
        self.button_cos.setMaximumSize(QSize(60, 60))
        self.button_cos.setStyleSheet('')

        self.gridLayout.addWidget(self.button_cos, 0, 1, 1, 1)

        self.button_minus = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_minus)
        self.button_minus.setObjectName('button_minus')
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setMinimumSize(QSize(60, 60))
        self.button_minus.setMaximumSize(QSize(60, 60))
        self.button_minus.setStyleSheet('')

        self.gridLayout.addWidget(self.button_minus, 1, 7, 1, 1)

        self.button_x = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_x)
        self.button_x.setObjectName('button_x')
        sizePolicy.setHeightForWidth(self.button_x.sizePolicy().hasHeightForWidth())
        self.button_x.setSizePolicy(sizePolicy)
        self.button_x.setMinimumSize(QSize(60, 60))
        self.button_x.setMaximumSize(QSize(60, 60))
        self.button_x.setStyleSheet('')

        self.gridLayout.addWidget(self.button_x, 3, 0, 1, 1)

        self.input_x = QLineEdit(self.frame)
        self.input_x.setObjectName('input_x')
        self.input_x.setMinimumSize(QSize(123, 60))
        self.input_x.setMaximumSize(QSize(123, 60))
        self.input_x.setSizeIncrement(QSize(123, 0))
        self.input_x.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.input_x, 3, 1, 1, 1)

        self.button_00 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_00)
        self.button_00.setObjectName('button_00')
        sizePolicy.setHeightForWidth(self.button_00.sizePolicy().hasHeightForWidth())
        self.button_00.setSizePolicy(sizePolicy)
        self.button_00.setMinimumSize(QSize(60, 60))
        self.button_00.setMaximumSize(QSize(60, 60))
        self.button_00.setStyleSheet('')

        self.gridLayout.addWidget(self.button_00, 3, 4, 1, 1)

        self.button_0 = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_0)
        self.button_0.setObjectName('button_0')
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setMinimumSize(QSize(60, 60))
        self.button_0.setMaximumSize(QSize(60, 60))
        self.button_0.setStyleSheet('')

        self.gridLayout.addWidget(self.button_0, 3, 5, 1, 1)

        self.button_dot = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_dot)
        self.button_dot.setObjectName('button_dot')
        sizePolicy.setHeightForWidth(self.button_dot.sizePolicy().hasHeightForWidth())
        self.button_dot.setSizePolicy(sizePolicy)
        self.button_dot.setMinimumSize(QSize(60, 60))
        self.button_dot.setMaximumSize(QSize(60, 60))
        self.button_dot.setStyleSheet('')

        self.gridLayout.addWidget(self.button_dot, 3, 6, 1, 1)

        self.button_div = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_div)
        self.button_div.setObjectName('button_div')
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        self.button_div.setMinimumSize(QSize(60, 60))
        self.button_div.setMaximumSize(QSize(60, 60))
        self.button_div.setStyleSheet('')

        self.gridLayout.addWidget(self.button_div, 3, 7, 1, 1)

        self.button_mod = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_mod)
        self.button_mod.setObjectName('button_mod')
        sizePolicy.setHeightForWidth(self.button_mod.sizePolicy().hasHeightForWidth())
        self.button_mod.setSizePolicy(sizePolicy)
        self.button_mod.setMinimumSize(QSize(60, 60))
        self.button_mod.setMaximumSize(QSize(60, 60))
        self.button_mod.setStyleSheet('')

        self.gridLayout.addWidget(self.button_mod, 3, 8, 1, 1)

        self.button_pow = QPushButton(self.frame)
        self.input_buttons.addButton(self.button_pow)
        self.button_pow.setObjectName('button_pow')
        sizePolicy.setHeightForWidth(self.button_pow.sizePolicy().hasHeightForWidth())
        self.button_pow.setSizePolicy(sizePolicy)
        self.button_pow.setMinimumSize(QSize(60, 60))
        self.button_pow.setMaximumSize(QSize(60, 60))
        self.button_pow.setStyleSheet('')

        self.gridLayout.addWidget(self.button_pow, 3, 9, 1, 1)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.button_plot = QPushButton(self.frame_2)
        self.button_plot.setObjectName('button_plot')
        sizePolicy1.setHeightForWidth(self.button_plot.sizePolicy().hasHeightForWidth())
        self.button_plot.setSizePolicy(sizePolicy1)
        self.button_plot.setMinimumSize(QSize(60, 60))
        self.button_plot.setMaximumSize(QSize(9999, 60))
        self.button_plot.setStyleSheet('')

        self.horizontalLayout.addWidget(self.button_plot)

        self.button_credit = QPushButton(self.frame_2)
        self.button_credit.setObjectName('button_credit')
        sizePolicy1.setHeightForWidth(
            self.button_credit.sizePolicy().hasHeightForWidth()
        )
        self.button_credit.setSizePolicy(sizePolicy1)
        self.button_credit.setMinimumSize(QSize(60, 60))
        self.button_credit.setMaximumSize(QSize(9999, 60))
        self.button_credit.setStyleSheet('')

        self.horizontalLayout.addWidget(self.button_credit)

        self.verticalLayout.addWidget(self.frame_2)

        View.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(View)
        self.menubar.setObjectName('menubar')
        self.menubar.setGeometry(QRect(0, 0, 600, 25))
        View.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(View)
        self.statusbar.setObjectName('statusbar')
        View.setStatusBar(self.statusbar)

        self.retranslateUi(View)

        QMetaObject.connectSlotsByName(View)

    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate('View', 'View', None))
        self.input.setText(QCoreApplication.translate('View', '0', None))
        self.history_prev.setText(QCoreApplication.translate('View', '<', None))
        self.history_next.setText(QCoreApplication.translate('View', '>', None))
        self.history_clear.setText(QCoreApplication.translate('View', 'Clear', None))
        self.label.setText(QCoreApplication.translate('View', 'History', None))
        self.button_c.setText(QCoreApplication.translate('View', 'C', None))
        self.button_3.setText(QCoreApplication.translate('View', '3', None))
        self.button_8.setText(QCoreApplication.translate('View', '8', None))
        self.button_2.setText(QCoreApplication.translate('View', '2', None))
        self.button_7.setText(QCoreApplication.translate('View', '7', None))
        self.button_6.setText(QCoreApplication.translate('View', '6', None))
        self.button_log.setText(QCoreApplication.translate('View', 'log', None))
        self.button_left_bracket.setText(QCoreApplication.translate('View', '(', None))
        self.button_5.setText(QCoreApplication.translate('View', '5', None))
        self.button_9.setText(QCoreApplication.translate('View', '9', None))
        self.button_tan.setText(QCoreApplication.translate('View', 'tan', None))
        self.button_acos.setText(QCoreApplication.translate('View', 'acos', None))
        self.button_sqrt.setText(QCoreApplication.translate('View', 'sqrt', None))
        self.button_4.setText(QCoreApplication.translate('View', '4', None))
        self.button_mult.setText(QCoreApplication.translate('View', '*', None))
        self.button_equal.setText(QCoreApplication.translate('View', '=', None))
        self.button_asin.setText(QCoreApplication.translate('View', 'asin', None))
        self.button_ln.setText(QCoreApplication.translate('View', 'ln', None))
        self.button_sin.setText(QCoreApplication.translate('View', 'sin', None))
        self.button_ac.setText(QCoreApplication.translate('View', 'AC', None))
        self.button_atan.setText(QCoreApplication.translate('View', 'atan', None))
        self.button_1.setText(QCoreApplication.translate('View', '1', None))
        self.button_rigth_bracket.setText(QCoreApplication.translate('View', ')', None))
        self.button_plus.setText(QCoreApplication.translate('View', '+', None))
        self.button_cos.setText(QCoreApplication.translate('View', 'cos', None))
        self.button_minus.setText(QCoreApplication.translate('View', '-', None))
        self.button_x.setText(QCoreApplication.translate('View', 'x', None))
        self.input_x.setText(QCoreApplication.translate('View', '0', None))
        self.button_00.setText(QCoreApplication.translate('View', '00', None))
        self.button_0.setText(QCoreApplication.translate('View', '0', None))
        self.button_dot.setText(QCoreApplication.translate('View', '.', None))
        self.button_div.setText(QCoreApplication.translate('View', '/', None))
        self.button_mod.setText(QCoreApplication.translate('View', '%', None))
        self.button_pow.setText(QCoreApplication.translate('View', '^', None))
        self.button_plot.setText(QCoreApplication.translate('View', 'Plot', None))
        self.button_credit.setText(QCoreApplication.translate('View', 'Credit', None))

    # retranslateUi
