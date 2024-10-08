# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credit.ui'
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
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Credit(object):
    def setupUi(self, Credit):
        if not Credit.objectName():
            Credit.setObjectName('Credit')
        Credit.resize(706, 371)
        Credit.setMinimumSize(QSize(706, 371))
        Credit.setMaximumSize(QSize(706, 371))
        Credit.setStyleSheet(
            '* {\n'
            '	background-color: #1c1c1e; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439, \u0431\u043b\u0438\u0436\u0435 \u043a \u0447\u0435\u0440\u043d\u043e\u043c\u0443 */\n'
            '	color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n'
            "	font-family: 'Open Sans';\n"
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
            '	background-color: #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n'
            ''
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
            '    font: bold 14px;\n'
            '    padding: 6px;\n'
            '}\n'
            '#every_month_payment, #total, #overpayment{\n'
            '	border-style: outset;\n'
            '    border-width: 2px;\n'
            '    border-radius: 10px;\n'
            '    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
            '    font: bold 14px;\n'
            '    padding: 6px;\n'
            '}'
        )
        self.verticalLayout_2 = QVBoxLayout(Credit)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.frame_2 = QFrame(Credit)
        self.frame_2.setObjectName('frame_2')
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName('groupBox')
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.label_term = QLabel(self.groupBox)
        self.label_term.setObjectName('label_term')
        self.label_term.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_term, 1, 0, 1, 1)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName('frame')
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName('verticalLayout')
        self.annuity = QRadioButton(self.frame)
        self.annuity.setObjectName('annuity')
        self.annuity.setMinimumSize(QSize(160, 0))
        self.annuity.setMaximumSize(QSize(160, 16777215))
        self.annuity.setChecked(True)

        self.verticalLayout.addWidget(self.annuity)

        self.differentiated = QRadioButton(self.frame)
        self.differentiated.setObjectName('differentiated')
        self.differentiated.setMinimumSize(QSize(160, 0))
        self.differentiated.setMaximumSize(QSize(160, 16777215))

        self.verticalLayout.addWidget(self.differentiated)

        self.gridLayout_2.addWidget(self.frame, 3, 1, 1, 1)

        self.line_edit_summ = QLineEdit(self.groupBox)
        self.line_edit_summ.setObjectName('line_edit_summ')
        self.line_edit_summ.setMinimumSize(QSize(160, 0))
        self.line_edit_summ.setMaximumSize(QSize(160, 16777215))
        self.line_edit_summ.setStyleSheet('')
        self.line_edit_summ.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_2.addWidget(self.line_edit_summ, 0, 1, 1, 1)

        self.label_summ = QLabel(self.groupBox)
        self.label_summ.setObjectName('label_summ')
        self.label_summ.setStyleSheet('')
        self.label_summ.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_summ, 0, 0, 1, 1)

        self.label_percent = QLabel(self.groupBox)
        self.label_percent.setObjectName('label_percent')
        self.label_percent.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_percent, 2, 0, 1, 1)

        self.line_edit_mounth = QLineEdit(self.groupBox)
        self.line_edit_mounth.setObjectName('line_edit_mounth')
        self.line_edit_mounth.setMinimumSize(QSize(160, 0))
        self.line_edit_mounth.setMaximumSize(QSize(160, 16777215))
        self.line_edit_mounth.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_2.addWidget(self.line_edit_mounth, 1, 1, 1, 1)

        self.label_type = QLabel(self.groupBox)
        self.label_type.setObjectName('label_type')
        self.label_type.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_type, 3, 0, 1, 1)

        self.line_edit_percent = QLineEdit(self.groupBox)
        self.line_edit_percent.setObjectName('line_edit_percent')
        self.line_edit_percent.setMinimumSize(QSize(160, 0))
        self.line_edit_percent.setMaximumSize(QSize(160, 16777215))
        self.line_edit_percent.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout_2.addWidget(self.line_edit_percent, 2, 1, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName('groupBox_2')
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName('gridLayout')
        self.label_every_month_payment = QLabel(self.groupBox_2)
        self.label_every_month_payment.setObjectName('label_every_month_payment')
        self.label_every_month_payment.setScaledContents(False)

        self.gridLayout.addWidget(self.label_every_month_payment, 0, 0, 1, 1)

        self.every_month_payment = QLabel(self.groupBox_2)
        self.every_month_payment.setObjectName('every_month_payment')
        self.every_month_payment.setMinimumSize(QSize(160, 55))
        self.every_month_payment.setMaximumSize(QSize(160, 55))
        self.every_month_payment.setScaledContents(False)
        self.every_month_payment.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout.addWidget(self.every_month_payment, 0, 1, 1, 1)

        self.label_overpayment = QLabel(self.groupBox_2)
        self.label_overpayment.setObjectName('label_overpayment')
        self.label_overpayment.setScaledContents(False)

        self.gridLayout.addWidget(self.label_overpayment, 1, 0, 1, 1)

        self.overpayment = QLabel(self.groupBox_2)
        self.overpayment.setObjectName('overpayment')
        self.overpayment.setMinimumSize(QSize(160, 55))
        self.overpayment.setMaximumSize(QSize(160, 55))
        self.overpayment.setScaledContents(False)
        self.overpayment.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.gridLayout.addWidget(self.overpayment, 1, 1, 1, 1)

        self.label_total = QLabel(self.groupBox_2)
        self.label_total.setObjectName('label_total')
        self.label_total.setScaledContents(False)

        self.gridLayout.addWidget(self.label_total, 2, 0, 1, 1)

        self.total = QLabel(self.groupBox_2)
        self.total.setObjectName('total')
        self.total.setMinimumSize(QSize(160, 55))
        self.total.setMaximumSize(QSize(160, 55))
        self.total.setScaledContents(False)
        self.total.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.total, 2, 1, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(Credit)
        self.frame_3.setObjectName('frame_3')
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.button_calc = QPushButton(self.frame_3)
        self.button_calc.setObjectName('button_calc')
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_calc.sizePolicy().hasHeightForWidth())
        self.button_calc.setSizePolicy(sizePolicy2)
        self.button_calc.setMinimumSize(QSize(0, 60))
        self.button_calc.setMaximumSize(QSize(9999, 60))
        self.button_calc.setStyleSheet('')

        self.horizontalLayout_2.addWidget(self.button_calc)

        self.button_back = QPushButton(self.frame_3)
        self.button_back.setObjectName('button_back')
        sizePolicy2.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy2)
        self.button_back.setMinimumSize(QSize(0, 60))
        self.button_back.setMaximumSize(QSize(9999, 60))
        self.button_back.setStyleSheet('')

        self.horizontalLayout_2.addWidget(self.button_back)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.retranslateUi(Credit)

        QMetaObject.connectSlotsByName(Credit)

    # setupUi

    def retranslateUi(self, Credit):
        Credit.setWindowTitle(QCoreApplication.translate('Credit', 'Form', None))
        self.groupBox.setTitle('')
        self.label_term.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0421\u0440\u043e\u043a \u043a\u0440\u0435\u0434\u0438\u0442\u0430\n'
                '\u0432 \u043c\u0435\u0441\u044f\u0446\u0430\u0445',
                None,
            )
        )
        self.annuity.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0410\u043d\u043d\u0443\u0438\u0442\u0435\u0442\u043d\u044b\u0439',
                None,
            )
        )
        self.differentiated.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0414\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439',
                None,
            )
        )
        self.line_edit_summ.setText(QCoreApplication.translate('Credit', '0', None))
        self.label_summ.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0421\u0443\u043c\u043c\u0430 \u043a\u0440\u0435\u0434\u0438\u0442\u0430\n'
                '\u0432 \u0440\u0443\u0431\u043b\u044f\u0445',
                None,
            )
        )
        self.label_percent.setText(
            QCoreApplication.translate(
                'Credit',
                '\u041f\u0440\u043e\u0446\u0435\u043d\u0442\u043d\u0430\u044f \n'
                '\u0441\u0442\u0430\u0432\u043a\u0430',
                None,
            )
        )
        self.line_edit_mounth.setText(QCoreApplication.translate('Credit', '0', None))
        self.label_type.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0422\u0438\u043f \u0435\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0445 \n'
                '\u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439',
                None,
            )
        )
        self.line_edit_percent.setText(QCoreApplication.translate('Credit', '0', None))
        self.groupBox_2.setTitle('')
        self.label_every_month_payment.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0415\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0439 \n'
                '\u043f\u043b\u0430\u0442\u0435\u0436',
                None,
            )
        )
        self.every_month_payment.setText(
            QCoreApplication.translate('Credit', '0', None)
        )
        self.label_overpayment.setText(
            QCoreApplication.translate(
                'Credit',
                '\u041f\u0435\u0440\u0435\u043f\u043b\u0430\u0442\u0430\n'
                '\u043f\u043e \u043a\u0440\u0435\u0434\u0438\u0442\u0443',
                None,
            )
        )
        self.overpayment.setText(QCoreApplication.translate('Credit', '0', None))
        self.label_total.setText(
            QCoreApplication.translate(
                'Credit',
                '\u0414\u043e\u043b\u0433 + \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u044b',
                None,
            )
        )
        self.total.setText(QCoreApplication.translate('Credit', '0', None))
        self.button_calc.setText(
            QCoreApplication.translate('Credit', 'Calculate', None)
        )
        self.button_back.setText(QCoreApplication.translate('Credit', 'Back', None))

    # retranslateUi
