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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)
from  . import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 648)
        MainWindow.setStyleSheet(u"#menu_widget, #toolBox {\n"
"	background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.menu_widget = QWidget(self.splitter)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMinimumSize(QSize(150, 0))
        self.menu_widget.setStyleSheet(u"background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.gridLayout = QGridLayout(self.menu_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 15)
        self.toolBox = QToolBox(self.menu_widget)
        self.toolBox.setObjectName(u"toolBox")
        font = QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(u"#toolBox {\n"
"	color: #fff;\n"
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
        self.general_page = QWidget()
        self.general_page.setObjectName(u"general_page")
        self.general_page.setGeometry(QRect(0, 0, 162, 509))
        self.verticalLayout = QVBoxLayout(self.general_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.pushButton = QPushButton(self.general_page)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton.setFont(font1)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.general_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setStyleSheet(u"")
        self.pushButton_2.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon = QIcon()
        icon.addFile(u":/icon/icon/home-4-48 (2).ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.general_page, icon, u"General")
        self.cars_page = QWidget()
        self.cars_page.setObjectName(u"cars_page")
        self.cars_page.setGeometry(QRect(0, 0, 83, 119))
        self.verticalLayout_2 = QVBoxLayout(self.cars_page)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.pushButton_3 = QPushButton(self.cars_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.cars_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.cars_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_5.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.verticalSpacer_2 = QSpacerItem(20, 350, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/car-4-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.cars_page, icon1, u"Cars")
        self.social_media_page = QWidget()
        self.social_media_page.setObjectName(u"social_media_page")
        self.social_media_page.setGeometry(QRect(0, 0, 162, 509))
        self.verticalLayout_3 = QVBoxLayout(self.social_media_page)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 5)
        self.pushButton_6 = QPushButton(self.social_media_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.social_media_page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.verticalSpacer_3 = QSpacerItem(20, 388, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.social_media_page, icon2, u"Social Media")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.splitter.addWidget(self.menu_widget)
        self.main_widget = QWidget(self.splitter)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_4 = QGridLayout(self.main_widget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_widget = QWidget(self.main_widget)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setStyleSheet(u"#search_widget {background-color: #ABB2B9;}")
        self.horizontalLayout = QHBoxLayout(self.search_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_8 = QPushButton(self.search_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/arrow-96-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/arrow-31-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(15, 15))
        self.pushButton_8.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search_frame = QFrame(self.search_widget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(300, 30))
        self.search_frame.setMaximumSize(QSize(300, 30))
        self.search_frame.setFont(font1)
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
        self.search_frame.setFrameShape(QFrame.Box)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(15, 0, 5, 0)
        self.lineEdit_5 = QLineEdit(self.search_frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_5)

        self.search_btn = QPushButton(self.search_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/search-3-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon4)
        self.search_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.search_btn)


        self.horizontalLayout.addWidget(self.search_frame)

        self.horizontalSpacer_2 = QSpacerItem(209, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.user_label = QLabel(self.search_widget)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setMinimumSize(QSize(30, 30))
        self.user_label.setMaximumSize(QSize(30, 30))
        self.user_label.setStyleSheet(u"#user_label {\n"
"	background-color: #fff;\n"
"	border: 1px solid #F2F4F4;\n"
"	padding: 5px 5px;\n"
"	border-radius: 15%;\n"
"}")
        self.user_label.setPixmap(QPixmap(u":/icon/icon/user-48.ico"))
        self.user_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.user_label)


        self.gridLayout_4.addWidget(self.search_widget, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.main_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"#tabWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"	margin-left: 3px;\n"
"	image: url(:/icon/icon/x-mark-4-32.ico)\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"	\n"
"	image: url(:/icon/icon/x-mark-4-48.ico);\n"
"}")
        self.tabWidget.setIconSize(QSize(10, 10))
        self.tabWidget.setTabsClosable(True)

        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.splitter.addWidget(self.main_widget)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_8.toggled.connect(self.menu_widget.setHidden)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)
        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.general_page), QCoreApplication.translate("MainWindow", u"General", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Toyota", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Lexus", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Mazda", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.cars_page), QCoreApplication.translate("MainWindow", u"Cars", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Tumbr", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.social_media_page), QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.pushButton_8.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Something...", None))
        self.search_btn.setText("")
        self.user_label.setText("")
    # retranslateUi

