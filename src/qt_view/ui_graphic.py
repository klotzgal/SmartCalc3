# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphic.ui'
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
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_Graphic(object):
    def setupUi(self, Graphic):
        if not Graphic.objectName():
            Graphic.setObjectName('Graphic')
        Graphic.resize(600, 538)
        Graphic.setMinimumSize(QSize(600, 500))
        Graphic.setMaximumSize(QSize(600, 624))
        Graphic.setStyleSheet(
            '* {\n'
            '	background-color: #1c1c1e; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439, \u0431\u043b\u0438\u0436\u0435 \u043a \u0447\u0435\u0440\u043d\u043e\u043c\u0443 */\n'
            '	color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n'
            "	font-family: 'Open Sans';\n"
            '    font: bold 14px;\n'
            '}\n'
            '\n'
            'QPushButton {\n'
            '	background-color: #445566; /* \u0413\u043b\u0443\u0431\u043e\u043a\u0438\u0439 \u0441\u0438\u043d\u0435-\u0441\u0435\u0440\u044b\u0439 */\n'
            '    border-style: outset;\n'
            '    border-width: 2px;\n'
            '    border-radius: 10px;\n'
            '    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
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
            'QLineEdit {\n'
            '	border-style: outset;\n'
            '    border-width: 2px;\n'
            '    border-radius: 10px;\n'
            '    border-color: #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
            '    font: bold 14px;\n'
            '    padding: 6px;\n'
            '}\n'
            '\n'
            '/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f QSlider */\n'
            'QSlider::groove:horizontal {\n'
            '    border: 1px solid #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
            '    height: 8px;\n'
            '    background: #445566; /* \u0413\u043b\u0443\u0431\u043e\u043a\u0438\u0439 \u0441\u0438\u043d\u0435-\u0441\u0435\u0440\u044b\u0439 */\n'
            '    margin: 2px 0;\n'
            '    border-radius: 4px;\n'
            '}\n'
            'QSlider::ha'
            'ndle:horizontal {\n'
            '    background: #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n'
            '    border: 1px solid #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 */\n'
            '    width: 20px;\n'
            '    height: 20px;\n'
            '    margin: -8px 0; /* \u0426\u0435\u043d\u0442\u0440\u0438\u0440\u0443\u0435\u043c \u043f\u043e\u043b\u0437\u0443\u043d\u043e\u043a */\n'
            '    border-radius: 10px;\n'
            '}\n'
            'QSlider::handle:horizontal:hover {\n'
            '    background: #89abcd; /* \u0411\u043e\u043b\u0435\u0435 \u044f\u0440\u043a\u0438\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n'
            '}\n'
            'QSlider::sub-page:horizontal {\n'
            '    background: #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 */\n'
            ''
            '}\n'
            'QSlider::add-page:horizontal {\n'
            '    background: #2a3b4c; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u043e\u0441\u043b\u0435 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n'
            '}\n'
            '\n'
            '/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f QCheckBox */\n'
            'QCheckBox {\n'
            '    spacing: 8px;\n'
            '    font: bold 14px;\n'
            '    color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n'
            '}\n'
            'QCheckBox::indicator {\n'
            '    width: 18px;\n'
            '    height: 18px;\n'
            '}\n'
            'QCheckBox::indicator:unchecked {\n'
            '    border: 2px solid #708090; /* \u0421\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 \u043a\u043e\u043d\u0442\u0443\u0440 */\n'
            '    background-color: #1c1c1e; /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n'
            '    border-radius: 4px;\n'
            '}\n'
            'QCheckBox::indicator:checked {\n'
            '    border: 2px s'
            'olid #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n'
            '    background-color: #567890; /* \u0421\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u0432\u044b\u0431\u043e\u0440\u0435 */\n'
            '    border-radius: 4px;\n'
            '}\n'
            'QCheckBox::indicator:unchecked:hover {\n'
            '    border-color: #89abcd; /* \u042f\u0440\u043a\u0438\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n'
            '}\n'
            'QCheckBox::indicator:checked:hover {\n'
            '    background-color: #89abcd; /* \u042f\u0440\u043a\u0438\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 */\n'
            '}\n'
            '\n'
            '/* \u0421\u0442\u0438\u043b\u0438 \u0434\u043b\u044f QSpinBox */\n'
            'QSpinBox {\n'
            '    background-color: #1c1c1e; /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n'
            '    border: 2px solid #708090; /* \u0421\u0442\u0430'
            '\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0440\u044b\u0439 \u043a\u043e\u043d\u0442\u0443\u0440 */\n'
            '    border-radius: 10px;\n'
            '    padding: 6px;\n'
            '    color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n'
            '    font: bold 14px;\n'
            '}\n'
            'QSpinBox::up-button {\n'
            '    background-color: #445566; /* \u0413\u043b\u0443\u0431\u043e\u043a\u0438\u0439 \u0441\u0438\u043d\u0435-\u0441\u0435\u0440\u044b\u0439 */\n'
            '    border: 1px solid #708090;\n'
            '    border-radius: 5px;\n'
            '    width: 16px;\n'
            '    height: 12px;\n'
            '}\n'
            'QSpinBox::down-button {\n'
            '    background-color: #445566; /* \u0413\u043b\u0443\u0431\u043e\u043a\u0438\u0439 \u0441\u0438\u043d\u0435-\u0441\u0435\u0440\u044b\u0439 */\n'
            '    border: 1px solid #708090;\n'
            '    border-radius: 5px;\n'
            '    width: 16px;\n'
            '    height: 12px;\n'
            '}\n'
            'QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n'
            '    background-color: #567890; /* \u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d'
            '\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n'
            '}\n'
            'QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n'
            '    background-color: #2a3b4c; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n'
            '}\n'
            'QSpinBox::up-arrow, QSpinBox::down-arrow {\n'
            '    width: 8px;\n'
            '    height: 8px;\n'
            '    color: #e5e5e5; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0442\u0440\u0435\u043b\u043e\u043a */\n'
            '}\n'
            ''
        )
        self.horizontalLayout_3 = QHBoxLayout(Graphic)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.frame_2 = QFrame(Graphic)
        self.frame_2.setObjectName('frame_2')
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.plot = QWidget(self.frame_2)
        self.plot.setObjectName('plot')
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.plot)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName('frame')
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName('verticalLayout')
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName('widget_2')
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName('horizontalLayout_4')
        self.slider = QSlider(self.widget_2)
        self.slider.setObjectName('slider')
        self.slider.setMinimum(1)
        self.slider.setMaximum(1000)
        self.slider.setSingleStep(10)
        self.slider.setValue(10)
        self.slider.setOrientation(Qt.Vertical)
        self.slider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_4.addWidget(self.slider)

        self.verticalLayout.addWidget(self.widget_2)

        self.autoscale = QCheckBox(self.frame)
        self.autoscale.setObjectName('autoscale')
        self.autoscale.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.autoscale)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName('widget')
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.limit = QSpinBox(self.widget)
        self.limit.setObjectName('limit')
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.limit.sizePolicy().hasHeightForWidth())
        self.limit.setSizePolicy(sizePolicy1)
        self.limit.setMaximumSize(QSize(60, 16777215))
        self.limit.setMinimum(-1000000)
        self.limit.setMaximum(1000000)
        self.limit.setSingleStep(1)
        self.limit.setValue(10)

        self.horizontalLayout.addWidget(self.limit)

        self.label_x_max = QLabel(self.widget)
        self.label_x_max.setObjectName('label_x_max')
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_x_max.sizePolicy().hasHeightForWidth())
        self.label_x_max.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_x_max)

        self.verticalLayout.addWidget(self.widget)

        self.button_back = QPushButton(self.frame)
        self.button_back.setObjectName('button_back')
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy3)
        self.button_back.setMinimumSize(QSize(0, 60))
        self.button_back.setMaximumSize(QSize(9999, 60))
        self.button_back.setStyleSheet('')

        self.verticalLayout.addWidget(self.button_back)

        self.horizontalLayout_2.addWidget(self.frame)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(Graphic)

        QMetaObject.connectSlotsByName(Graphic)

    # setupUi

    def retranslateUi(self, Graphic):
        Graphic.setWindowTitle(QCoreApplication.translate('Graphic', 'Form', None))
        self.autoscale.setText(QCoreApplication.translate('Graphic', 'Autoscale', None))
        self.label_x_max.setText(QCoreApplication.translate('Graphic', 'Range', None))
        self.button_back.setText(QCoreApplication.translate('Graphic', 'Back', None))

    # retranslateUi
