# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appDashboardiOscKB.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.Widgets import QCustomSlideMenu
#import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 658)
        MainWindow.setStyleSheet(u"	*{\n"
"	color: #000;\n"
"	border: none;\n"
"	\n"
"	\n"
"QTableWidget::item {\n"
"    text-align: center;\n"
"}	\n"
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
"	border-bottom-left-radi"
                        "us: 10px;\n"
"}\n"
"#homeBtn {\n"
"	background-color: #87CEEB;\n"
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
""
                        "	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#headerFrame, #headerFrame_2, #headerFrame_3, #headerFrame_4, #headerFrame_5, #headerFrame_6{\n"
"\n"
"	background-color: #FFFFFF\n"
"}\n"
"#ordersBtn, #customersBtn {\n"
"	background-color: #879CEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"}")
        MainWindow.setInputMethodHints(Qt.ImhDigitsOnly)
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
        self.packagesMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"resource/package.png", QSize(), QIcon.Normal, QIcon.Off)
        self.packagesMenuBtn.setIcon(icon3)
        self.packagesMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.packagesMenuBtn)

        self.dishesMenuBtn = QPushButton(self.frame_9)
        self.dishesMenuBtn.setObjectName(u"dishesMenuBtn")
        self.dishesMenuBtn.setFont(font1)
        self.dishesMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"resource/dishes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dishesMenuBtn.setIcon(icon4)
        self.dishesMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.dishesMenuBtn)

        self.servicesMenuBtn = QPushButton(self.frame_9)
        self.servicesMenuBtn.setObjectName(u"servicesMenuBtn")
        self.servicesMenuBtn.setFont(font1)
        self.servicesMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"resource/truck.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.servicesMenuBtn.setIcon(icon5)
        self.servicesMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.servicesMenuBtn)


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
        self.homePage.setFont(font1)
        self.homePage.setStyleSheet(u"")
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
        self.ordersTableWidgetDashboard = QTableWidget(self.frame_5)
        if (self.ordersTableWidgetDashboard.columnCount() < 8):
            self.ordersTableWidgetDashboard.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ordersTableWidgetDashboard.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.ordersTableWidgetDashboard.setObjectName(u"ordersTableWidgetDashboard")
        self.ordersTableWidgetDashboard.setMinimumSize(QSize(300, 0))
        self.ordersTableWidgetDashboard.setFont(font1)
        self.ordersTableWidgetDashboard.setStyleSheet(u"background-color: #FFFFFF")

        self.gridLayout.addWidget(self.ordersTableWidgetDashboard, 0, 0, 1, 1)


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
        self.customerTableWidgetDashboard = QTableWidget(self.frame_7)
        if (self.customerTableWidgetDashboard.columnCount() < 4):
            self.customerTableWidgetDashboard.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.customerTableWidgetDashboard.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.customerTableWidgetDashboard.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.customerTableWidgetDashboard.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.customerTableWidgetDashboard.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.customerTableWidgetDashboard.setObjectName(u"customerTableWidgetDashboard")
        self.customerTableWidgetDashboard.setMinimumSize(QSize(300, 0))
        self.customerTableWidgetDashboard.setFont(font1)
        self.customerTableWidgetDashboard.setStyleSheet(u"background-color: #FFFFFF")

        self.horizontalLayout_14.addWidget(self.customerTableWidgetDashboard)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.horizontalLayout_11.addWidget(self.customersCard)


        self.verticalLayout_10.addWidget(self.mainFrame)

        self.mainPages.addWidget(self.homePage)
        self.ordersPage = QWidget()
        self.ordersPage.setObjectName(u"ordersPage")
        self.ordersPage.setFont(font4)
        self.ordersPage.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.ordersSearchBtn = QPushButton(self.searchBar_1)
        self.ordersSearchBtn.setObjectName(u"ordersSearchBtn")
        self.ordersSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ordersSearchBtn.setStyleSheet(u"\n"
"padding: 0;")
        icon10 = QIcon()
        icon10.addFile(u"resource/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ordersSearchBtn.setIcon(icon10)
        self.ordersSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_29.addWidget(self.ordersSearchBtn)

        self.lineEdit_1 = QLineEdit(self.searchBar_1)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setStyleSheet(u"color:black;\n"
"font-size: 9pt;\n"
"font-weight: normal")

        self.horizontalLayout_29.addWidget(self.lineEdit_1)


        self.horizontalLayout_28.addWidget(self.searchBar_1, 0, Qt.AlignLeft|Qt.AlignTop)

        self.refSearchOrder = QPushButton(self.widget_12)
        self.refSearchOrder.setObjectName(u"refSearchOrder")
        self.refSearchOrder.setFont(font4)
        self.refSearchOrder.setCursor(QCursor(Qt.PointingHandCursor))
        self.refSearchOrder.setStyleSheet(u"background-color: #D3D3D3;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"resource/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refSearchOrder.setIcon(icon11)
        self.refSearchOrder.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.refSearchOrder, 0, Qt.AlignLeft)


        self.horizontalLayout_26.addWidget(self.widget_12, 0, Qt.AlignHCenter)

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
        icon12 = QIcon()
        icon12.addFile(u"resource/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteOrderBtn.setIcon(icon12)
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
        icon13 = QIcon()
        icon13.addFile(u"resource/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editOrderBtn.setIcon(icon13)
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
        icon14 = QIcon()
        icon14.addFile(u"resource/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createOrderBtn.setIcon(icon14)
        self.createOrderBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.createOrderBtn, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_13)

        self.ordersTableWidget = QTableWidget(self.frame_12)
        if (self.ordersTableWidget.columnCount() < 8):
            self.ordersTableWidget.setColumnCount(8)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.ordersTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        self.ordersTableWidget.setObjectName(u"ordersTableWidget")
        self.ordersTableWidget.setFont(font1)
        self.ordersTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.ordersTableWidget)


        self.verticalLayout_13.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.mainPages.addWidget(self.ordersPage)
        self.customersPage = QWidget()
        self.customersPage.setObjectName(u"customersPage")
        self.customersPage.setFont(font1)
        self.customersPage.setCursor(QCursor(Qt.PointingHandCursor))
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
        font5 = QFont()
        font5.setPointSize(9)
        self.searchBar_2.setFont(font5)
        self.searchBar_2.setFrameShape(QFrame.StyledPanel)
        self.searchBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.searchBar_2)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 1, 0, 2)
        self.customerSearchBtn = QPushButton(self.searchBar_2)
        self.customerSearchBtn.setObjectName(u"customerSearchBtn")
        self.customerSearchBtn.setStyleSheet(u"padding: 0;")
        self.customerSearchBtn.setIcon(icon10)
        self.customerSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.customerSearchBtn)

        self.customerSearch = QLineEdit(self.searchBar_2)
        self.customerSearch.setObjectName(u"customerSearch")
        self.customerSearch.setStyleSheet(u"color:black;\n"
"font-size: 9pt;\n"
"font-weight: normal")

        self.horizontalLayout_34.addWidget(self.customerSearch)


        self.horizontalLayout_33.addWidget(self.searchBar_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.refSearchCus = QPushButton(self.widget_16)
        self.refSearchCus.setObjectName(u"refSearchCus")
        self.refSearchCus.setFont(font4)
        self.refSearchCus.setCursor(QCursor(Qt.PointingHandCursor))
        self.refSearchCus.setStyleSheet(u"\n"
"	background-color: #D3D3D3;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.refSearchCus.setIcon(icon11)
        self.refSearchCus.setIconSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.refSearchCus, 0, Qt.AlignRight)


        self.horizontalLayout_31.addWidget(self.widget_16, 0, Qt.AlignHCenter)

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
        self.deleteCustomerBtn.setIcon(icon12)
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
        self.editCustomerBtn.setIcon(icon13)
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
        self.createCustomerBtn.setIcon(icon14)
        self.createCustomerBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.createCustomerBtn, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_15)

        self.customersTableWidget = QTableWidget(self.frame_14)
        if (self.customersTableWidget.columnCount() < 4):
            self.customersTableWidget.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.customersTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.customersTableWidget.setObjectName(u"customersTableWidget")
        self.customersTableWidget.setFont(font1)
        self.customersTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.customersTableWidget)


        self.verticalLayout_15.addWidget(self.frame_14)


        self.verticalLayout_17.addWidget(self.widget_14)

        self.mainPages.addWidget(self.customersPage)
        self.dishesPage = QWidget()
        self.dishesPage.setObjectName(u"dishesPage")
        self.dishesPage.setFont(font4)
        self.dishesPage.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.dishesSearchBtn = QPushButton(self.searchBar_3)
        self.dishesSearchBtn.setObjectName(u"dishesSearchBtn")
        self.dishesSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dishesSearchBtn.setStyleSheet(u"\n"
"padding: 0;")
        self.dishesSearchBtn.setIcon(icon10)
        self.dishesSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_39.addWidget(self.dishesSearchBtn)

        self.lineEdit_3 = QLineEdit(self.searchBar_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color:black;\n"
"font-size: 9pt;\n"
"font-weight: normal")

        self.horizontalLayout_39.addWidget(self.lineEdit_3)


        self.horizontalLayout_38.addWidget(self.searchBar_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.refSearchDish = QPushButton(self.widget_20)
        self.refSearchDish.setObjectName(u"refSearchDish")
        self.refSearchDish.setFont(font4)
        self.refSearchDish.setCursor(QCursor(Qt.PointingHandCursor))
        self.refSearchDish.setStyleSheet(u"\n"
"	background-color: #D3D3D3;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.refSearchDish.setIcon(icon11)
        self.refSearchDish.setIconSize(QSize(24, 24))

        self.horizontalLayout_38.addWidget(self.refSearchDish, 0, Qt.AlignLeft)


        self.horizontalLayout_36.addWidget(self.widget_20, 0, Qt.AlignHCenter)

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
"	color: #FFFFFF;")
        self.deleteDishesBtn.setIcon(icon12)
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
        self.editDishesBtn.setIcon(icon13)
        self.editDishesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.editDishesBtn, 0, Qt.AlignRight)

        self.createDishesBtn = QPushButton(self.frame_17)
        self.createDishesBtn.setObjectName(u"createDishesBtn")
        self.createDishesBtn.setFont(font4)
        self.createDishesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createDishesBtn.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.createDishesBtn.setIcon(icon14)
        self.createDishesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.createDishesBtn, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_17)

        self.dishesTableWidget = QTableWidget(self.frame_16)
        if (self.dishesTableWidget.columnCount() < 2):
            self.dishesTableWidget.setColumnCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.dishesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.dishesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        self.dishesTableWidget.setObjectName(u"dishesTableWidget")
        self.dishesTableWidget.setFont(font1)
        self.dishesTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.dishesTableWidget.setStyleSheet(u"text-align: center;\n"
"background-color: #FFFFFF;\n"
"alignment: center;")

        self.verticalLayout_19.addWidget(self.dishesTableWidget)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_20.addWidget(self.widget_18)

        self.mainPages.addWidget(self.dishesPage)
        self.servicesPage = QWidget()
        self.servicesPage.setObjectName(u"servicesPage")
        self.servicesPage.setFont(font4)
        self.servicesPage.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.servicesSearchBtn = QPushButton(self.searchBar_4)
        self.servicesSearchBtn.setObjectName(u"servicesSearchBtn")
        self.servicesSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.servicesSearchBtn.setStyleSheet(u"\n"
"padding: 0;")
        self.servicesSearchBtn.setIcon(icon10)
        self.servicesSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.servicesSearchBtn)

        self.lineEdit_4 = QLineEdit(self.searchBar_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setKerning(True)
        self.lineEdit_4.setFont(font6)
        self.lineEdit_4.setStyleSheet(u"color:black;\n"
"font-size: 9pt;\n"
"font-weight: normal")

        self.horizontalLayout_44.addWidget(self.lineEdit_4)


        self.horizontalLayout_43.addWidget(self.searchBar_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.refSearchService = QPushButton(self.widget_24)
        self.refSearchService.setObjectName(u"refSearchService")
        self.refSearchService.setFont(font4)
        self.refSearchService.setStyleSheet(u"background-color: #D3D3D3;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
"")
        self.refSearchService.setIcon(icon11)
        self.refSearchService.setIconSize(QSize(24, 24))

        self.horizontalLayout_43.addWidget(self.refSearchService, 0, Qt.AlignLeft)


        self.horizontalLayout_41.addWidget(self.widget_24, 0, Qt.AlignHCenter)

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

        self.deleteService = QPushButton(self.frame_19)
        self.deleteService.setObjectName(u"deleteService")
        self.deleteService.setFont(font4)
        self.deleteService.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteService.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.deleteService.setIcon(icon12)
        self.deleteService.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.deleteService)

        self.editService = QPushButton(self.frame_19)
        self.editService.setObjectName(u"editService")
        self.editService.setMaximumSize(QSize(16777215, 16777212))
        self.editService.setFont(font4)
        self.editService.setCursor(QCursor(Qt.PointingHandCursor))
        self.editService.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.editService.setIcon(icon13)
        self.editService.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.editService)

        self.createService = QPushButton(self.frame_19)
        self.createService.setObjectName(u"createService")
        self.createService.setFont(font4)
        self.createService.setCursor(QCursor(Qt.PointingHandCursor))
        self.createService.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")
        self.createService.setIcon(icon14)
        self.createService.setIconSize(QSize(24, 24))

        self.horizontalLayout_19.addWidget(self.createService)


        self.verticalLayout_22.addWidget(self.frame_19)

        self.servicesTableWidget = QTableWidget(self.frame_18)
        if (self.servicesTableWidget.columnCount() < 2):
            self.servicesTableWidget.setColumnCount(2)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.servicesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.servicesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        self.servicesTableWidget.setObjectName(u"servicesTableWidget")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        self.servicesTableWidget.setFont(font7)
        self.servicesTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.servicesTableWidget.horizontalHeader().setDefaultSectionSize(99)

        self.verticalLayout_22.addWidget(self.servicesTableWidget)


        self.verticalLayout_21.addWidget(self.frame_18)


        self.verticalLayout_23.addWidget(self.widget_22)

        self.mainPages.addWidget(self.servicesPage)
        self.addDishesPage = QWidget()
        self.addDishesPage.setObjectName(u"addDishesPage")
        self.verticalLayout_32 = QVBoxLayout(self.addDishesPage)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_39 = QWidget(self.addDishesPage)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setStyleSheet(u"background-color: #FFFFFF")
        self.verticalLayout_30 = QVBoxLayout(self.widget_39)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_7 = QWidget(self.widget_39)
        self.headerFrame_7.setObjectName(u"headerFrame_7")
        self.horizontalLayout_51 = QHBoxLayout(self.headerFrame_7)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_40 = QWidget(self.headerFrame_7)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 6, 0, -1)
        self.backToPackageBtn = QPushButton(self.widget_40)
        self.backToPackageBtn.setObjectName(u"backToPackageBtn")
        self.backToPackageBtn.setMinimumSize(QSize(40, 34))
        self.backToPackageBtn.setMaximumSize(QSize(40, 16777215))
        self.backToPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.backToPackageBtn.setStyleSheet(u"background-color: #879CEB;\n"
"	border-radius: 10px;")
        icon15 = QIcon()
        icon15.addFile(u"resource/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backToPackageBtn.setIcon(icon15)
        self.backToPackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_53.addWidget(self.backToPackageBtn, 0, Qt.AlignVCenter)

        self.dashBoard_6 = QLabel(self.widget_40)
        self.dashBoard_6.setObjectName(u"dashBoard_6")
        self.dashBoard_6.setFont(font3)
        self.dashBoard_6.setStyleSheet(u"color: #87CEEB;")

        self.horizontalLayout_53.addWidget(self.dashBoard_6)


        self.horizontalLayout_51.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.headerFrame_7)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_64 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.searchBar_6 = QFrame(self.widget_41)
        self.searchBar_6.setObjectName(u"searchBar_6")
        self.searchBar_6.setMinimumSize(QSize(160, 0))
        self.searchBar_6.setFrameShape(QFrame.StyledPanel)
        self.searchBar_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.searchBar_6)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 1, 0, 2)

        self.horizontalLayout_64.addWidget(self.searchBar_6, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_51.addWidget(self.widget_41, 0, Qt.AlignHCenter)

        self.widget_42 = QWidget(self.headerFrame_7)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_66 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 5, 9, 0)
        self.aboutBtn_6 = QPushButton(self.widget_42)
        self.aboutBtn_6.setObjectName(u"aboutBtn_6")
        self.aboutBtn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutBtn_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.aboutBtn_6.setIcon(icon7)
        self.aboutBtn_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_66.addWidget(self.aboutBtn_6, 0, Qt.AlignTop)


        self.horizontalLayout_51.addWidget(self.widget_42, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.headerFrame_7)

        self.frame_22 = QFrame(self.widget_39)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-color: #FFFFFF")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_22)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(18, 18, 18, -1)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: #879CEB")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setSpacing(12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_7 = QLabel(self.frame_23)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: #FFFFFF")

        self.horizontalLayout_21.addWidget(self.label_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_6)

        self.add3Dish = QPushButton(self.frame_23)
        self.add3Dish.setObjectName(u"add3Dish")
        self.add3Dish.setFont(font4)
        self.add3Dish.setCursor(QCursor(Qt.PointingHandCursor))
        self.add3Dish.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.add3Dish.setIcon(icon4)
        self.add3Dish.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.add3Dish)

        self.add4Dish = QPushButton(self.frame_23)
        self.add4Dish.setObjectName(u"add4Dish")
        self.add4Dish.setFont(font4)
        self.add4Dish.setCursor(QCursor(Qt.PointingHandCursor))
        self.add4Dish.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.add4Dish.setIcon(icon4)
        self.add4Dish.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.add4Dish)

        self.add5Dish = QPushButton(self.frame_23)
        self.add5Dish.setObjectName(u"add5Dish")
        self.add5Dish.setFont(font4)
        self.add5Dish.setCursor(QCursor(Qt.PointingHandCursor))
        self.add5Dish.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.add5Dish.setIcon(icon4)
        self.add5Dish.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.add5Dish, 0, Qt.AlignRight)


        self.verticalLayout_31.addWidget(self.frame_23)

        self.addCoupleDishTableWidget = QTableWidget(self.frame_22)
        if (self.addCoupleDishTableWidget.columnCount() < 5):
            self.addCoupleDishTableWidget.setColumnCount(5)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.addCoupleDishTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.addCoupleDishTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.addCoupleDishTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.addCoupleDishTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.addCoupleDishTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        self.addCoupleDishTableWidget.setObjectName(u"addCoupleDishTableWidget")
        self.addCoupleDishTableWidget.setFont(font1)
        self.addCoupleDishTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.addCoupleDishTableWidget)


        self.verticalLayout_30.addWidget(self.frame_22)


        self.verticalLayout_32.addWidget(self.widget_39)

        self.mainPages.addWidget(self.addDishesPage)
        self.packagesPage = QWidget()
        self.packagesPage.setObjectName(u"packagesPage")
        self.packagesPage.setFont(font4)
        self.packagesPage.setAutoFillBackground(False)
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
        self.horizontalLayout_47.setContentsMargins(-1, 6, 0, -1)
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
        self.packagesSearchBtn = QPushButton(self.searchBar_5)
        self.packagesSearchBtn.setObjectName(u"packagesSearchBtn")
        self.packagesSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.packagesSearchBtn.setStyleSheet(u"\n"
"padding: 0;")
        self.packagesSearchBtn.setIcon(icon10)
        self.packagesSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_49.addWidget(self.packagesSearchBtn)

        self.lineEdit_5 = QLineEdit(self.searchBar_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color:black;\n"
"font-size: 9pt;\n"
"font-weight: normal")

        self.horizontalLayout_49.addWidget(self.lineEdit_5)


        self.horizontalLayout_48.addWidget(self.searchBar_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.refSearchPack = QPushButton(self.widget_28)
        self.refSearchPack.setObjectName(u"refSearchPack")
        self.refSearchPack.setFont(font4)
        self.refSearchPack.setCursor(QCursor(Qt.PointingHandCursor))
        self.refSearchPack.setStyleSheet(u"background-color: #D3D3D3;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
"")
        self.refSearchPack.setIcon(icon11)
        self.refSearchPack.setIconSize(QSize(24, 24))

        self.horizontalLayout_48.addWidget(self.refSearchPack, 0, Qt.AlignLeft)


        self.horizontalLayout_46.addWidget(self.widget_28, 0, Qt.AlignHCenter)

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

        self.addDishesInPackageBtn = QPushButton(self.frame_21)
        self.addDishesInPackageBtn.setObjectName(u"addDishesInPackageBtn")
        self.addDishesInPackageBtn.setFont(font4)
        self.addDishesInPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addDishesInPackageBtn.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.addDishesInPackageBtn.setIcon(icon4)
        self.addDishesInPackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.addDishesInPackageBtn)

        self.deletePackageBtn = QPushButton(self.frame_21)
        self.deletePackageBtn.setObjectName(u"deletePackageBtn")
        self.deletePackageBtn.setFont(font4)
        self.deletePackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletePackageBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.deletePackageBtn.setIcon(icon12)
        self.deletePackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.deletePackageBtn)

        self.editPackageBtn = QPushButton(self.frame_21)
        self.editPackageBtn.setObjectName(u"editPackageBtn")
        self.editPackageBtn.setMaximumSize(QSize(16777215, 16777212))
        self.editPackageBtn.setFont(font4)
        self.editPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editPackageBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.editPackageBtn.setIcon(icon13)
        self.editPackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.editPackageBtn)

        self.createPackageBtn = QPushButton(self.frame_21)
        self.createPackageBtn.setObjectName(u"createPackageBtn")
        self.createPackageBtn.setFont(font4)
        self.createPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createPackageBtn.setStyleSheet(u"	background-color: #87CEEB;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")
        self.createPackageBtn.setIcon(icon14)
        self.createPackageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.createPackageBtn, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_21)

        self.packagesTableWidget = QTableWidget(self.frame_20)
        if (self.packagesTableWidget.columnCount() < 5):
            self.packagesTableWidget.setColumnCount(5)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.packagesTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        self.packagesTableWidget.setObjectName(u"packagesTableWidget")
        self.packagesTableWidget.setFont(font1)
        self.packagesTableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.packagesTableWidget.setAutoFillBackground(False)
        self.packagesTableWidget.setStyleSheet(u"QTableWidget::item {\n"
"    text-align: center;\n"
"}\n"
"gridline-color: #879CEB;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.packagesTableWidget.setGridStyle(Qt.SolidLine)

        self.verticalLayout_25.addWidget(self.packagesTableWidget)


        self.verticalLayout_24.addWidget(self.frame_20)


        self.verticalLayout_26.addWidget(self.widget_26)

        self.mainPages.addWidget(self.packagesPage)

        self.verticalLayout.addWidget(self.mainPages)


        self.horizontalLayout.addWidget(self.mainBody)

        self.rightMenu_2 = QCustomSlideMenu(self.centralwidget)
        self.rightMenu_2.setObjectName(u"rightMenu_2")
        self.rightMenu_2.setMinimumSize(QSize(0, 658))
        self.rightMenu_2.setMaximumSize(QSize(0, 16777215))
        self.rightMenu_2.setCursor(QCursor(Qt.ArrowCursor))
        self.rightMenu_2.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_51 = QVBoxLayout(self.rightMenu_2)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(6, 0, 0, 0)
        self.widget_30 = QWidget(self.rightMenu_2)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(200, 350))
        self.widget_30.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_52 = QVBoxLayout(self.widget_30)
        self.verticalLayout_52.setSpacing(9)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, -1, -1, 0)
        self.frame_38 = QFrame(self.widget_30)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy1)
        self.frame_38.setStyleSheet(u"background-color: #879CEB;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.closeCreateOrder = QPushButton(self.frame_38)
        self.closeCreateOrder.setObjectName(u"closeCreateOrder")
        icon16 = QIcon()
        icon16.addFile(u"../SSIS v@/Resource/closeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCreateOrder.setIcon(icon16)
        self.closeCreateOrder.setIconSize(QSize(24, 24))

        self.horizontalLayout_54.addWidget(self.closeCreateOrder, 0, Qt.AlignRight)


        self.verticalLayout_52.addWidget(self.frame_38)

        self.label_17 = QLabel(self.widget_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(70, 70))
        self.label_17.setMaximumSize(QSize(70, 70))
        self.label_17.setPixmap(QPixmap(u"resource/orders.png"))
        self.label_17.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.frame_39 = QFrame(self.widget_30)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_39)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.customerComboBox = QComboBox(self.frame_39)
        self.customerComboBox.setObjectName(u"customerComboBox")
        self.customerComboBox.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_27.addWidget(self.customerComboBox)

        self.cusIDinOrders = QLineEdit(self.frame_39)
        self.cusIDinOrders.setObjectName(u"cusIDinOrders")
        font8 = QFont()
        font8.setKerning(False)
        self.cusIDinOrders.setFont(font8)
        self.cusIDinOrders.setMouseTracking(True)
        self.cusIDinOrders.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.cusIDinOrders.setFrame(True)
        self.cusIDinOrders.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.cusIDinOrders)

        self.packComboBox = QComboBox(self.frame_39)
        self.packComboBox.setObjectName(u"packComboBox")
        self.packComboBox.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_27.addWidget(self.packComboBox)

        self.packIDinOrders = QLineEdit(self.frame_39)
        self.packIDinOrders.setObjectName(u"packIDinOrders")
        self.packIDinOrders.setFont(font8)
        self.packIDinOrders.setMouseTracking(True)
        self.packIDinOrders.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.packIDinOrders.setFrame(True)
        self.packIDinOrders.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.packIDinOrders)

        self.packPriceInOrder = QLineEdit(self.frame_39)
        self.packPriceInOrder.setObjectName(u"packPriceInOrder")
        self.packPriceInOrder.setFont(font8)
        self.packPriceInOrder.setMouseTracking(True)
        self.packPriceInOrder.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.packPriceInOrder.setFrame(True)
        self.packPriceInOrder.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.packPriceInOrder)


        self.verticalLayout_52.addWidget(self.frame_39)


        self.verticalLayout_51.addWidget(self.widget_30)

        self.frame_40 = QFrame(self.rightMenu_2)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 250))
        self.frame_40.setStyleSheet(u"background-color: #879CEB;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_40)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 20, 0, 0)
        self.addOrder = QPushButton(self.frame_40)
        self.addOrder.setObjectName(u"addOrder")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setStrikeOut(False)
        self.addOrder.setFont(font9)
        self.addOrder.setCursor(QCursor(Qt.PointingHandCursor))
        self.addOrder.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_54.addWidget(self.addOrder, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_7)

        self.verticalSpacer_8 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_8)


        self.verticalLayout_51.addWidget(self.frame_40)


        self.horizontalLayout.addWidget(self.rightMenu_2)

        self.rightMenu = QCustomSlideMenu(self.centralwidget)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(0, 16777215))
        self.rightMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_43 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(6, 0, 0, 0)
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
        sizePolicy1.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy1)
        self.frame_34.setStyleSheet(u"background-color: #879CEB;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.closeAddCustomer = QPushButton(self.frame_34)
        self.closeAddCustomer.setObjectName(u"closeAddCustomer")
        self.closeAddCustomer.setIcon(icon16)
        self.closeAddCustomer.setIconSize(QSize(24, 24))

        self.horizontalLayout_52.addWidget(self.closeAddCustomer, 0, Qt.AlignRight)


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
        self.customerName.setFont(font8)
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
        self.customerAddress.setFont(font8)
        self.customerAddress.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_45.addWidget(self.customerAddress)

        self.customerPhoneNum = QLineEdit(self.frame_32)
        self.customerPhoneNum.setObjectName(u"customerPhoneNum")
        self.customerPhoneNum.setFont(font8)
        self.customerPhoneNum.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_45.addWidget(self.customerPhoneNum)


        self.verticalLayout_44.addWidget(self.frame_32)

        self.addCustomer = QPushButton(self.widget_8)
        self.addCustomer.setObjectName(u"addCustomer")
        self.addCustomer.setFont(font9)
        self.addCustomer.setCursor(QCursor(Qt.PointingHandCursor))
        self.addCustomer.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_44.addWidget(self.addCustomer, 0, Qt.AlignHCenter)


        self.verticalLayout_43.addWidget(self.widget_8)

        self.frame_33 = QFrame(self.rightMenu)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color: #879CEB;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_33)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_3)


        self.verticalLayout_43.addWidget(self.frame_33)


        self.horizontalLayout.addWidget(self.rightMenu)

        self.add3DishesMenu = QCustomSlideMenu(self.centralwidget)
        self.add3DishesMenu.setObjectName(u"add3DishesMenu")
        self.add3DishesMenu.setMinimumSize(QSize(0, 658))
        self.add3DishesMenu.setMaximumSize(QSize(0, 16777215))
        self.add3DishesMenu.setCursor(QCursor(Qt.ArrowCursor))
        self.add3DishesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_86 = QVBoxLayout(self.add3DishesMenu)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(6, 0, 0, 0)
        self.widget_43 = QWidget(self.add3DishesMenu)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMinimumSize(QSize(200, 350))
        self.widget_43.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_87 = QVBoxLayout(self.widget_43)
        self.verticalLayout_87.setSpacing(9)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(-1, -1, -1, 0)
        self.frame_67 = QFrame(self.widget_43)
        self.frame_67.setObjectName(u"frame_67")
        sizePolicy1.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy1)
        self.frame_67.setStyleSheet(u"background-color: #879CEB;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.closeAdd3DishMenu = QPushButton(self.frame_67)
        self.closeAdd3DishMenu.setObjectName(u"closeAdd3DishMenu")
        self.closeAdd3DishMenu.setIcon(icon16)
        self.closeAdd3DishMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_67.addWidget(self.closeAdd3DishMenu, 0, Qt.AlignRight)


        self.verticalLayout_87.addWidget(self.frame_67)

        self.label_27 = QLabel(self.widget_43)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(70, 70))
        self.label_27.setMaximumSize(QSize(70, 70))
        self.label_27.setPixmap(QPixmap(u"resource/package.png"))
        self.label_27.setScaledContents(True)

        self.verticalLayout_87.addWidget(self.label_27, 0, Qt.AlignHCenter)

        self.frame_68 = QFrame(self.widget_43)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_68)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.dish3PackageName = QLineEdit(self.frame_68)
        self.dish3PackageName.setObjectName(u"dish3PackageName")
        self.dish3PackageName.setFont(font8)
        self.dish3PackageName.setMouseTracking(True)
        self.dish3PackageName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.dish3PackageName.setFrame(True)
        self.dish3PackageName.setReadOnly(False)

        self.verticalLayout_33.addWidget(self.dish3PackageName)

        self.dish3Name1 = QComboBox(self.frame_68)
        self.dish3Name1.setObjectName(u"dish3Name1")
        self.dish3Name1.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_33.addWidget(self.dish3Name1)

        self.dish3Name2 = QComboBox(self.frame_68)
        self.dish3Name2.setObjectName(u"dish3Name2")
        self.dish3Name2.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_33.addWidget(self.dish3Name2)

        self.dish3Name3 = QComboBox(self.frame_68)
        self.dish3Name3.setObjectName(u"dish3Name3")
        self.dish3Name3.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_33.addWidget(self.dish3Name3)


        self.verticalLayout_87.addWidget(self.frame_68)


        self.verticalLayout_86.addWidget(self.widget_43)

        self.frame_69 = QFrame(self.add3DishesMenu)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMaximumSize(QSize(16777215, 250))
        self.frame_69.setStyleSheet(u"background-color: #879CEB;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_69)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 20, 0, 0)
        self.add3DishBtn = QPushButton(self.frame_69)
        self.add3DishBtn.setObjectName(u"add3DishBtn")
        self.add3DishBtn.setFont(font9)
        self.add3DishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add3DishBtn.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_88.addWidget(self.add3DishBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_31 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacer_31)

        self.verticalSpacer_32 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_88.addItem(self.verticalSpacer_32)


        self.verticalLayout_86.addWidget(self.frame_69)


        self.horizontalLayout.addWidget(self.add3DishesMenu)

        self.addPackagesMenu = QCustomSlideMenu(self.centralwidget)
        self.addPackagesMenu.setObjectName(u"addPackagesMenu")
        self.addPackagesMenu.setMinimumSize(QSize(0, 658))
        self.addPackagesMenu.setMaximumSize(QSize(0, 16777215))
        self.addPackagesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_56 = QVBoxLayout(self.addPackagesMenu)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(6, 0, 0, 0)
        self.widget_36 = QWidget(self.addPackagesMenu)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMinimumSize(QSize(200, 350))
        self.widget_36.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_77 = QVBoxLayout(self.widget_36)
        self.verticalLayout_77.setSpacing(9)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(-1, -1, -1, 0)
        self.frame_42 = QFrame(self.widget_36)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy1.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy1)
        self.frame_42.setStyleSheet(u"background-color: #879CEB;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.closeAddPackage = QPushButton(self.frame_42)
        self.closeAddPackage.setObjectName(u"closeAddPackage")
        self.closeAddPackage.setIcon(icon16)
        self.closeAddPackage.setIconSize(QSize(24, 24))

        self.horizontalLayout_55.addWidget(self.closeAddPackage, 0, Qt.AlignRight)


        self.verticalLayout_77.addWidget(self.frame_42)

        self.label_18 = QLabel(self.widget_36)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(70, 70))
        self.label_18.setMaximumSize(QSize(70, 70))
        self.label_18.setPixmap(QPixmap(u"../SSIS v@/Resource/addUser.png"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_77.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.frame_43 = QFrame(self.widget_36)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_43)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.addPackageName = QLineEdit(self.frame_43)
        self.addPackageName.setObjectName(u"addPackageName")
        self.addPackageName.setFont(font8)
        self.addPackageName.setMouseTracking(True)
        self.addPackageName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.addPackageName.setFrame(True)
        self.addPackageName.setReadOnly(False)

        self.verticalLayout_28.addWidget(self.addPackageName)

        self.addPackagePrice = QLineEdit(self.frame_43)
        self.addPackagePrice.setObjectName(u"addPackagePrice")
        self.addPackagePrice.setFont(font8)
        self.addPackagePrice.setMouseTracking(True)
        self.addPackagePrice.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.addPackagePrice.setFrame(True)
        self.addPackagePrice.setReadOnly(False)

        self.verticalLayout_28.addWidget(self.addPackagePrice)

        self.addPackagePax = QLineEdit(self.frame_43)
        self.addPackagePax.setObjectName(u"addPackagePax")
        self.addPackagePax.setFont(font8)
        self.addPackagePax.setMouseTracking(True)
        self.addPackagePax.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.addPackagePax.setFrame(True)
        self.addPackagePax.setReadOnly(False)

        self.verticalLayout_28.addWidget(self.addPackagePax)


        self.verticalLayout_77.addWidget(self.frame_43)


        self.verticalLayout_56.addWidget(self.widget_36)

        self.frame_60 = QFrame(self.addPackagesMenu)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 250))
        self.frame_60.setStyleSheet(u"background-color: #879CEB;")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_60)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 20, 0, 0)
        self.addPackageBtn = QPushButton(self.frame_60)
        self.addPackageBtn.setObjectName(u"addPackageBtn")
        self.addPackageBtn.setFont(font9)
        self.addPackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addPackageBtn.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_78.addWidget(self.addPackageBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_24 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_78.addItem(self.verticalSpacer_24)

        self.verticalSpacer_28 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_78.addItem(self.verticalSpacer_28)


        self.verticalLayout_56.addWidget(self.frame_60)


        self.horizontalLayout.addWidget(self.addPackagesMenu)

        self.add4DishesMenu = QCustomSlideMenu(self.centralwidget)
        self.add4DishesMenu.setObjectName(u"add4DishesMenu")
        self.add4DishesMenu.setMinimumSize(QSize(0, 658))
        self.add4DishesMenu.setMaximumSize(QSize(0, 16777215))
        self.add4DishesMenu.setCursor(QCursor(Qt.ArrowCursor))
        self.add4DishesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_89 = QVBoxLayout(self.add4DishesMenu)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(6, 0, 0, 0)
        self.widget_45 = QWidget(self.add4DishesMenu)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(200, 350))
        self.widget_45.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_90 = QVBoxLayout(self.widget_45)
        self.verticalLayout_90.setSpacing(9)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(-1, -1, -1, 0)
        self.frame_70 = QFrame(self.widget_45)
        self.frame_70.setObjectName(u"frame_70")
        sizePolicy1.setHeightForWidth(self.frame_70.sizePolicy().hasHeightForWidth())
        self.frame_70.setSizePolicy(sizePolicy1)
        self.frame_70.setStyleSheet(u"background-color: #879CEB;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.closeAdd4DishMenu = QPushButton(self.frame_70)
        self.closeAdd4DishMenu.setObjectName(u"closeAdd4DishMenu")
        self.closeAdd4DishMenu.setIcon(icon16)
        self.closeAdd4DishMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_68.addWidget(self.closeAdd4DishMenu, 0, Qt.AlignRight)


        self.verticalLayout_90.addWidget(self.frame_70)

        self.label_28 = QLabel(self.widget_45)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(70, 70))
        self.label_28.setMaximumSize(QSize(70, 70))
        self.label_28.setPixmap(QPixmap(u"resource/package.svg"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_90.addWidget(self.label_28, 0, Qt.AlignHCenter)

        self.frame_71 = QFrame(self.widget_45)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_71)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.dish4PackageName = QLineEdit(self.frame_71)
        self.dish4PackageName.setObjectName(u"dish4PackageName")
        self.dish4PackageName.setFont(font8)
        self.dish4PackageName.setMouseTracking(True)
        self.dish4PackageName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.dish4PackageName.setFrame(True)
        self.dish4PackageName.setReadOnly(False)

        self.verticalLayout_34.addWidget(self.dish4PackageName)

        self.dish4Name1 = QComboBox(self.frame_71)
        self.dish4Name1.setObjectName(u"dish4Name1")
        self.dish4Name1.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_34.addWidget(self.dish4Name1)

        self.dish4Name2 = QComboBox(self.frame_71)
        self.dish4Name2.setObjectName(u"dish4Name2")
        self.dish4Name2.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_34.addWidget(self.dish4Name2)

        self.dish4Name3 = QComboBox(self.frame_71)
        self.dish4Name3.setObjectName(u"dish4Name3")
        self.dish4Name3.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_34.addWidget(self.dish4Name3)

        self.dish4Name4 = QComboBox(self.frame_71)
        self.dish4Name4.setObjectName(u"dish4Name4")
        self.dish4Name4.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_34.addWidget(self.dish4Name4)


        self.verticalLayout_90.addWidget(self.frame_71)


        self.verticalLayout_89.addWidget(self.widget_45)

        self.frame_72 = QFrame(self.add4DishesMenu)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMaximumSize(QSize(16777215, 250))
        self.frame_72.setStyleSheet(u"background-color: #879CEB;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_72)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 20, 0, 0)
        self.add4DishBtn = QPushButton(self.frame_72)
        self.add4DishBtn.setObjectName(u"add4DishBtn")
        self.add4DishBtn.setFont(font9)
        self.add4DishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add4DishBtn.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_91.addWidget(self.add4DishBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_33 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_91.addItem(self.verticalSpacer_33)

        self.verticalSpacer_34 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_91.addItem(self.verticalSpacer_34)


        self.verticalLayout_89.addWidget(self.frame_72)


        self.horizontalLayout.addWidget(self.add4DishesMenu)

        self.updateCustomerRightMenu = QCustomSlideMenu(self.centralwidget)
        self.updateCustomerRightMenu.setObjectName(u"updateCustomerRightMenu")
        self.updateCustomerRightMenu.setMinimumSize(QSize(0, 0))
        self.updateCustomerRightMenu.setMaximumSize(QSize(0, 16777215))
        self.updateCustomerRightMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_63 = QVBoxLayout(self.updateCustomerRightMenu)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(6, 0, 0, 0)
        self.widget_32 = QWidget(self.updateCustomerRightMenu)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(200, 350))
        self.widget_32.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_64 = QVBoxLayout(self.widget_32)
        self.verticalLayout_64.setSpacing(9)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(-1, -1, -1, 0)
        self.frame_48 = QFrame(self.widget_32)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy1.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy1)
        self.frame_48.setStyleSheet(u"background-color: #879CEB;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.iconCloseUpdateCustomer = QPushButton(self.frame_48)
        self.iconCloseUpdateCustomer.setObjectName(u"iconCloseUpdateCustomer")
        self.iconCloseUpdateCustomer.setIcon(icon16)
        self.iconCloseUpdateCustomer.setIconSize(QSize(24, 24))

        self.horizontalLayout_58.addWidget(self.iconCloseUpdateCustomer, 0, Qt.AlignRight)


        self.verticalLayout_64.addWidget(self.frame_48)

        self.label_21 = QLabel(self.widget_32)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 70))
        self.label_21.setMaximumSize(QSize(70, 70))
        self.label_21.setPixmap(QPixmap(u"../SSIS v@/Resource/addUser.png"))
        self.label_21.setScaledContents(True)

        self.verticalLayout_64.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.frame_49 = QFrame(self.widget_32)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_49)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(-1, 0, -1, 0)
        self.customerIDUpdate = QLineEdit(self.frame_49)
        self.customerIDUpdate.setObjectName(u"customerIDUpdate")
        self.customerIDUpdate.setFont(font8)
        self.customerIDUpdate.setMouseTracking(True)
        self.customerIDUpdate.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.customerIDUpdate.setFrame(True)

        self.verticalLayout_65.addWidget(self.customerIDUpdate)

        self.customerNameUpdate = QLineEdit(self.frame_49)
        self.customerNameUpdate.setObjectName(u"customerNameUpdate")
        self.customerNameUpdate.setFont(font8)
        self.customerNameUpdate.setMouseTracking(True)
        self.customerNameUpdate.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.customerNameUpdate.setFrame(True)

        self.verticalLayout_65.addWidget(self.customerNameUpdate)

        self.customerPhoneNumUpdate = QLineEdit(self.frame_49)
        self.customerPhoneNumUpdate.setObjectName(u"customerPhoneNumUpdate")
        self.customerPhoneNumUpdate.setFont(font8)
        self.customerPhoneNumUpdate.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.customerPhoneNumUpdate.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_65.addWidget(self.customerPhoneNumUpdate)

        self.customerAddressUpdate = QLineEdit(self.frame_49)
        self.customerAddressUpdate.setObjectName(u"customerAddressUpdate")
        self.customerAddressUpdate.setFont(font8)
        self.customerAddressUpdate.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_65.addWidget(self.customerAddressUpdate)


        self.verticalLayout_64.addWidget(self.frame_49)

        self.updateCustomerBtn = QPushButton(self.widget_32)
        self.updateCustomerBtn.setObjectName(u"updateCustomerBtn")
        self.updateCustomerBtn.setFont(font9)
        self.updateCustomerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateCustomerBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.verticalLayout_64.addWidget(self.updateCustomerBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_63.addWidget(self.widget_32)

        self.frame_50 = QFrame(self.updateCustomerRightMenu)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"background-color: #879CEB;")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_50)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_66.addItem(self.verticalSpacer_11)

        self.verticalSpacer_12 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_66.addItem(self.verticalSpacer_12)


        self.verticalLayout_63.addWidget(self.frame_50)


        self.horizontalLayout.addWidget(self.updateCustomerRightMenu)

        self.add5DishesMenu = QCustomSlideMenu(self.centralwidget)
        self.add5DishesMenu.setObjectName(u"add5DishesMenu")
        self.add5DishesMenu.setMinimumSize(QSize(0, 658))
        self.add5DishesMenu.setMaximumSize(QSize(0, 16777215))
        self.add5DishesMenu.setCursor(QCursor(Qt.ArrowCursor))
        self.add5DishesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_92 = QVBoxLayout(self.add5DishesMenu)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(6, 0, 0, 0)
        self.widget_46 = QWidget(self.add5DishesMenu)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(200, 350))
        self.widget_46.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_93 = QVBoxLayout(self.widget_46)
        self.verticalLayout_93.setSpacing(9)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(-1, -1, -1, 0)
        self.frame_73 = QFrame(self.widget_46)
        self.frame_73.setObjectName(u"frame_73")
        sizePolicy1.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy1)
        self.frame_73.setStyleSheet(u"background-color: #879CEB;")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.closeAdd5DishMenu = QPushButton(self.frame_73)
        self.closeAdd5DishMenu.setObjectName(u"closeAdd5DishMenu")
        self.closeAdd5DishMenu.setIcon(icon16)
        self.closeAdd5DishMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_69.addWidget(self.closeAdd5DishMenu, 0, Qt.AlignRight)


        self.verticalLayout_93.addWidget(self.frame_73)

        self.label_29 = QLabel(self.widget_46)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(70, 70))
        self.label_29.setMaximumSize(QSize(70, 70))
        self.label_29.setPixmap(QPixmap(u"resource/package.png"))
        self.label_29.setScaledContents(True)

        self.verticalLayout_93.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.frame_74 = QFrame(self.widget_46)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_74)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.dish5PackageName = QLineEdit(self.frame_74)
        self.dish5PackageName.setObjectName(u"dish5PackageName")
        self.dish5PackageName.setFont(font8)
        self.dish5PackageName.setMouseTracking(True)
        self.dish5PackageName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.dish5PackageName.setFrame(True)
        self.dish5PackageName.setReadOnly(False)

        self.verticalLayout_35.addWidget(self.dish5PackageName)

        self.dish5Name1 = QComboBox(self.frame_74)
        self.dish5Name1.setObjectName(u"dish5Name1")
        self.dish5Name1.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_35.addWidget(self.dish5Name1)

        self.dish5Name2 = QComboBox(self.frame_74)
        self.dish5Name2.setObjectName(u"dish5Name2")
        self.dish5Name2.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_35.addWidget(self.dish5Name2)

        self.dish5Name3 = QComboBox(self.frame_74)
        self.dish5Name3.setObjectName(u"dish5Name3")
        self.dish5Name3.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_35.addWidget(self.dish5Name3)

        self.dish5Name4 = QComboBox(self.frame_74)
        self.dish5Name4.setObjectName(u"dish5Name4")
        self.dish5Name4.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_35.addWidget(self.dish5Name4)

        self.dish5Name5 = QComboBox(self.frame_74)
        self.dish5Name5.setObjectName(u"dish5Name5")
        self.dish5Name5.setStyleSheet(u"\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	color: #808080;\n"
"")

        self.verticalLayout_35.addWidget(self.dish5Name5)


        self.verticalLayout_93.addWidget(self.frame_74)


        self.verticalLayout_92.addWidget(self.widget_46)

        self.frame_75 = QFrame(self.add5DishesMenu)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMaximumSize(QSize(16777215, 250))
        self.frame_75.setStyleSheet(u"background-color: #879CEB;")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_75)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 20, 0, 0)
        self.add5DishBtn = QPushButton(self.frame_75)
        self.add5DishBtn.setObjectName(u"add5DishBtn")
        self.add5DishBtn.setFont(font9)
        self.add5DishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add5DishBtn.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_94.addWidget(self.add5DishBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_35 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_94.addItem(self.verticalSpacer_35)

        self.verticalSpacer_36 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_94.addItem(self.verticalSpacer_36)


        self.verticalLayout_92.addWidget(self.frame_75)


        self.horizontalLayout.addWidget(self.add5DishesMenu)

        self.updatePackagesMenu = QCustomSlideMenu(self.centralwidget)
        self.updatePackagesMenu.setObjectName(u"updatePackagesMenu")
        self.updatePackagesMenu.setMinimumSize(QSize(0, 658))
        self.updatePackagesMenu.setMaximumSize(QSize(0, 16777215))
        self.updatePackagesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_83 = QVBoxLayout(self.updatePackagesMenu)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(6, 0, 0, 0)
        self.widget_38 = QWidget(self.updatePackagesMenu)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMinimumSize(QSize(200, 350))
        self.widget_38.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_84 = QVBoxLayout(self.widget_38)
        self.verticalLayout_84.setSpacing(9)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(-1, -1, -1, 0)
        self.frame_61 = QFrame(self.widget_38)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy1.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy1)
        self.frame_61.setStyleSheet(u"background-color: #879CEB;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.closeUpdatePackagesMenu = QPushButton(self.frame_61)
        self.closeUpdatePackagesMenu.setObjectName(u"closeUpdatePackagesMenu")
        self.closeUpdatePackagesMenu.setIcon(icon16)
        self.closeUpdatePackagesMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_62.addWidget(self.closeUpdatePackagesMenu, 0, Qt.AlignRight)


        self.verticalLayout_84.addWidget(self.frame_61)

        self.label_24 = QLabel(self.widget_38)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(70, 70))
        self.label_24.setMaximumSize(QSize(70, 70))
        self.label_24.setPixmap(QPixmap(u"resource/package.png"))
        self.label_24.setScaledContents(True)

        self.verticalLayout_84.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.frame_65 = QFrame(self.widget_38)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_65)
        self.verticalLayout_29.setSpacing(16)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.updatePackageID = QLineEdit(self.frame_65)
        self.updatePackageID.setObjectName(u"updatePackageID")
        self.updatePackageID.setFont(font8)
        self.updatePackageID.setMouseTracking(True)
        self.updatePackageID.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackageID.setFrame(True)
        self.updatePackageID.setReadOnly(False)

        self.verticalLayout_29.addWidget(self.updatePackageID)

        self.updatePackageName = QLineEdit(self.frame_65)
        self.updatePackageName.setObjectName(u"updatePackageName")
        self.updatePackageName.setFont(font8)
        self.updatePackageName.setMouseTracking(True)
        self.updatePackageName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackageName.setFrame(True)
        self.updatePackageName.setReadOnly(False)

        self.verticalLayout_29.addWidget(self.updatePackageName)

        self.updatePackagePrice = QLineEdit(self.frame_65)
        self.updatePackagePrice.setObjectName(u"updatePackagePrice")
        self.updatePackagePrice.setFont(font8)
        self.updatePackagePrice.setMouseTracking(True)
        self.updatePackagePrice.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackagePrice.setFrame(True)
        self.updatePackagePrice.setReadOnly(False)

        self.verticalLayout_29.addWidget(self.updatePackagePrice)

        self.updatePackagePax = QLineEdit(self.frame_65)
        self.updatePackagePax.setObjectName(u"updatePackagePax")
        self.updatePackagePax.setFont(font8)
        self.updatePackagePax.setMouseTracking(True)
        self.updatePackagePax.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackagePax.setFrame(True)
        self.updatePackagePax.setReadOnly(False)

        self.verticalLayout_29.addWidget(self.updatePackagePax)


        self.verticalLayout_84.addWidget(self.frame_65)


        self.verticalLayout_83.addWidget(self.widget_38)

        self.frame_66 = QFrame(self.updatePackagesMenu)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(16777215, 250))
        self.frame_66.setStyleSheet(u"background-color: #879CEB;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_66)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 20, 0, 0)
        self.updatePackageBtn = QPushButton(self.frame_66)
        self.updatePackageBtn.setObjectName(u"updatePackageBtn")
        self.updatePackageBtn.setFont(font9)
        self.updatePackageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updatePackageBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")

        self.verticalLayout_85.addWidget(self.updatePackageBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_29 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_85.addItem(self.verticalSpacer_29)

        self.verticalSpacer_30 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_85.addItem(self.verticalSpacer_30)


        self.verticalLayout_83.addWidget(self.frame_66)


        self.horizontalLayout.addWidget(self.updatePackagesMenu)

        self.addDishesMenu = QCustomSlideMenu(self.centralwidget)
        self.addDishesMenu.setObjectName(u"addDishesMenu")
        self.addDishesMenu.setMinimumSize(QSize(0, 658))
        self.addDishesMenu.setMaximumSize(QSize(0, 16777215))
        self.addDishesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_49 = QVBoxLayout(self.addDishesMenu)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(6, 0, 0, 0)
        self.widget_9 = QWidget(self.addDishesMenu)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(200, 350))
        self.widget_9.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_50 = QVBoxLayout(self.widget_9)
        self.verticalLayout_50.setSpacing(24)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(-1, -1, -1, 0)
        self.frame_37 = QFrame(self.widget_9)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy1.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy1)
        self.frame_37.setStyleSheet(u"background-color: #879CEB;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.closeAddDishes = QPushButton(self.frame_37)
        self.closeAddDishes.setObjectName(u"closeAddDishes")
        self.closeAddDishes.setIcon(icon16)
        self.closeAddDishes.setIconSize(QSize(24, 24))

        self.horizontalLayout_56.addWidget(self.closeAddDishes, 0, Qt.AlignRight)


        self.verticalLayout_50.addWidget(self.frame_37)

        self.label_19 = QLabel(self.widget_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(70, 70))
        self.label_19.setMaximumSize(QSize(70, 70))
        self.label_19.setPixmap(QPixmap(u"resource/dishes.png"))
        self.label_19.setScaledContents(True)

        self.verticalLayout_50.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.frame_44 = QFrame(self.widget_9)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_44)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(-1, 0, -1, 0)
        self.dishesName = QLineEdit(self.frame_44)
        self.dishesName.setObjectName(u"dishesName")
        self.dishesName.setFont(font8)
        self.dishesName.setMouseTracking(True)
        self.dishesName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.dishesName.setFrame(True)

        self.verticalLayout_57.addWidget(self.dishesName)


        self.verticalLayout_50.addWidget(self.frame_44)

        self.addDishes = QPushButton(self.widget_9)
        self.addDishes.setObjectName(u"addDishes")
        self.addDishes.setFont(font9)
        self.addDishes.setCursor(QCursor(Qt.PointingHandCursor))
        self.addDishes.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_50.addWidget(self.addDishes, 0, Qt.AlignHCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_50.addItem(self.verticalSpacer_16)


        self.verticalLayout_49.addWidget(self.widget_9)

        self.frame_45 = QFrame(self.addDishesMenu)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"background-color: #879CEB;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_45)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_5)

        self.verticalSpacer_6 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_6)


        self.verticalLayout_49.addWidget(self.frame_45)


        self.horizontalLayout.addWidget(self.addDishesMenu)

        self.customerDeleteRightMenu = QCustomSlideMenu(self.centralwidget)
        self.customerDeleteRightMenu.setObjectName(u"customerDeleteRightMenu")
        self.customerDeleteRightMenu.setMinimumSize(QSize(0, 0))
        self.customerDeleteRightMenu.setMaximumSize(QSize(0, 16777215))
        self.customerDeleteRightMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_69 = QVBoxLayout(self.customerDeleteRightMenu)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(6, 0, 0, 0)
        self.widget_37 = QWidget(self.customerDeleteRightMenu)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMinimumSize(QSize(200, 350))
        self.widget_37.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_70 = QVBoxLayout(self.widget_37)
        self.verticalLayout_70.setSpacing(9)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(-1, -1, -1, 0)
        self.frame_53 = QFrame(self.widget_37)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy1.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy1)
        self.frame_53.setStyleSheet(u"background-color: #879CEB;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.closeDeleteCustomer = QPushButton(self.frame_53)
        self.closeDeleteCustomer.setObjectName(u"closeDeleteCustomer")
        self.closeDeleteCustomer.setIcon(icon16)
        self.closeDeleteCustomer.setIconSize(QSize(24, 24))

        self.horizontalLayout_60.addWidget(self.closeDeleteCustomer, 0, Qt.AlignRight)


        self.verticalLayout_70.addWidget(self.frame_53)

        self.label_26 = QLabel(self.widget_37)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(70, 70))
        self.label_26.setMaximumSize(QSize(70, 70))
        self.label_26.setPixmap(QPixmap(u"../SSIS v@/Resource/addUser.png"))
        self.label_26.setScaledContents(True)

        self.verticalLayout_70.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.frame_54 = QFrame(self.widget_37)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_54)
        self.verticalLayout_71.setSpacing(30)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(-1, 30, -1, 0)
        self.deleteCustomerLineEdit = QLineEdit(self.frame_54)
        self.deleteCustomerLineEdit.setObjectName(u"deleteCustomerLineEdit")
        self.deleteCustomerLineEdit.setFont(font8)
        self.deleteCustomerLineEdit.setMouseTracking(True)
        self.deleteCustomerLineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.deleteCustomerLineEdit.setFrame(True)

        self.verticalLayout_71.addWidget(self.deleteCustomerLineEdit)

        self.deleteCustomerBtn_2 = QPushButton(self.frame_54)
        self.deleteCustomerBtn_2.setObjectName(u"deleteCustomerBtn_2")
        self.deleteCustomerBtn_2.setFont(font9)
        self.deleteCustomerBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteCustomerBtn_2.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.verticalLayout_71.addWidget(self.deleteCustomerBtn_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_71.addItem(self.verticalSpacer_15)


        self.verticalLayout_70.addWidget(self.frame_54)


        self.verticalLayout_69.addWidget(self.widget_37)

        self.frame_55 = QFrame(self.customerDeleteRightMenu)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"background-color: #879CEB;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_55)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_13)

        self.verticalSpacer_14 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_14)


        self.verticalLayout_69.addWidget(self.frame_55)


        self.horizontalLayout.addWidget(self.customerDeleteRightMenu)

        self.addServicesMenu = QCustomSlideMenu(self.centralwidget)
        self.addServicesMenu.setObjectName(u"addServicesMenu")
        self.addServicesMenu.setMinimumSize(QSize(0, 658))
        self.addServicesMenu.setMaximumSize(QSize(0, 16777215))
        self.addServicesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_53 = QVBoxLayout(self.addServicesMenu)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(6, 0, 0, 0)
        self.widget_31 = QWidget(self.addServicesMenu)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(200, 350))
        self.widget_31.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_55 = QVBoxLayout(self.widget_31)
        self.verticalLayout_55.setSpacing(24)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(-1, -1, -1, 0)
        self.frame_41 = QFrame(self.widget_31)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.frame_41.setStyleSheet(u"background-color: #879CEB;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.closeAddService = QPushButton(self.frame_41)
        self.closeAddService.setObjectName(u"closeAddService")
        self.closeAddService.setIcon(icon16)
        self.closeAddService.setIconSize(QSize(24, 24))

        self.horizontalLayout_61.addWidget(self.closeAddService, 0, Qt.AlignRight)


        self.verticalLayout_55.addWidget(self.frame_41)

        self.label_23 = QLabel(self.widget_31)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(70, 70))
        self.label_23.setMaximumSize(QSize(70, 70))
        self.label_23.setPixmap(QPixmap(u"resource/truck.svg"))
        self.label_23.setScaledContents(True)

        self.verticalLayout_55.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.frame_58 = QFrame(self.widget_31)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_58)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(-1, 0, -1, 0)
        self.AddServiceName = QLineEdit(self.frame_58)
        self.AddServiceName.setObjectName(u"AddServiceName")
        self.AddServiceName.setFont(font8)
        self.AddServiceName.setMouseTracking(True)
        self.AddServiceName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.AddServiceName.setFrame(True)

        self.verticalLayout_75.addWidget(self.AddServiceName)


        self.verticalLayout_55.addWidget(self.frame_58)

        self.addServiceBtn = QPushButton(self.widget_31)
        self.addServiceBtn.setObjectName(u"addServiceBtn")
        self.addServiceBtn.setFont(font9)
        self.addServiceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addServiceBtn.setStyleSheet(u"	color: #FFFFFF;\n"
"	background-color: #87CEEB;\n"
"	border-radius: 10px\n"
"")

        self.verticalLayout_55.addWidget(self.addServiceBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_23)


        self.verticalLayout_53.addWidget(self.widget_31)

        self.frame_59 = QFrame(self.addServicesMenu)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"background-color: #879CEB;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_59)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_76.addItem(self.verticalSpacer_9)

        self.verticalSpacer_10 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_76.addItem(self.verticalSpacer_10)


        self.verticalLayout_53.addWidget(self.frame_59)


        self.horizontalLayout.addWidget(self.addServicesMenu)

        self.updateDishesMenu = QCustomSlideMenu(self.centralwidget)
        self.updateDishesMenu.setObjectName(u"updateDishesMenu")
        self.updateDishesMenu.setMinimumSize(QSize(0, 658))
        self.updateDishesMenu.setMaximumSize(QSize(0, 16777215))
        self.updateDishesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_59 = QVBoxLayout(self.updateDishesMenu)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(6, 0, 0, 0)
        self.widget_33 = QWidget(self.updateDishesMenu)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(200, 350))
        self.widget_33.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_60 = QVBoxLayout(self.widget_33)
        self.verticalLayout_60.setSpacing(24)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(-1, -1, -1, 0)
        self.frame_46 = QFrame(self.widget_33)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy1.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy1)
        self.frame_46.setStyleSheet(u"background-color: #879CEB;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.closeUpdateDish = QPushButton(self.frame_46)
        self.closeUpdateDish.setObjectName(u"closeUpdateDish")
        self.closeUpdateDish.setIcon(icon16)
        self.closeUpdateDish.setIconSize(QSize(24, 24))

        self.horizontalLayout_57.addWidget(self.closeUpdateDish, 0, Qt.AlignRight)


        self.verticalLayout_60.addWidget(self.frame_46)

        self.label_20 = QLabel(self.widget_33)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(70, 70))
        self.label_20.setMaximumSize(QSize(70, 70))
        self.label_20.setPixmap(QPixmap(u"resource/dishes.png"))
        self.label_20.setScaledContents(True)

        self.verticalLayout_60.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.frame_47 = QFrame(self.widget_33)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_47)
        self.verticalLayout_61.setSpacing(24)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(-1, 0, -1, 0)
        self.updateDishID = QLineEdit(self.frame_47)
        self.updateDishID.setObjectName(u"updateDishID")
        self.updateDishID.setFont(font8)
        self.updateDishID.setMouseTracking(True)
        self.updateDishID.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updateDishID.setFrame(True)

        self.verticalLayout_61.addWidget(self.updateDishID)

        self.updateDishName = QLineEdit(self.frame_47)
        self.updateDishName.setObjectName(u"updateDishName")
        self.updateDishName.setFont(font8)
        self.updateDishName.setMouseTracking(True)
        self.updateDishName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updateDishName.setFrame(True)

        self.verticalLayout_61.addWidget(self.updateDishName)


        self.verticalLayout_60.addWidget(self.frame_47)

        self.updateDishesBtn = QPushButton(self.widget_33)
        self.updateDishesBtn.setObjectName(u"updateDishesBtn")
        self.updateDishesBtn.setFont(font9)
        self.updateDishesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateDishesBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.verticalLayout_60.addWidget(self.updateDishesBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_60.addItem(self.verticalSpacer_17)


        self.verticalLayout_59.addWidget(self.widget_33)

        self.frame_51 = QFrame(self.updateDishesMenu)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color: #879CEB;")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_51)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_18 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_18)

        self.verticalSpacer_19 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_19)


        self.verticalLayout_59.addWidget(self.frame_51)


        self.horizontalLayout.addWidget(self.updateDishesMenu)

        self.deleteDishMenu = QCustomSlideMenu(self.centralwidget)
        self.deleteDishMenu.setObjectName(u"deleteDishMenu")
        self.deleteDishMenu.setMinimumSize(QSize(0, 658))
        self.deleteDishMenu.setMaximumSize(QSize(0, 16777215))
        self.deleteDishMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_67 = QVBoxLayout(self.deleteDishMenu)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(6, 0, 0, 0)
        self.widget_34 = QWidget(self.deleteDishMenu)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(200, 350))
        self.widget_34.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_68 = QVBoxLayout(self.widget_34)
        self.verticalLayout_68.setSpacing(24)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(-1, -1, -1, 0)
        self.frame_52 = QFrame(self.widget_34)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy1.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy1)
        self.frame_52.setStyleSheet(u"background-color: #879CEB;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.closeDeleteDishes = QPushButton(self.frame_52)
        self.closeDeleteDishes.setObjectName(u"closeDeleteDishes")
        self.closeDeleteDishes.setIcon(icon16)
        self.closeDeleteDishes.setIconSize(QSize(24, 24))

        self.horizontalLayout_59.addWidget(self.closeDeleteDishes, 0, Qt.AlignRight)


        self.verticalLayout_68.addWidget(self.frame_52)

        self.label_22 = QLabel(self.widget_34)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(70, 70))
        self.label_22.setMaximumSize(QSize(70, 70))
        self.label_22.setPixmap(QPixmap(u"resource/dishes.png"))
        self.label_22.setScaledContents(True)

        self.verticalLayout_68.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.frame_56 = QFrame(self.widget_34)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_56)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(-1, 0, -1, 0)
        self.deleteDishName = QLineEdit(self.frame_56)
        self.deleteDishName.setObjectName(u"deleteDishName")
        self.deleteDishName.setFont(font8)
        self.deleteDishName.setMouseTracking(True)
        self.deleteDishName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.deleteDishName.setFrame(True)

        self.verticalLayout_73.addWidget(self.deleteDishName)


        self.verticalLayout_68.addWidget(self.frame_56)

        self.deleteDishBtn = QPushButton(self.widget_34)
        self.deleteDishBtn.setObjectName(u"deleteDishBtn")
        self.deleteDishBtn.setFont(font9)
        self.deleteDishBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteDishBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")

        self.verticalLayout_68.addWidget(self.deleteDishBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_68.addItem(self.verticalSpacer_20)


        self.verticalLayout_67.addWidget(self.widget_34)

        self.frame_57 = QFrame(self.deleteDishMenu)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: #879CEB;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_57)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_21 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_74.addItem(self.verticalSpacer_21)

        self.verticalSpacer_22 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_74.addItem(self.verticalSpacer_22)


        self.verticalLayout_67.addWidget(self.frame_57)


        self.horizontalLayout.addWidget(self.deleteDishMenu)

        self.deleteServicesMenu = QCustomSlideMenu(self.centralwidget)
        self.deleteServicesMenu.setObjectName(u"deleteServicesMenu")
        self.deleteServicesMenu.setMinimumSize(QSize(0, 658))
        self.deleteServicesMenu.setMaximumSize(QSize(0, 16777215))
        self.deleteServicesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_79 = QVBoxLayout(self.deleteServicesMenu)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(6, 0, 0, 0)
        self.widget_35 = QWidget(self.deleteServicesMenu)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(200, 350))
        self.widget_35.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_80 = QVBoxLayout(self.widget_35)
        self.verticalLayout_80.setSpacing(24)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(-1, -1, -1, 0)
        self.frame_62 = QFrame(self.widget_35)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy1.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy1)
        self.frame_62.setStyleSheet(u"background-color: #879CEB;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.closeDeleteService = QPushButton(self.frame_62)
        self.closeDeleteService.setObjectName(u"closeDeleteService")
        self.closeDeleteService.setIcon(icon16)
        self.closeDeleteService.setIconSize(QSize(24, 24))

        self.horizontalLayout_63.addWidget(self.closeDeleteService, 0, Qt.AlignRight)


        self.verticalLayout_80.addWidget(self.frame_62)

        self.label_25 = QLabel(self.widget_35)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(70, 70))
        self.label_25.setMaximumSize(QSize(70, 70))
        self.label_25.setPixmap(QPixmap(u"resource/truck.svg"))
        self.label_25.setScaledContents(True)

        self.verticalLayout_80.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.frame_63 = QFrame(self.widget_35)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_63)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(-1, 0, -1, 0)
        self.deleteServiceName = QLineEdit(self.frame_63)
        self.deleteServiceName.setObjectName(u"deleteServiceName")
        self.deleteServiceName.setFont(font8)
        self.deleteServiceName.setMouseTracking(True)
        self.deleteServiceName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.deleteServiceName.setFrame(True)

        self.verticalLayout_81.addWidget(self.deleteServiceName)


        self.verticalLayout_80.addWidget(self.frame_63)

        self.deleteServiceBtn = QPushButton(self.widget_35)
        self.deleteServiceBtn.setObjectName(u"deleteServiceBtn")
        self.deleteServiceBtn.setFont(font9)
        self.deleteServiceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteServiceBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")

        self.verticalLayout_80.addWidget(self.deleteServiceBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_80.addItem(self.verticalSpacer_25)


        self.verticalLayout_79.addWidget(self.widget_35)

        self.frame_64 = QFrame(self.deleteServicesMenu)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"background-color: #879CEB;")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_64)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_26 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_82.addItem(self.verticalSpacer_26)

        self.verticalSpacer_27 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_82.addItem(self.verticalSpacer_27)


        self.verticalLayout_79.addWidget(self.frame_64)


        self.horizontalLayout.addWidget(self.deleteServicesMenu)

        self.deletePackagesMenu = QCustomSlideMenu(self.centralwidget)
        self.deletePackagesMenu.setObjectName(u"deletePackagesMenu")
        self.deletePackagesMenu.setMinimumSize(QSize(0, 658))
        self.deletePackagesMenu.setMaximumSize(QSize(0, 16777215))
        self.deletePackagesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_95 = QVBoxLayout(self.deletePackagesMenu)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(6, 0, 0, 0)
        self.widget_47 = QWidget(self.deletePackagesMenu)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMinimumSize(QSize(200, 350))
        self.widget_47.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_96 = QVBoxLayout(self.widget_47)
        self.verticalLayout_96.setSpacing(24)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_96.setContentsMargins(-1, -1, -1, 0)
        self.frame_76 = QFrame(self.widget_47)
        self.frame_76.setObjectName(u"frame_76")
        sizePolicy1.setHeightForWidth(self.frame_76.sizePolicy().hasHeightForWidth())
        self.frame_76.setSizePolicy(sizePolicy1)
        self.frame_76.setStyleSheet(u"background-color: #879CEB;")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.closeDeletePackagesMenu = QPushButton(self.frame_76)
        self.closeDeletePackagesMenu.setObjectName(u"closeDeletePackagesMenu")
        self.closeDeletePackagesMenu.setIcon(icon16)
        self.closeDeletePackagesMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_70.addWidget(self.closeDeletePackagesMenu, 0, Qt.AlignRight)


        self.verticalLayout_96.addWidget(self.frame_76)

        self.label_30 = QLabel(self.widget_47)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(70, 70))
        self.label_30.setMaximumSize(QSize(70, 70))
        self.label_30.setPixmap(QPixmap(u"resource/package.png"))
        self.label_30.setScaledContents(True)

        self.verticalLayout_96.addWidget(self.label_30, 0, Qt.AlignHCenter)

        self.frame_77 = QFrame(self.widget_47)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_77)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(-1, 0, -1, 0)
        self.deletePackageName = QLineEdit(self.frame_77)
        self.deletePackageName.setObjectName(u"deletePackageName")
        self.deletePackageName.setFont(font8)
        self.deletePackageName.setMouseTracking(True)
        self.deletePackageName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.deletePackageName.setFrame(True)

        self.verticalLayout_97.addWidget(self.deletePackageName)


        self.verticalLayout_96.addWidget(self.frame_77)

        self.deletePackageMenuBtn = QPushButton(self.widget_47)
        self.deletePackageMenuBtn.setObjectName(u"deletePackageMenuBtn")
        self.deletePackageMenuBtn.setFont(font9)
        self.deletePackageMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletePackageMenuBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")

        self.verticalLayout_96.addWidget(self.deletePackageMenuBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_96.addItem(self.verticalSpacer_37)


        self.verticalLayout_95.addWidget(self.widget_47)

        self.frame_78 = QFrame(self.deletePackagesMenu)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"background-color: #879CEB;")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_78)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_38 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_98.addItem(self.verticalSpacer_38)

        self.verticalSpacer_39 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_98.addItem(self.verticalSpacer_39)


        self.verticalLayout_95.addWidget(self.frame_78)


        self.horizontalLayout.addWidget(self.deletePackagesMenu)

        self.deleteOrdersMenu = QCustomSlideMenu(self.centralwidget)
        self.deleteOrdersMenu.setObjectName(u"deleteOrdersMenu")
        self.deleteOrdersMenu.setMinimumSize(QSize(0, 658))
        self.deleteOrdersMenu.setMaximumSize(QSize(0, 16777215))
        self.deleteOrdersMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_99 = QVBoxLayout(self.deleteOrdersMenu)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(6, 0, 0, 0)
        self.widget_48 = QWidget(self.deleteOrdersMenu)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(200, 350))
        self.widget_48.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_100 = QVBoxLayout(self.widget_48)
        self.verticalLayout_100.setSpacing(24)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(-1, -1, -1, 0)
        self.frame_79 = QFrame(self.widget_48)
        self.frame_79.setObjectName(u"frame_79")
        sizePolicy1.setHeightForWidth(self.frame_79.sizePolicy().hasHeightForWidth())
        self.frame_79.setSizePolicy(sizePolicy1)
        self.frame_79.setStyleSheet(u"background-color: #879CEB;")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.closeDeleteOrdersMenu = QPushButton(self.frame_79)
        self.closeDeleteOrdersMenu.setObjectName(u"closeDeleteOrdersMenu")
        self.closeDeleteOrdersMenu.setIcon(icon16)
        self.closeDeleteOrdersMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_71.addWidget(self.closeDeleteOrdersMenu, 0, Qt.AlignRight)


        self.verticalLayout_100.addWidget(self.frame_79)

        self.label_31 = QLabel(self.widget_48)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(70, 70))
        self.label_31.setMaximumSize(QSize(70, 70))
        self.label_31.setPixmap(QPixmap(u"resource/orders.png"))
        self.label_31.setScaledContents(True)

        self.verticalLayout_100.addWidget(self.label_31, 0, Qt.AlignHCenter)

        self.frame_80 = QFrame(self.widget_48)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_80)
        self.verticalLayout_101.setSpacing(24)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(-1, 0, -1, 0)
        self.deleteOrderNameCus = QLineEdit(self.frame_80)
        self.deleteOrderNameCus.setObjectName(u"deleteOrderNameCus")
        self.deleteOrderNameCus.setFont(font8)
        self.deleteOrderNameCus.setMouseTracking(True)
        self.deleteOrderNameCus.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.deleteOrderNameCus.setFrame(True)

        self.verticalLayout_101.addWidget(self.deleteOrderNameCus)

        self.deleteOrderNamePack = QLineEdit(self.frame_80)
        self.deleteOrderNamePack.setObjectName(u"deleteOrderNamePack")
        self.deleteOrderNamePack.setFont(font8)
        self.deleteOrderNamePack.setMouseTracking(True)
        self.deleteOrderNamePack.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.deleteOrderNamePack.setFrame(True)

        self.verticalLayout_101.addWidget(self.deleteOrderNamePack)


        self.verticalLayout_100.addWidget(self.frame_80)

        self.deleteOrderMenuBtn = QPushButton(self.widget_48)
        self.deleteOrderMenuBtn.setObjectName(u"deleteOrderMenuBtn")
        self.deleteOrderMenuBtn.setFont(font9)
        self.deleteOrderMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteOrderMenuBtn.setStyleSheet(u"	background-color: #e64a3b;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;")

        self.verticalLayout_100.addWidget(self.deleteOrderMenuBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_100.addItem(self.verticalSpacer_40)


        self.verticalLayout_99.addWidget(self.widget_48)

        self.frame_81 = QFrame(self.deleteOrdersMenu)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"background-color: #879CEB;")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_81)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_41 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_102.addItem(self.verticalSpacer_41)

        self.verticalSpacer_42 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_102.addItem(self.verticalSpacer_42)


        self.verticalLayout_99.addWidget(self.frame_81)


        self.horizontalLayout.addWidget(self.deleteOrdersMenu)

        self.updateOrderMenu = QCustomSlideMenu(self.centralwidget)
        self.updateOrderMenu.setObjectName(u"updateOrderMenu")
        self.updateOrderMenu.setMinimumSize(QSize(0, 658))
        self.updateOrderMenu.setMaximumSize(QSize(0, 16777215))
        self.updateOrderMenu.setCursor(QCursor(Qt.ArrowCursor))
        self.updateOrderMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_103 = QVBoxLayout(self.updateOrderMenu)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(6, 0, 0, 0)
        self.widget_49 = QWidget(self.updateOrderMenu)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(200, 350))
        self.widget_49.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_104 = QVBoxLayout(self.widget_49)
        self.verticalLayout_104.setSpacing(9)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(-1, -1, -1, 0)
        self.frame_82 = QFrame(self.widget_49)
        self.frame_82.setObjectName(u"frame_82")
        sizePolicy1.setHeightForWidth(self.frame_82.sizePolicy().hasHeightForWidth())
        self.frame_82.setSizePolicy(sizePolicy1)
        self.frame_82.setStyleSheet(u"background-color: #879CEB;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.closeUpdateOrderMenu = QPushButton(self.frame_82)
        self.closeUpdateOrderMenu.setObjectName(u"closeUpdateOrderMenu")
        self.closeUpdateOrderMenu.setIcon(icon16)
        self.closeUpdateOrderMenu.setIconSize(QSize(24, 24))

        self.horizontalLayout_72.addWidget(self.closeUpdateOrderMenu, 0, Qt.AlignRight)


        self.verticalLayout_104.addWidget(self.frame_82)

        self.label_32 = QLabel(self.widget_49)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(70, 70))
        self.label_32.setMaximumSize(QSize(70, 70))
        self.label_32.setPixmap(QPixmap(u"resource/orders.png"))
        self.label_32.setScaledContents(True)

        self.verticalLayout_104.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.frame_83 = QFrame(self.widget_49)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_83)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, -1, -1, 0)
        self.updateCusInOrders = QLineEdit(self.frame_83)
        self.updateCusInOrders.setObjectName(u"updateCusInOrders")
        self.updateCusInOrders.setFont(font8)
        self.updateCusInOrders.setMouseTracking(True)
        self.updateCusInOrders.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updateCusInOrders.setFrame(True)
        self.updateCusInOrders.setReadOnly(True)

        self.verticalLayout_36.addWidget(self.updateCusInOrders)

        self.updateCusIDinOrders = QLineEdit(self.frame_83)
        self.updateCusIDinOrders.setObjectName(u"updateCusIDinOrders")
        self.updateCusIDinOrders.setFont(font8)
        self.updateCusIDinOrders.setMouseTracking(True)
        self.updateCusIDinOrders.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updateCusIDinOrders.setFrame(True)
        self.updateCusIDinOrders.setReadOnly(True)

        self.verticalLayout_36.addWidget(self.updateCusIDinOrders)

        self.updatePackInOrders = QLineEdit(self.frame_83)
        self.updatePackInOrders.setObjectName(u"updatePackInOrders")
        self.updatePackInOrders.setFont(font8)
        self.updatePackInOrders.setMouseTracking(True)
        self.updatePackInOrders.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackInOrders.setFrame(True)
        self.updatePackInOrders.setReadOnly(True)

        self.verticalLayout_36.addWidget(self.updatePackInOrders)

        self.updatePackIDinOrders = QLineEdit(self.frame_83)
        self.updatePackIDinOrders.setObjectName(u"updatePackIDinOrders")
        self.updatePackIDinOrders.setFont(font8)
        self.updatePackIDinOrders.setMouseTracking(True)
        self.updatePackIDinOrders.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackIDinOrders.setFrame(True)
        self.updatePackIDinOrders.setReadOnly(True)

        self.verticalLayout_36.addWidget(self.updatePackIDinOrders)

        self.updatePackPriceInOrder = QLineEdit(self.frame_83)
        self.updatePackPriceInOrder.setObjectName(u"updatePackPriceInOrder")
        self.updatePackPriceInOrder.setFont(font8)
        self.updatePackPriceInOrder.setMouseTracking(True)
        self.updatePackPriceInOrder.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackPriceInOrder.setFrame(True)
        self.updatePackPriceInOrder.setReadOnly(True)

        self.verticalLayout_36.addWidget(self.updatePackPriceInOrder)

        self.updatePackDateInOrder = QLineEdit(self.frame_83)
        self.updatePackDateInOrder.setObjectName(u"updatePackDateInOrder")
        self.updatePackDateInOrder.setFont(font8)
        self.updatePackDateInOrder.setMouseTracking(True)
        self.updatePackDateInOrder.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updatePackDateInOrder.setFrame(True)
        self.updatePackDateInOrder.setReadOnly(True)

        self.verticalLayout_36.addWidget(self.updatePackDateInOrder)


        self.verticalLayout_104.addWidget(self.frame_83)


        self.verticalLayout_103.addWidget(self.widget_49)

        self.frame_84 = QFrame(self.updateOrderMenu)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(16777215, 250))
        self.frame_84.setStyleSheet(u"background-color: #879CEB;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_84)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_84)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_24)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(16)
        self.gridLayout_2.setContentsMargins(18, -1, 18, -1)
        self.paidBtn = QPushButton(self.frame_24)
        self.paidBtn.setObjectName(u"paidBtn")
        self.paidBtn.setFont(font9)
        self.paidBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.paidBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.gridLayout_2.addWidget(self.paidBtn, 0, 1, 1, 1)

        self.deliveredBtn = QPushButton(self.frame_24)
        self.deliveredBtn.setObjectName(u"deliveredBtn")
        self.deliveredBtn.setFont(font9)
        self.deliveredBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deliveredBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.gridLayout_2.addWidget(self.deliveredBtn, 0, 2, 1, 1)

        self.paidResetBtn = QPushButton(self.frame_24)
        self.paidResetBtn.setObjectName(u"paidResetBtn")
        self.paidResetBtn.setFont(font9)
        self.paidResetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.paidResetBtn.setStyleSheet(u"	background-color: #C0C0C0;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.gridLayout_2.addWidget(self.paidResetBtn, 1, 1, 1, 1)

        self.deliveredResetBtn = QPushButton(self.frame_24)
        self.deliveredResetBtn.setObjectName(u"deliveredResetBtn")
        self.deliveredResetBtn.setFont(font9)
        self.deliveredResetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deliveredResetBtn.setStyleSheet(u"	background-color: #C0C0C0;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.gridLayout_2.addWidget(self.deliveredResetBtn, 1, 2, 1, 1)


        self.verticalLayout_105.addWidget(self.frame_24)

        self.verticalSpacer_43 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_105.addItem(self.verticalSpacer_43)

        self.verticalSpacer_44 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_105.addItem(self.verticalSpacer_44)


        self.verticalLayout_103.addWidget(self.frame_84)


        self.horizontalLayout.addWidget(self.updateOrderMenu)

        self.updateServicesMenu = QCustomSlideMenu(self.centralwidget)
        self.updateServicesMenu.setObjectName(u"updateServicesMenu")
        self.updateServicesMenu.setMinimumSize(QSize(0, 658))
        self.updateServicesMenu.setMaximumSize(QSize(0, 16777215))
        self.updateServicesMenu.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_117 = QVBoxLayout(self.updateServicesMenu)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(6, 0, 0, 0)
        self.widget_44 = QWidget(self.updateServicesMenu)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setMinimumSize(QSize(200, 350))
        self.widget_44.setStyleSheet(u"background-color: #879CEB;")
        self.verticalLayout_118 = QVBoxLayout(self.widget_44)
        self.verticalLayout_118.setSpacing(24)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.verticalLayout_118.setContentsMargins(-1, -1, -1, 0)
        self.frame_92 = QFrame(self.widget_44)
        self.frame_92.setObjectName(u"frame_92")
        sizePolicy1.setHeightForWidth(self.frame_92.sizePolicy().hasHeightForWidth())
        self.frame_92.setSizePolicy(sizePolicy1)
        self.frame_92.setStyleSheet(u"background-color: #879CEB;")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.closeUpdateService = QPushButton(self.frame_92)
        self.closeUpdateService.setObjectName(u"closeUpdateService")
        self.closeUpdateService.setIcon(icon16)
        self.closeUpdateService.setIconSize(QSize(24, 24))

        self.horizontalLayout_74.addWidget(self.closeUpdateService, 0, Qt.AlignRight)


        self.verticalLayout_118.addWidget(self.frame_92)

        self.label_37 = QLabel(self.widget_44)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(70, 70))
        self.label_37.setMaximumSize(QSize(70, 70))
        self.label_37.setPixmap(QPixmap(u"resource/truck.svg"))
        self.label_37.setScaledContents(True)

        self.verticalLayout_118.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.frame_93 = QFrame(self.widget_44)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_93)
        self.verticalLayout_119.setSpacing(24)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(-1, 0, -1, 0)
        self.updateServiceID = QLineEdit(self.frame_93)
        self.updateServiceID.setObjectName(u"updateServiceID")
        self.updateServiceID.setFont(font8)
        self.updateServiceID.setMouseTracking(True)
        self.updateServiceID.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updateServiceID.setFrame(True)

        self.verticalLayout_119.addWidget(self.updateServiceID)

        self.updateServiceName = QLineEdit(self.frame_93)
        self.updateServiceName.setObjectName(u"updateServiceName")
        self.updateServiceName.setFont(font8)
        self.updateServiceName.setMouseTracking(True)
        self.updateServiceName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #FFFFFF;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.updateServiceName.setFrame(True)

        self.verticalLayout_119.addWidget(self.updateServiceName)


        self.verticalLayout_118.addWidget(self.frame_93)

        self.updateServicesBtn = QPushButton(self.widget_44)
        self.updateServicesBtn.setObjectName(u"updateServicesBtn")
        self.updateServicesBtn.setFont(font9)
        self.updateServicesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateServicesBtn.setStyleSheet(u"	background-color: #1bc98c;\n"
"	border-radius: 10px;\n"
"	color: #FFFFFF;\n"
"")

        self.verticalLayout_118.addWidget(self.updateServicesBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_118.addItem(self.verticalSpacer_51)


        self.verticalLayout_117.addWidget(self.widget_44)

        self.frame_94 = QFrame(self.updateServicesMenu)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setStyleSheet(u"background-color: #879CEB;")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_94)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_52 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_120.addItem(self.verticalSpacer_52)

        self.verticalSpacer_53 = QSpacerItem(20, 305, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_120.addItem(self.verticalSpacer_53)


        self.verticalLayout_117.addWidget(self.frame_94)


        self.horizontalLayout.addWidget(self.updateServicesMenu)

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
        self.dishesMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Dishes", None))
        self.servicesMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        self.menuBtn.setText("")
        self.dashBoard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.aboutBtn.setText("")
        self.packages.setText(QCoreApplication.translate("MainWindow", u"Packages", None))
        self.PackageBtn.setText("")
        self.dishes.setText(QCoreApplication.translate("MainWindow", u"Dishes", None))
        self.dishesBtn.setText("")
        self.services.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        self.servicesBtn.setText("")
        self.orders.setText(QCoreApplication.translate("MainWindow", u"Latest Orders", None))
        self.ordersBtn.setText(QCoreApplication.translate("MainWindow", u"View Orders", None))
        ___qtablewidgetitem = self.ordersTableWidgetDashboard.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Customers", None));
        ___qtablewidgetitem1 = self.ordersTableWidgetDashboard.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Customers ID", None));
        ___qtablewidgetitem2 = self.ordersTableWidgetDashboard.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Package", None));
        ___qtablewidgetitem3 = self.ordersTableWidgetDashboard.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Package ID", None));
        ___qtablewidgetitem4 = self.ordersTableWidgetDashboard.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem5 = self.ordersTableWidgetDashboard.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem6 = self.ordersTableWidgetDashboard.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem7 = self.ordersTableWidgetDashboard.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Delivered", None));
        self.customers.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.customersBtn.setText(QCoreApplication.translate("MainWindow", u"View Customers", None))
        ___qtablewidgetitem8 = self.customerTableWidgetDashboard.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.customerTableWidgetDashboard.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.customerTableWidgetDashboard.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem11 = self.customerTableWidgetDashboard.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        self.menuBtn_1.setText("")
        self.dashBoard_1.setText(QCoreApplication.translate("MainWindow", u"Orders Page", None))
        self.ordersSearchBtn.setText("")
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.refSearchOrder.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.aboutBtn_1.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Orders Page", None))
        self.deleteOrderBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editOrderBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createOrderBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem12 = self.ordersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Customers", None));
        ___qtablewidgetitem13 = self.ordersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Customer ID", None));
        ___qtablewidgetitem14 = self.ordersTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Package", None));
        ___qtablewidgetitem15 = self.ordersTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Package ID", None));
        ___qtablewidgetitem16 = self.ordersTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem17 = self.ordersTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem18 = self.ordersTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Paid", None));
        ___qtablewidgetitem19 = self.ordersTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Delivered", None));
        self.menuBtn_2.setText("")
        self.dashBoard_2.setText("")
        self.customerSearchBtn.setText("")
        self.customerSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.refSearchCus.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.aboutBtn_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Customers Page", None))
        self.deleteCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem20 = self.customersTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem21 = self.customersTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem22 = self.customersTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem23 = self.customersTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        self.menuBtn_3.setText("")
        self.dashBoard_3.setText(QCoreApplication.translate("MainWindow", u"Dishes Page", None))
        self.dishesSearchBtn.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.refSearchDish.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.aboutBtn_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dishes Page", None))
        self.deleteDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem24 = self.dishesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem25 = self.dishesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.menuBtn_4.setText("")
        self.dashBoard_4.setText(QCoreApplication.translate("MainWindow", u"Services Page", None))
        self.servicesSearchBtn.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.refSearchService.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.aboutBtn_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Services Page", None))
        self.deleteService.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editService.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createService.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem26 = self.servicesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem27 = self.servicesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.backToPackageBtn.setText("")
        self.dashBoard_6.setText(QCoreApplication.translate("MainWindow", u"Packages Page", None))
        self.aboutBtn_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Add Dishes To Package", None))
        self.add3Dish.setText(QCoreApplication.translate("MainWindow", u"3 Dishes", None))
        self.add4Dish.setText(QCoreApplication.translate("MainWindow", u"4 Dishes", None))
        self.add5Dish.setText(QCoreApplication.translate("MainWindow", u"5 Dishes", None))
        ___qtablewidgetitem28 = self.addCoupleDishTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem29 = self.addCoupleDishTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem30 = self.addCoupleDishTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Price (Pesos)", None));
        ___qtablewidgetitem31 = self.addCoupleDishTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Pax", None));
        ___qtablewidgetitem32 = self.addCoupleDishTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Dishes", None));
        self.menuBtn_5.setText("")
        self.dashBoard_5.setText(QCoreApplication.translate("MainWindow", u"Packages Page", None))
        self.packagesSearchBtn.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.refSearchPack.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.aboutBtn_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Packages Page", None))
        self.addDishesInPackageBtn.setText(QCoreApplication.translate("MainWindow", u"Add Dishes", None))
        self.deletePackageBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editPackageBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.createPackageBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        ___qtablewidgetitem33 = self.packagesTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem34 = self.packagesTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem35 = self.packagesTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Price (Pesos)", None));
        ___qtablewidgetitem36 = self.packagesTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Pax", None));
        ___qtablewidgetitem37 = self.packagesTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Dishes", None));
        self.closeCreateOrder.setText("")
        self.label_17.setText("")
        self.customerComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.cusIDinOrders.setInputMask("")
        self.cusIDinOrders.setText("")
        self.cusIDinOrders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.packComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package", None))
        self.packIDinOrders.setText("")
        self.packIDinOrders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package ID", None))
        self.packPriceInOrder.setText("")
        self.packPriceInOrder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.addOrder.setText(QCoreApplication.translate("MainWindow", u"Create Order", None))
        self.closeAddCustomer.setText("")
        self.label_15.setText("")
        self.customerName.setText("")
        self.customerName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer Name", None))
        self.customerAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.customerPhoneNum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.addCustomer.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.closeAdd3DishMenu.setText("")
        self.label_27.setText("")
        self.dish3PackageName.setInputMask("")
        self.dish3PackageName.setText("")
        self.dish3PackageName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Name", None))
        self.dish3Name1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 1", None))
        self.dish3Name2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 2", None))
        self.dish3Name3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 3", None))
        self.add3DishBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.closeAddPackage.setText("")
        self.label_18.setText("")
        self.addPackageName.setInputMask("")
        self.addPackageName.setText("")
        self.addPackageName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Name", None))
        self.addPackagePrice.setText("")
        self.addPackagePrice.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Price", None))
        self.addPackagePax.setText("")
        self.addPackagePax.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Pax", None))
        self.addPackageBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.closeAdd4DishMenu.setText("")
        self.label_28.setText("")
        self.dish4PackageName.setInputMask("")
        self.dish4PackageName.setText("")
        self.dish4PackageName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Name", None))
        self.dish4Name1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 1", None))
        self.dish4Name2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 2", None))
        self.dish4Name3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 3", None))
        self.dish4Name4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 4", None))
        self.add4DishBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.iconCloseUpdateCustomer.setText("")
        self.label_21.setText("")
        self.customerIDUpdate.setText("")
        self.customerIDUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.customerNameUpdate.setText("")
        self.customerNameUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer Name", None))
        self.customerPhoneNumUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.customerAddressUpdate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.updateCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Update Customer", None))
        self.closeAdd5DishMenu.setText("")
        self.label_29.setText("")
        self.dish5PackageName.setInputMask("")
        self.dish5PackageName.setText("")
        self.dish5PackageName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Name", None))
        self.dish5Name1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 1", None))
        self.dish5Name2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 2", None))
        self.dish5Name3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 3", None))
        self.dish5Name4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 4", None))
        self.dish5Name5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish 5", None))
        self.add5DishBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.closeUpdatePackagesMenu.setText("")
        self.label_24.setText("")
        self.updatePackageID.setInputMask("")
        self.updatePackageID.setText("")
        self.updatePackageID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package ID", None))
        self.updatePackageName.setInputMask("")
        self.updatePackageName.setText("")
        self.updatePackageName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Name", None))
        self.updatePackagePrice.setText("")
        self.updatePackagePrice.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Price", None))
        self.updatePackagePax.setText("")
        self.updatePackagePax.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package Pax", None))
        self.updatePackageBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.closeAddDishes.setText("")
        self.label_19.setText("")
        self.dishesName.setText("")
        self.dishesName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of the Dish", None))
        self.addDishes.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.closeDeleteCustomer.setText("")
        self.label_26.setText("")
        self.deleteCustomerLineEdit.setText("")
        self.deleteCustomerLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.deleteCustomerBtn_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.closeAddService.setText("")
        self.label_23.setText("")
        self.AddServiceName.setText("")
        self.AddServiceName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of Service", None))
        self.addServiceBtn.setText(QCoreApplication.translate("MainWindow", u"Create New", None))
        self.closeUpdateDish.setText("")
        self.label_20.setText("")
        self.updateDishID.setText("")
        self.updateDishID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dish ID", None))
        self.updateDishName.setText("")
        self.updateDishName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of the Dish", None))
        self.updateDishesBtn.setText(QCoreApplication.translate("MainWindow", u"Update Dish", None))
        self.closeDeleteDishes.setText("")
        self.label_22.setText("")
        self.deleteDishName.setText("")
        self.deleteDishName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of the Dish", None))
        self.deleteDishBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Dish", None))
        self.closeDeleteService.setText("")
        self.label_25.setText("")
        self.deleteServiceName.setText("")
        self.deleteServiceName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Service ID", None))
        self.deleteServiceBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Service", None))
        self.closeDeletePackagesMenu.setText("")
        self.label_30.setText("")
        self.deletePackageName.setText("")
        self.deletePackageName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package ID", None))
        self.deletePackageMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Dish", None))
        self.closeDeleteOrdersMenu.setText("")
        self.label_31.setText("")
        self.deleteOrderNameCus.setText("")
        self.deleteOrderNameCus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.deleteOrderNamePack.setText("")
        self.deleteOrderNamePack.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package ID", None))
        self.deleteOrderMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Order", None))
        self.closeUpdateOrderMenu.setText("")
        self.label_32.setText("")
        self.updateCusInOrders.setInputMask("")
        self.updateCusInOrders.setText("")
        self.updateCusInOrders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.updateCusIDinOrders.setInputMask("")
        self.updateCusIDinOrders.setText("")
        self.updateCusIDinOrders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Customer ID", None))
        self.updatePackInOrders.setInputMask("")
        self.updatePackInOrders.setText("")
        self.updatePackInOrders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package", None))
        self.updatePackIDinOrders.setText("")
        self.updatePackIDinOrders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Package ID", None))
        self.updatePackPriceInOrder.setText("")
        self.updatePackPriceInOrder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.updatePackDateInOrder.setText("")
        self.updatePackDateInOrder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.paidBtn.setText(QCoreApplication.translate("MainWindow", u"Paid", None))
        self.deliveredBtn.setText(QCoreApplication.translate("MainWindow", u"Delivered", None))
        self.paidResetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.deliveredResetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.closeUpdateService.setText("")
        self.label_37.setText("")
        self.updateServiceID.setText("")
        self.updateServiceID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Service ID", None))
        self.updateServiceName.setText("")
        self.updateServiceName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of the Service", None))
        self.updateServicesBtn.setText(QCoreApplication.translate("MainWindow", u"Update Service", None))
    # retranslateUi

