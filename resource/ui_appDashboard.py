# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appDashboardUprBHf.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import QCustomSlideMenu
#import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 658)
        MainWindow.setStyleSheet(u"	*{\n"
"	color: #000;\n"
"	border: none;\n"
"	\n"
"	\n"
"	\n"
"}\n"
"#leftMenu, #frame_11, #frame_8 {\n"
"	background-color: #879CEB;\n"
"}\n"
"\n"
"#customerName, #customerAddress, #customerPhoneNum {\n"
"	color: black;\n"
"	\n"
"}\n"
"\n"
"\n"
"#PackageBtn, #dishesBtn, #servicesBtn{\n"
"	background-color: #879CEB;\n"
"	border-radius: 10px;\n"
"}\n"
"#addCustomer {\n"
"	background-color: #879CEB;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"#dashBoard_1,  #label_2, #dashBoard_2, #label_3, #label_4, #label_5, #dashBoard_3, #dashBoard_4, #dashBoard_5, #label_6{\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"#dashBoard {\n"
"	color: #87CEEB;\n"
"}\n"
"\n"
"#packages, #dishes, #services, #orders, #customers{\n"
"	color: #87CEEB;\n"
"}\n"
"\n"
"#homeBtn, #ordersMenuBtn, #customersMenuBtn, #packagesMenuBtn, #dishesMenuBtn, #servicesMenuBtn    {\n"
"	color: #FFFFFF\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#homeBtn {\n"
"	background-color: "
                        "#87CEEB;\n"
"	padding: 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px\n"
"}\n"
"#ordersMenuBtn, #customersMenuBtn, #packagesMenuBtn, #dishesMenuBtn, #servicesMenuBtn {\n"
"\n"
"	padding: 5px;\n"
"	text-align: left;\n"
"	\n"
"}\n"
"#aboutBtn, #aboutBtn_1, #aboutBtn_2, #aboutBtn_3, #aboutBtn_4, #aboutBtn_5{\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	background-color: #879CEB;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: transparent;\n"
"}\n"
"#searchBar, #searchBar_1, #searchBar_2, #searchBar_3, #searchBar_4, #searchBar_5 {\n"
"	border-radius: 10px;\n"
"	border: 2px solid #879CEB;\n"
"}\n"
"#menuBtn, #menuBtn_1, #menuBtn_2, #menuBtn_3, #menuBtn_4, #menuBtn_5{\n"
"	background-color: #879CEB;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#dishCard, #packageCard, #serviceCard, #ordersCard, #customersCard{\n"
"	border-radius: 20px;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#headerF"
                        "rame, #headerFrame_2, #headerFrame_3, #headerFrame_4, #headerFrame_5, #headerFrame_6{\n"
"\n"
"	background-color: #FFFFFF\n"
"}\n"
"#ordersBtn, #customersBtn {\n"
"	background-color: #879CEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 658))
        self.leftMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.leftMenu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 18, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_10)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"resource/dashboard.png"))

        self.horizontalLayout_15.addWidget(self.label)


        self.verticalLayout_8.addWidget(self.frame_10, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, -1, 0, -1)
        self.homeBtn = QPushButton(self.frame_9)
        self.homeBtn.setObjectName(u"homeBtn")
        font1 = QFont()
        font1.setPointSize(12)
        self.homeBtn.setFont(font1)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"resource/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.homeBtn)

        self.ordersMenuBtn = QPushButton(self.frame_9)
        self.ordersMenuBtn.setObjectName(u"ordersMenuBtn")
        self.ordersMenuBtn.setFont(font1)
        self.ordersMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"resource/orders.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ordersMenuBtn.setIcon(icon1)
        self.ordersMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.ordersMenuBtn)

        self.customersMenuBtn = QPushButton(self.frame_9)
        self.customersMenuBtn.setObjectName(u"customersMenuBtn")
        self.customersMenuBtn.setFont(font1)
        self.customersMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"resource/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.customersMenuBtn.setIcon(icon2)
        self.customersMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.customersMenuBtn)

        self.line = QFrame(self.frame_9)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(182, 16777215))
        font2 = QFont()
        font2.setBold(False)
        font2.setUnderline(False)
        self.line.setFont(font2)
        self.line.setStyleSheet(u"background-color: #FFFFFF")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.packagesMenuBtn = QPushButton(self.frame_9)
        self.packagesMenuBtn.setObjectName(u"packagesMenuBtn")
        self.packagesMenuBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"resource/package.png", QSize(), QIcon.Normal, QIcon.Off)
        self.packagesMenuBtn.setIcon(icon3)
        self.packagesMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.packagesMenuBtn)

        self.servicesMenuBtn = QPushButton(self.frame_9)
        self.servicesMenuBtn.setObjectName(u"servicesMenuBtn")
        self.servicesMenuBtn.setFont(font1)
        self.servicesMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"resource/dishes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.servicesMenuBtn.setIcon(icon4)
        self.servicesMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.servicesMenuBtn)

        self.dishesMenuBtn = QPushButton(self.frame_9)
        self.dishesMenuBtn.setObjectName(u"dishesMenuBtn")
        self.dishesMenuBtn.setFont(font1)
        self.dishesMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"resource/truck.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dishesMenuBtn.setIcon(icon5)
        self.dishesMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.dishesMenuBtn)


        self.verticalLayout_8.addWidget(self.frame_9, 0, Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.leftMenu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 306, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QStackedWidget(self.mainBody)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.homePage)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(40, 34))
        self.menuBtn.setMaximumSize(QSize(40, 16777215))
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"resource/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon6)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignVCenter)

        self.dashBoard = QLabel(self.widget)
        self.dashBoard.setObjectName(u"dashBoard")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.dashBoard.setFont(font3)

        self.horizontalLayout_3.addWidget(self.dashBoard)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.headerFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchBar = QFrame(self.widget_2)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(160, 0))
        self.searchBar.setFrameShape(QFrame.StyledPanel)
        self.searchBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.searchBtn = QLabel(self.searchBar)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(24, 24))
        self.searchBtn.setMaximumSize(QSize(24, 24))
        self.searchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn.setPixmap(QPixmap(u"resource/search.svg"))
        self.searchBtn.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.searchBtn)

        self.lineEdit = QLineEdit(self.searchBar)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_4.addWidget(self.searchBar, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn = QPushButton(self.widget_3)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon7 = QIcon()
        icon7.addFile(u"resource/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon7)
        self.aboutBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.aboutBtn, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.headerFrame)

        self.cardFrame = QWidget(self.homePage)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 5, 9, 0)
        self.packageCard = QFrame(self.cardFrame)
        self.packageCard.setObjectName(u"packageCard")
        self.packageCard.setFrameShape(QFrame.StyledPanel)
        self.packageCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.packageCard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.packageCard)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 15, -1, 15)
        self.packages = QLabel(self.frame)
        self.packages.setObjectName(u"packages")
        self.packages.setFont(font3)

        self.horizontalLayout_8.addWidget(self.packages)

        self.PackageBtn = QPushButton(self.frame)
        self.PackageBtn.setObjectName(u"PackageBtn")
        self.PackageBtn.setMinimumSize(QSize(64, 50))
        self.PackageBtn.setMaximumSize(QSize(64, 16777215))
        self.PackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"resource/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PackageBtn.setIcon(icon8)
        self.PackageBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.PackageBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_7.addWidget(self.packageCard)

        self.dishCard = QFrame(self.cardFrame)
        self.dishCard.setObjectName(u"dishCard")
        self.dishCard.setFrameShape(QFrame.StyledPanel)
        self.dishCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dishCard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.dishCard)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 15, -1, 15)
        self.dishes = QLabel(self.frame_2)
        self.dishes.setObjectName(u"dishes")
        self.dishes.setFont(font3)

        self.horizontalLayout_9.addWidget(self.dishes)

        self.dishesBtn = QPushButton(self.frame_2)
        self.dishesBtn.setObjectName(u"dishesBtn")
        self.dishesBtn.setMinimumSize(QSize(64, 50))
        self.dishesBtn.setMaximumSize(QSize(64, 16777215))
        self.dishesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dishesBtn.setIcon(icon4)
        self.dishesBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.dishesBtn)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.dishCard)

        self.serviceCard = QFrame(self.cardFrame)
        self.serviceCard.setObjectName(u"serviceCard")
        self.serviceCard.setFrameShape(QFrame.StyledPanel)
        self.serviceCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.serviceCard)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 15, -1, 15)
        self.frame_3 = QFrame(self.serviceCard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.services = QLabel(self.frame_3)
        self.services.setObjectName(u"services")
        self.services.setFont(font3)

        self.horizontalLayout_10.addWidget(self.services)

        self.servicesBtn = QPushButton(self.frame_3)
        self.servicesBtn.setObjectName(u"servicesBtn")
        self.servicesBtn.setMinimumSize(QSize(64, 50))
        self.servicesBtn.setMaximumSize(QSize(64, 16777215))
        self.servicesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.servicesBtn.setIcon(icon5)
        self.servicesBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_10.addWidget(self.servicesBtn)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.serviceCard)


        self.verticalLayout_10.addWidget(self.cardFrame)

        self.mainFrame = QWidget(self.homePage)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, -1)
        self.ordersCard = QWidget(self.mainFrame)
        self.ordersCard.setObjectName(u"ordersCard")
        self.verticalLayout_6 = QVBoxLayout(self.ordersCard)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.ordersCard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.orders = QLabel(self.frame_4)
        self.orders.setObjectName(u"orders")
        self.orders.setFont(font3)

        self.horizontalLayout_12.addWidget(self.orders, 0, Qt.AlignLeft)

        self.ordersBtn = QPushButton(self.frame_4)
        self.ordersBtn.setObjectName(u"ordersBtn")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.ordersBtn.setFont(font4)
        self.ordersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"resource/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ordersBtn.setIcon(icon9)
        self.ordersBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.ordersBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.ordersCard)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_5)


        self.horizontalLayout_11.addWidget(self.ordersCard)

        self.customersCard = QWidget(self.mainFrame)
        self.customersCard.setObjectName(u"customersCard")
        self.verticalLayout_5 = QVBoxLayout(self.customersCard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.customersCard)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.customers = QLabel(self.frame_6)
        self.customers.setObjectName(u"customers")
        self.customers.setFont(font3)

        self.horizontalLayout_13.addWidget(self.customers, 0, Qt.AlignLeft)

        self.customersBtn = QPushButton(self.frame_6)
        self.customersBtn.setObjectName(u"customersBtn")
        self.customersBtn.setFont(font4)
        self.customersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.customersBtn.setIcon(icon9)
        self.customersBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.customersBtn, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.customersCard)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tableWidget_2 = QTableWidget(self.frame_7)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_14.addWidget(self.tableWidget_2)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.horizontalLayout_11.addWidget(self.customersCard)


        self.verticalLayout_10.addWidget(self.mainFrame)

        self.mainPages.addWidget(self.homePage)
        self.ordersPage = QWidget()
        self.ordersPage.setObjectName(u"ordersPage")
        self.verticalLayout_12 = QVBoxLayout(self.ordersPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.ordersPage)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.widget_10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_2 = QWidget(self.widget_10)
        self.headerFrame_2.setObjectName(u"headerFrame_2")
        self.horizontalLayout_26 = QHBoxLayout(self.headerFrame_2)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.headerFrame_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 6, -1, -1)
        self.menuBtn_1 = QPushButton(self.widget_11)
        self.menuBtn_1.setObjectName(u"menuBtn_1")
        self.menuBtn_1.setMinimumSize(QSize(40, 34))
        self.menuBtn_1.setMaximumSize(QSize(40, 16777215))
        self.menuBtn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn_1.setIcon(icon6)
        self.menuBtn_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.menuBtn_1, 0, Qt.AlignVCenter)

        self.dashBoard_1 = QLabel(self.widget_11)
        self.dashBoard_1.setObjectName(u"dashBoard_1")
        self.dashBoard_1.setFont(font3)

        self.horizontalLayout_27.addWidget(self.dashBoard_1)


        self.horizontalLayout_26.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.headerFrame_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.searchBar_1 = QFrame(self.widget_12)
        self.searchBar_1.setObjectName(u"searchBar_1")
        self.searchBar_1.setMinimumSize(QSize(160, 0))
        self.searchBar_1.setFrameShape(QFrame.StyledPanel)
        self.searchBar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.searchBar_1)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 1, 0, 2)
        self.searchBtn_1 = QLabel(self.searchBar_1)
        self.searchBtn_1.setObjectName(u"searchBtn_1")
        self.searchBtn_1.setMinimumSize(QSize(24, 24))
        self.searchBtn_1.setMaximumSize(QSize(24, 24))
        self.searchBtn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn_1.setPixmap(QPixmap(u"resource/search.svg"))
        self.searchBtn_1.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.searchBtn_1)

        self.lineEdit_1 = QLineEdit(self.searchBar_1)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.horizontalLayout_29.addWidget(self.lineEdit_1)


        self.horizontalLayout_28.addWidget(self.searchBar_1, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_26.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.headerFrame_2)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn_1 = QPushButton(self.widget_13)
        self.aboutBtn_1.setObjectName(u"aboutBtn_1")
        self.aboutBtn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn_1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aboutBtn_1.setIcon(icon7)
        self.aboutBtn_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_30.addWidget(self.aboutBtn_1, 0, Qt.AlignTop)


        self.horizontalLayout_26.addWidget(self.widget_13, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.headerFrame_2)

        self.frame_12 = QFrame(self.widget_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(18, 18, 18, -1)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: #879CEB")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer)

        self.deleteOrderBtn = QPushButton(self.frame_13)
        self.deleteOrderBtn.setObjectName(u"deleteOrderBtn")
        self.deleteOrderBtn.setFont(font4)
        self.deleteOrderBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteOrderBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"resource/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteOrderBtn.setIcon(icon10)
        self.deleteOrderBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.deleteOrderBtn)

        self.editOrderBtn = QPushButton(self.frame_13)
        self.editOrderBtn.setObjectName(u"editOrderBtn")
        self.editOrderBtn.setMaximumSize(QSize(16777215, 16777212))
        self.editOrderBtn.setFont(font4)
        self.editOrderBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editOrderBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"resource/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editOrderBtn.setIcon(icon11)
        self.editOrderBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.editOrderBtn, 0, Qt.AlignRight)

        self.createOrderBtn = QPushButton(self.frame_13)
        self.createOrderBtn.setObjectName(u"createOrderBtn")
        self.createOrderBtn.setFont(font4)
        self.createOrderBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createOrderBtn.setStyleSheet(u"\n"
"	background-color:#87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"resource/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createOrderBtn.setIcon(icon12)
        self.createOrderBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.createOrderBtn, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_13)

        self.ordersTableWidget = QTableWidget(self.frame_12)
        if (self.ordersTableWidget.columnCount() < 6):
            self.ordersTableWidget.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        self.ordersTableWidget.setObjectName(u"ordersTableWidget")
        self.ordersTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.ordersTableWidget)


        self.verticalLayout_13.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.mainPages.addWidget(self.ordersPage)
        self.customersPage = QWidget()
        self.customersPage.setObjectName(u"customersPage")
        font5 = QFont()
        font5.setPointSize(16)
        self.customersPage.setFont(font5)
        self.verticalLayout_17 = QVBoxLayout(self.customersPage)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.customersPage)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_14)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_3 = QWidget(self.widget_14)
        self.headerFrame_3.setObjectName(u"headerFrame_3")
        self.horizontalLayout_31 = QHBoxLayout(self.headerFrame_3)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.headerFrame_3)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, 6, -1, -1)
        self.menuBtn_2 = QPushButton(self.widget_15)
        self.menuBtn_2.setObjectName(u"menuBtn_2")
        self.menuBtn_2.setMinimumSize(QSize(40, 34))
        self.menuBtn_2.setMaximumSize(QSize(40, 16777215))
        self.menuBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn_2.setIcon(icon6)
        self.menuBtn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.menuBtn_2, 0, Qt.AlignVCenter)

        self.dashBoard_2 = QLabel(self.widget_15)
        self.dashBoard_2.setObjectName(u"dashBoard_2")
        self.dashBoard_2.setFont(font3)

        self.horizontalLayout_32.addWidget(self.dashBoard_2)


        self.horizontalLayout_31.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.headerFrame_3)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.searchBar_2 = QFrame(self.widget_16)
        self.searchBar_2.setObjectName(u"searchBar_2")
        self.searchBar_2.setMinimumSize(QSize(160, 0))
        font6 = QFont()
        font6.setPointSize(9)
        self.searchBar_2.setFont(font6)
        self.searchBar_2.setFrameShape(QFrame.StyledPanel)
        self.searchBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.searchBar_2)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 1, 0, 2)
        self.searchBtn_2 = QLabel(self.searchBar_2)
        self.searchBtn_2.setObjectName(u"searchBtn_2")
        self.searchBtn_2.setMinimumSize(QSize(24, 24))
        self.searchBtn_2.setMaximumSize(QSize(24, 24))
        self.searchBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn_2.setPixmap(QPixmap(u"resource/search.svg"))
        self.searchBtn_2.setScaledContents(True)

        self.horizontalLayout_34.addWidget(self.searchBtn_2)

        self.lineEdit_2 = QLineEdit(self.searchBar_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_34.addWidget(self.lineEdit_2)


        self.horizontalLayout_33.addWidget(self.searchBar_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_31.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.headerFrame_3)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn_2 = QPushButton(self.widget_17)
        self.aboutBtn_2.setObjectName(u"aboutBtn_2")
        self.aboutBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aboutBtn_2.setIcon(icon7)
        self.aboutBtn_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_35.addWidget(self.aboutBtn_2, 0, Qt.AlignTop)


        self.horizontalLayout_31.addWidget(self.widget_17, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.headerFrame_3)

        self.frame_14 = QFrame(self.widget_14)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(18, 18, 18, -1)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: #879CEB")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)

        self.deleteCustomerBtn = QPushButton(self.frame_15)
        self.deleteCustomerBtn.setObjectName(u"deleteCustomerBtn")
        self.deleteCustomerBtn.setFont(font4)
        self.deleteCustomerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteCustomerBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.deleteCustomerBtn.setIcon(icon10)
        self.deleteCustomerBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.deleteCustomerBtn)

        self.editCustomerBtn = QPushButton(self.frame_15)
        self.editCustomerBtn.setObjectName(u"editCustomerBtn")
        self.editCustomerBtn.setMaximumSize(QSize(16777215, 16777212))
        self.editCustomerBtn.setFont(font4)
        self.editCustomerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editCustomerBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.editCustomerBtn.setIcon(icon11)
        self.editCustomerBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.editCustomerBtn, 0, Qt.AlignRight)

        self.createCustomerBtn = QPushButton(self.frame_15)
        self.createCustomerBtn.setObjectName(u"createCustomerBtn")
        self.createCustomerBtn.setFont(font4)
        self.createCustomerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createCustomerBtn.setStyleSheet(u"\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.createCustomerBtn.setIcon(icon12)
        self.createCustomerBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.createCustomerBtn, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_15)

        self.customersTableWidget = QTableWidget(self.frame_14)
        if (self.customersTableWidget.columnCount() < 4):
            self.customersTableWidget.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.customersTableWidget.setObjectName(u"customersTableWidget")
        self.customersTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.customersTableWidget)


        self.verticalLayout_15.addWidget(self.frame_14)


        self.verticalLayout_17.addWidget(self.widget_14)

        self.mainPages.addWidget(self.customersPage)
        self.dishesPage = QWidget()
        self.dishesPage.setObjectName(u"dishesPage")
        self.verticalLayout_20 = QVBoxLayout(self.dishesPage)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.dishesPage)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.widget_18)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_4 = QWidget(self.widget_18)
        self.headerFrame_4.setObjectName(u"headerFrame_4")
        self.horizontalLayout_36 = QHBoxLayout(self.headerFrame_4)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.headerFrame_4)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 6, -1, -1)
        self.menuBtn_3 = QPushButton(self.widget_19)
        self.menuBtn_3.setObjectName(u"menuBtn_3")
        self.menuBtn_3.setMinimumSize(QSize(40, 34))
        self.menuBtn_3.setMaximumSize(QSize(40, 16777215))
        self.menuBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn_3.setIcon(icon6)
        self.menuBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_37.addWidget(self.menuBtn_3, 0, Qt.AlignVCenter)

        self.dashBoard_3 = QLabel(self.widget_19)
        self.dashBoard_3.setObjectName(u"dashBoard_3")
        self.dashBoard_3.setFont(font3)

        self.horizontalLayout_37.addWidget(self.dashBoard_3)


        self.horizontalLayout_36.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.headerFrame_4)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.searchBar_3 = QFrame(self.widget_20)
        self.searchBar_3.setObjectName(u"searchBar_3")
        self.searchBar_3.setMinimumSize(QSize(160, 0))
        self.searchBar_3.setFrameShape(QFrame.StyledPanel)
        self.searchBar_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.searchBar_3)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 1, 0, 2)
        self.searchBtn_3 = QLabel(self.searchBar_3)
        self.searchBtn_3.setObjectName(u"searchBtn_3")
        self.searchBtn_3.setMinimumSize(QSize(24, 24))
        self.searchBtn_3.setMaximumSize(QSize(24, 24))
        self.searchBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn_3.setPixmap(QPixmap(u"resource/search.svg"))
        self.searchBtn_3.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.searchBtn_3)

        self.lineEdit_3 = QLineEdit(self.searchBar_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_39.addWidget(self.lineEdit_3)


        self.horizontalLayout_38.addWidget(self.searchBar_3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_36.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.headerFrame_4)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn_3 = QPushButton(self.widget_21)
        self.aboutBtn_3.setObjectName(u"aboutBtn_3")
        self.aboutBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aboutBtn_3.setIcon(icon7)
        self.aboutBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_40.addWidget(self.aboutBtn_3, 0, Qt.AlignTop)


        self.horizontalLayout_36.addWidget(self.widget_21, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.headerFrame_4)

        self.frame_16 = QFrame(self.widget_18)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(18, 18, 18, -1)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: #879CEB")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_18.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)

        self.deleteDishesBtn = QPushButton(self.frame_17)
        self.deleteDishesBtn.setObjectName(u"deleteDishesBtn")
        self.deleteDishesBtn.setFont(font4)
        self.deleteDishesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteDishesBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.deleteDishesBtn.setIcon(icon10)
        self.deleteDishesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.deleteDishesBtn)

        self.editDishesBtn = QPushButton(self.frame_17)
        self.editDishesBtn.setObjectName(u"editDishesBtn")
        self.editDishesBtn.setMaximumSize(QSize(16777215, 16777212))
        self.editDishesBtn.setFont(font4)
        self.editDishesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editDishesBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.editDishesBtn.setIcon(icon11)
        self.editDishesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.editDishesBtn, 0, Qt.AlignRight)

        self.createDishesBtn = QPushButton(self.frame_17)
        self.createDishesBtn.setObjectName(u"createDishesBtn")
        self.createDishesBtn.setFont(font4)
        self.createDishesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createDishesBtn.setStyleSheet(u"\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.createDishesBtn.setIcon(icon12)
        self.createDishesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.createDishesBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_17)

        self.dishesTableWidget = QTableWidget(self.frame_16)
        if (self.dishesTableWidget.columnCount() < 2):
            self.dishesTableWidget.setColumnCount(2)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.dishesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.dishesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        self.dishesTableWidget.setObjectName(u"dishesTableWidget")
        self.dishesTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_19.addWidget(self.dishesTableWidget)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_20.addWidget(self.widget_18)

        self.mainPages.addWidget(self.dishesPage)
        self.servicesPage = QWidget()
        self.servicesPage.setObjectName(u"servicesPage")
        self.verticalLayout_23 = QVBoxLayout(self.servicesPage)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.servicesPage)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.widget_22)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_5 = QWidget(self.widget_22)
        self.headerFrame_5.setObjectName(u"headerFrame_5")
        self.horizontalLayout_41 = QHBoxLayout(self.headerFrame_5)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.headerFrame_5)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 6, -1, -1)
        self.menuBtn_4 = QPushButton(self.widget_23)
        self.menuBtn_4.setObjectName(u"menuBtn_4")
        self.menuBtn_4.setMinimumSize(QSize(40, 34))
        self.menuBtn_4.setMaximumSize(QSize(40, 16777215))
        self.menuBtn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn_4.setIcon(icon6)
        self.menuBtn_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_42.addWidget(self.menuBtn_4, 0, Qt.AlignVCenter)

        self.dashBoard_4 = QLabel(self.widget_23)
        self.dashBoard_4.setObjectName(u"dashBoard_4")
        self.dashBoard_4.setFont(font3)

        self.horizontalLayout_42.addWidget(self.dashBoard_4)


        self.horizontalLayout_41.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.headerFrame_5)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.searchBar_4 = QFrame(self.widget_24)
        self.searchBar_4.setObjectName(u"searchBar_4")
        self.searchBar_4.setMinimumSize(QSize(160, 0))
        self.searchBar_4.setFrameShape(QFrame.StyledPanel)
        self.searchBar_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.searchBar_4)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 1, 0, 2)
        self.searchBtn_4 = QLabel(self.searchBar_4)
        self.searchBtn_4.setObjectName(u"searchBtn_4")
        self.searchBtn_4.setMinimumSize(QSize(24, 24))
        self.searchBtn_4.setMaximumSize(QSize(24, 24))
        self.searchBtn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn_4.setPixmap(QPixmap(u"resource/search.svg"))
        self.searchBtn_4.setScaledContents(True)

        self.horizontalLayout_44.addWidget(self.searchBtn_4)

        self.lineEdit_4 = QLineEdit(self.searchBar_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_44.addWidget(self.lineEdit_4)


        self.horizontalLayout_43.addWidget(self.searchBar_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_41.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.headerFrame_5)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn_4 = QPushButton(self.widget_25)
        self.aboutBtn_4.setObjectName(u"aboutBtn_4")
        self.aboutBtn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aboutBtn_4.setIcon(icon7)
        self.aboutBtn_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_45.addWidget(self.aboutBtn_4, 0, Qt.AlignTop)


        self.horizontalLayout_41.addWidget(self.widget_25, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_21.addWidget(self.headerFrame_5)

        self.frame_18 = QFrame(self.widget_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_18)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(18, 18, 18, -1)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: #879CEB")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_5 = QLabel(self.frame_19)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_19.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.deleteServiceBtn = QPushButton(self.frame_19)
        self.deleteServiceBtn.setObjectName(u"deleteServiceBtn")
        self.deleteServiceBtn.setFont(font4)
        self.deleteServiceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteServiceBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.deleteServiceBtn.setIcon(icon10)
        self.deleteServiceBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.deleteServiceBtn)

        self.editServiceBtn = QPushButton(self.frame_19)
        self.editServiceBtn.setObjectName(u"editServiceBtn")
        self.editServiceBtn.setMaximumSize(QSize(16777215, 16777212))
        self.editServiceBtn.setFont(font4)
        self.editServiceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editServiceBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.editServiceBtn.setIcon(icon11)
        self.editServiceBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.editServiceBtn, 0, Qt.AlignRight)

        self.createServiceBtn = QPushButton(self.frame_19)
        self.createServiceBtn.setObjectName(u"createServiceBtn")
        self.createServiceBtn.setFont(font4)
        self.createServiceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createServiceBtn.setStyleSheet(u"\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.createServiceBtn.setIcon(icon12)
        self.createServiceBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.createServiceBtn, 0, Qt.AlignRight)


        self.verticalLayout_22.addWidget(self.frame_19)

        self.servicesTableWidget = QTableWidget(self.frame_18)
        if (self.servicesTableWidget.columnCount() < 2):
            self.servicesTableWidget.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.servicesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.servicesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        self.servicesTableWidget.setObjectName(u"servicesTableWidget")
        self.servicesTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_22.addWidget(self.servicesTableWidget)


        self.verticalLayout_21.addWidget(self.frame_18)


        self.verticalLayout_23.addWidget(self.widget_22)

        self.mainPages.addWidget(self.servicesPage)
        self.packagesPage = QWidget()
        self.packagesPage.setObjectName(u"packagesPage")
        self.verticalLayout_26 = QVBoxLayout(self.packagesPage)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.packagesPage)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.widget_26)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_6 = QWidget(self.widget_26)
        self.headerFrame_6.setObjectName(u"headerFrame_6")
        self.horizontalLayout_46 = QHBoxLayout(self.headerFrame_6)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.headerFrame_6)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(-1, 6, -1, -1)
        self.menuBtn_5 = QPushButton(self.widget_27)
        self.menuBtn_5.setObjectName(u"menuBtn_5")
        self.menuBtn_5.setMinimumSize(QSize(40, 34))
        self.menuBtn_5.setMaximumSize(QSize(40, 16777215))
        self.menuBtn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn_5.setIcon(icon6)
        self.menuBtn_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_47.addWidget(self.menuBtn_5, 0, Qt.AlignVCenter)

        self.dashBoard_5 = QLabel(self.widget_27)
        self.dashBoard_5.setObjectName(u"dashBoard_5")
        self.dashBoard_5.setFont(font3)

        self.horizontalLayout_47.addWidget(self.dashBoard_5)


        self.horizontalLayout_46.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.headerFrame_6)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_48 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.searchBar_5 = QFrame(self.widget_28)
        self.searchBar_5.setObjectName(u"searchBar_5")
        self.searchBar_5.setMinimumSize(QSize(160, 0))
        self.searchBar_5.setFrameShape(QFrame.StyledPanel)
        self.searchBar_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.searchBar_5)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 1, 0, 2)
        self.searchBtn_5 = QLabel(self.searchBar_5)
        self.searchBtn_5.setObjectName(u"searchBtn_5")
        self.searchBtn_5.setMinimumSize(QSize(24, 24))
        self.searchBtn_5.setMaximumSize(QSize(24, 24))
        self.searchBtn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn_5.setPixmap(QPixmap(u"resource/search.svg"))
        self.searchBtn_5.setScaledContents(True)

        self.horizontalLayout_49.addWidget(self.searchBtn_5)

        self.lineEdit_5 = QLineEdit(self.searchBar_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_49.addWidget(self.lineEdit_5)


        self.horizontalLayout_48.addWidget(self.searchBar_5, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_46.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.headerFrame_6)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn_5 = QPushButton(self.widget_29)
        self.aboutBtn_5.setObjectName(u"aboutBtn_5")
        self.aboutBtn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aboutBtn_5.setIcon(icon7)
        self.aboutBtn_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_50.addWidget(self.aboutBtn_5, 0, Qt.AlignTop)


        self.horizontalLayout_46.addWidget(self.widget_29, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.headerFrame_6)

        self.frame_20 = QFrame(self.widget_26)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(18, 18, 18, -1)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: #879CEB")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_6 = QLabel(self.frame_21)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_20.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)

        self.deletePackageBtn = QPushButton(self.frame_21)
        self.deletePackageBtn.setObjectName(u"deletePackageBtn")
        self.deletePackageBtn.setFont(font4)
        self.deletePackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletePackageBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.deletePackageBtn.setIcon(icon10)
        self.deletePackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.deletePackageBtn)

        self.editPackageBtn = QPushButton(self.frame_21)
        self.editPackageBtn.setObjectName(u"editPackageBtn")
        self.editPackageBtn.setMaximumSize(QSize(16777215, 16777212))
        self.editPackageBtn.setFont(font4)
        self.editPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editPackageBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.editPackageBtn.setIcon(icon11)
        self.editPackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.editPackageBtn, 0, Qt.AlignRight)

        self.createPackageBtn = QPushButton(self.frame_21)
        self.createPackageBtn.setObjectName(u"createPackageBtn")
        self.createPackageBtn.setFont(font4)
        self.createPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createPackageBtn.setStyleSheet(u"\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.createPackageBtn.setIcon(icon12)
        self.createPackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.createPackageBtn, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_21)

        self.packagesTableWidget = QTableWidget(self.frame_20)
        if (self.packagesTableWidget.columnCount() < 4):
            self.packagesTableWidget.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        self.packagesTableWidget.setObjectName(u"packagesTableWidget")
        self.packagesTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.packagesTableWidget)


        self.verticalLayout_24.addWidget(self.frame_20)


        self.verticalLayout_26.addWidget(self.widget_26)

        self.mainPages.addWidget(self.packagesPage)

        self.verticalLayout.addWidget(self.mainPages)


        self.horizontalLayout.addWidget(self.mainBody)

        self.rightMenu = QCustomSlideMenu(self.centralwidget)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(16777215, 16777215))
        self.rightMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_43 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.rightMenu)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(200, 350))
        self.widget_8.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_44 = QVBoxLayout(self.widget_8)
        self.verticalLayout_44.setSpacing(9)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, -1, -1, 0)
        self.frame_34 = QFrame(self.widget_8)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy1)
        self.frame_34.setStyleSheet(u"background-color: #879CEB;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.iconCloseStudent_5 = QPushButton(self.frame_34)
        self.iconCloseStudent_5.setObjectName(u"iconCloseStudent_5")
        icon13 = QIcon()
        icon13.addFile(u"../SSIS v@/Resource/closeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconCloseStudent_5.setIcon(icon13)
        self.iconCloseStudent_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_52.addWidget(self.iconCloseStudent_5, 0, Qt.AlignRight)


        self.verticalLayout_44.addWidget(self.frame_34)

        self.label_15 = QLabel(self.widget_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(70, 70))
        self.label_15.setMaximumSize(QSize(70, 70))
        self.label_15.setPixmap(QPixmap(u"../SSIS v@/Resource/addUser.png"))
        self.label_15.setScaledContents(True)

        self.verticalLayout_44.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.frame_32 = QFrame(self.widget_8)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_32)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.customerName = QLineEdit(self.frame_32)
        self.customerName.setObjectName(u"customerName")
        font7 = QFont()
        font7.setKerning(False)
        self.customerName.setFont(font7)
        self.customerName.setMouseTracking(True)
        self.customerName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.customerName.setFrame(True)

        self.verticalLayout_45.addWidget(self.customerName)

        self.customerAddress = QLineEdit(self.frame_32)
        self.customerAddress.setObjectName(u"customerAddress")
        self.customerAddress.setFont(font7)
        self.customerAddress.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_45.addWidget(self.customerAddress)

        self.customerPhoneNum = QLineEdit(self.frame_32)
        self.customerPhoneNum.setObjectName(u"customerPhoneNum")
        self.customerPhoneNum.setFont(font7)
        self.customerPhoneNum.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_45.addWidget(self.customerPhoneNum)


        self.verticalLayout_44.addWidget(self.frame_32)

        self.addCustomer = QPushButton(self.widget_8)
        self.addCustomer.setObjectName(u"addCustomer")
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setStrikeOut(False)
        self.addCustomer.setFont(font8)
        self.addCustomer.setCursor(QCursor(Qt.PointingHandCursor))
        self.addCustomer.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_44.addWidget(self.addCustomer, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.widget_8, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_33 = QFrame(self.rightMenu)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color: #879CEB;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_33)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_3)


        self.verticalLayout_43.addWidget(self.frame_33)


        self.horizontalLayout.addWidget(self.rightMenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.ordersMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.customersMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.packagesMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Packages", None))
        self.servicesMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Dishes", None))
        self.dishesMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        self.menuBtn.setText("")
        self.dashBoard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.searchBtn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.aboutBtn.setText("")
        self.packages.setText(QCoreApplication.translate("MainWindow", u"Packages", None))
        self.PackageBtn.setText("")
        self.dishes.setText(QCoreApplication.translate("MainWindow", u"Dishes", None))
        self.dishesBtn.setText("")
        self.services.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        self.servicesBtn.setText("")
        self.orders.setText(QCoreApplication.translate("MainWindow", u"Latest Orders", None))
        self.ordersBtn.setText(QCoreApplication.translate("MainWindow", u"View Orders", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Customers", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Package", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Delivered", None));
        self.customers.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.customersBtn.setText(QCoreApplication.translate("MainWindow", u"View Customers", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        self.menuBtn_1.setText("")
        self.dashBoard_1.setText(QCoreApplication.translate("MainWindow", u"Orders Page", None))
        self.searchBtn_1.setText("")
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.aboutBtn_1.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Orders Page", None))
        self.deleteOrderBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editOrderBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createOrderBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem9 = self.ordersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Customers", None));
        ___qtablewidgetitem10 = self.ordersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Package", None));
        ___qtablewidgetitem11 = self.ordersTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem12 = self.ordersTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem13 = self.ordersTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem14 = self.ordersTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Delivered", None));
        self.menuBtn_2.setText("")
        self.dashBoard_2.setText("")
        self.searchBtn_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.aboutBtn_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Customers Page", None))
        self.deleteCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem15 = self.customersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.customersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.customersTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem18 = self.customersTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        self.menuBtn_3.setText("")
        self.dashBoard_3.setText(QCoreApplication.translate("MainWindow", u"Dishes Page", None))
        self.searchBtn_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.aboutBtn_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dishes Page", None))
        self.deleteDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem19 = self.dishesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem20 = self.dishesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.menuBtn_4.setText("")
        self.dashBoard_4.setText(QCoreApplication.translate("MainWindow", u"Services Page", None))
        self.searchBtn_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.aboutBtn_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Services Page", None))
        self.deleteServiceBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editServiceBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createServiceBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem21 = self.servicesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem22 = self.servicesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.menuBtn_5.setText("")
        self.dashBoard_5.setText(QCoreApplication.translate("MainWindow", u"Packages Page", None))
        self.searchBtn_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.aboutBtn_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Packages Page", None))
        self.deletePackageBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editPackageBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createPackageBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem23 = self.packagesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem24 = self.packagesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem25 = self.packagesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem26 = self.packagesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.iconCloseStudent_5.setText("")
        self.label_15.setText("")
        self.customerName.setText("")
        self.customerName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer Name", None))
        self.customerAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.customerPhoneNum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.addCustomer.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
    # retranslateUi

