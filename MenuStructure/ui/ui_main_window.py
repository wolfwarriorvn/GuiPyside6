# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QToolBox,
    QVBoxLayout, QWidget)
from  . import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(817, 600)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.menu_widget.setFont(font)
        self.menu_widget.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.5, x3: 0 y3: 1,\n"
"                                     stop: 0 #ABCD44, stop: 0.5 #ABCD44,\n"
"                                     stop: 0.5 #A1C72E, stop: 1.0 #9CC322);\n"
"color: #fff;\n"
"font-size: 12pt;\n"
"border: none;")
        self.gridLayout = QGridLayout(self.menu_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.menu_widget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"#toolBox {\n"
"	color:  white;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"	padding-left:5px;\n"
"	text-align:left;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"	background-color: #2d9cdb;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"	padding:5px 0px 5px 20px;\n"
"	text-align:left;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"	background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"	background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 140, 492))
        self.verticalLayout = QVBoxLayout(self.page_3)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.btn_home = QPushButton(self.page_3)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_dashboard = QPushButton(self.page_3)
        self.btn_dashboard.setObjectName(u"btn_dashboard")

        self.verticalLayout.addWidget(self.btn_dashboard)

        self.verticalSpacer = QSpacerItem(20, 417, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon = QIcon()
        icon.addFile(u":/icons/icon/home-4-48 (2).ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon, u"Gerneral")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 140, 492))
        self.verticalLayout_2 = QVBoxLayout(self.page_4)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.btn_toyota = QPushButton(self.page_4)
        self.btn_toyota.setObjectName(u"btn_toyota")

        self.verticalLayout_2.addWidget(self.btn_toyota)

        self.btn_lexus = QPushButton(self.page_4)
        self.btn_lexus.setObjectName(u"btn_lexus")

        self.verticalLayout_2.addWidget(self.btn_lexus)

        self.btn_mazda = QPushButton(self.page_4)
        self.btn_mazda.setObjectName(u"btn_mazda")

        self.verticalLayout_2.addWidget(self.btn_mazda)

        self.verticalSpacer_2 = QSpacerItem(20, 381, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/car-4-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon1, u"Car")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 140, 492))
        self.verticalLayout_3 = QVBoxLayout(self.page_5)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.btn_youtube = QPushButton(self.page_5)
        self.btn_youtube.setObjectName(u"btn_youtube")

        self.verticalLayout_3.addWidget(self.btn_youtube)

        self.btn_tumb = QPushButton(self.page_5)
        self.btn_tumb.setObjectName(u"btn_tumb")

        self.verticalLayout_3.addWidget(self.btn_tumb)

        self.verticalSpacer_3 = QSpacerItem(20, 417, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_5, icon2, u"Social Media")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.menu_widget)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_4 = QVBoxLayout(self.main_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_widget = QWidget(self.main_widget)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setStyleSheet(u"#search_widget {background-color: #ABB2B9;}")
        self.horizontalLayout_2 = QHBoxLayout(self.search_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pushButton_8 = QPushButton(self.search_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/arrow-96-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(156, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.search_frame = QFrame(self.search_widget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(300, 0))
        self.search_frame.setStyleSheet(u"#search_frame {\n"
"	border:  1px solid #aa7e6f;\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#search_btn {\n"
"	padding:5px 5px;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#search_btn:pressed {\n"
"	padding-left: 10px;\n"
"}")
        self.search_frame.setFrameShape(QFrame.NoFrame)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.lineEdit = QLineEdit(self.search_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(False)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.search_btn = QPushButton(self.search_frame)
        self.search_btn.setObjectName(u"search_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/search-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_2.addWidget(self.search_frame)

        self.horizontalSpacer_2 = QSpacerItem(155, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_9 = QPushButton(self.search_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/user-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.pushButton_9)


        self.verticalLayout_4.addWidget(self.search_widget)

        self.tabWidget = QTabWidget(self.main_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setStyleSheet(u"#tabWidget{\n"
"	background-color: #fff\n"
"}\n"
"\n"
"QTabBar::close-button{\n"
"	margin-left: 3px;\n"
"	image: url(:/icons/icon/x-mark-4-32.ico);\n"
"}\n"
"\n"
"QTabBar::close-button:hover{\n"
"	image: url(:/icons/icon/x-mark-4-48.ico);\n"
"}")
        self.tabWidget.setTabsClosable(True)

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout_3.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_8.toggled.connect(self.menu_widget.setHidden)

        self.toolBox.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Gerneral", None))
        self.btn_toyota.setText(QCoreApplication.translate("MainWindow", u"Toyota", None))
        self.btn_lexus.setText(QCoreApplication.translate("MainWindow", u"Lexus", None))
        self.btn_mazda.setText(QCoreApplication.translate("MainWindow", u"Mazda", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Car", None))
        self.btn_youtube.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.btn_tumb.setText(QCoreApplication.translate("MainWindow", u"Tumb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.pushButton_8.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Something...", None))
        self.search_btn.setText("")
        self.pushButton_9.setText("")
    # retranslateUi

