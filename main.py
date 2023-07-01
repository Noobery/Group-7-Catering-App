import os
os.environ['ICONIFY_QTLIB'] = 'PySide6'


import sys

from ui_appDashboard import *

from Custom_Widgets.Widgets import *

settings = QSettings()

from Functions import appFunctions



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui) 

        # Connect signals to appFunctions methods
    ####################### CUSTOMERS ##################################
        self.ui.addCustomer.clicked.connect(lambda: appFunctions.inputCustomer(self))

        self.ui.refSearchCus.clicked.connect(lambda: appFunctions.displayCustomer(self))
        self.ui.customerSearchBtn.clicked.connect(lambda: appFunctions.searchCustomer(self))

        self.ui.deleteCustomerBtn_2.clicked.connect(lambda: appFunctions.deleteCustomer(self))
        self.ui.customersTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedCustomer(self))

        appFunctions.displayCustomer(self)
        appFunctions.displayCustomerDashboard(self)
        
        self.ui.updateCustomerBtn.clicked.connect(lambda: appFunctions.updateCustomer(self))
        self.ui.customersTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedCustomerUpdate(self))
        
        
    ####################### CUSTOMERS ##################################

    ####################### ORDERS ##################################
        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)

        self.ui.ordersTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedOrderDelete(self))
        self.ui.deleteOrderMenuBtn.clicked.connect(lambda: appFunctions.deleteOrder(self))
        self.ui.customerComboBox.currentIndexChanged.connect(lambda: appFunctions.updateCustOrder(self))
        self.ui.packComboBox.currentIndexChanged.connect(lambda: appFunctions.updatePackOrder(self))
        self.ui.addOrder.clicked.connect(lambda: appFunctions.addOrder(self))
        self.ui.ordersSearchBtn.clicked.connect(lambda: appFunctions.searchOrder(self))
        self.ui.refSearchOrder.clicked.connect(lambda: appFunctions.displayOrders(self))
        self.ui.deliveredBtn.clicked.connect(lambda: appFunctions.updateOrderDel(self))
        self.ui.paidBtn.clicked.connect(lambda: appFunctions.updateOrderPay(self))
        self.ui.deliveredResetBtn.clicked.connect(lambda: appFunctions.updateOrderOrdReset(self))
        self.ui.paidResetBtn.clicked.connect(lambda: appFunctions.updateOrderPayReset(self))

        self.ui.ordersTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedOrderUpdate(self))
    ####################### ORDERS ##################################


    ####################### DISHES ##################################
        self.ui.refSearchDish.clicked.connect(lambda: appFunctions.displayDishes(self))
        self.ui.dishesSearchBtn.clicked.connect(lambda: appFunctions.searchDishes(self))

        appFunctions.displayDishes(self)

        self.ui.addDishes.clicked.connect(lambda: appFunctions.inputDishes(self))

        self.ui.updateDishesBtn.clicked.connect(lambda: appFunctions.updateDishes(self))
        self.ui.dishesTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedDishesUpdate(self))

        self.ui.deleteDishBtn.clicked.connect(lambda: appFunctions.deleteDishes(self))
        self.ui.dishesTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedDishesDelete(self))

        
    ####################### DISHES ##################################



    ####################### PACKAGES ##################################
        self.ui.addPackageBtn.clicked.connect(lambda: appFunctions.inputPackage(self))
        self.ui.packagesSearchBtn.clicked.connect(lambda: appFunctions.searchPackages(self))
        self.ui.refSearchPack.clicked.connect(lambda: appFunctions.displayPackage(self))
        
        self.ui.add3DishBtn.clicked.connect(lambda: appFunctions.addDish3(self))
        self.ui.add4DishBtn.clicked.connect(lambda: appFunctions.addDish4(self))
        self.ui.add5DishBtn.clicked.connect(lambda: appFunctions.addDish5(self))

        self.ui.updatePackageBtn.clicked.connect(lambda: appFunctions.updatePackage(self))
        self.ui.packagesTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedPackageUpdate(self))

        self.ui.addCoupleDishTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedPackageDish(self))

        self.ui.deletePackageMenuBtn.clicked.connect(lambda: appFunctions.deletePackage(self))
        self.ui.packagesTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedPackDelete(self))

        appFunctions.displayPackage(self)
        appFunctions.displayPackageDish(self)

    ####################### PACKAGES ##################################

        
    ####################### SERVICES ##################################

        self.ui.servicesSearchBtn.clicked.connect(lambda: appFunctions.searchServies(self))
        self.ui.refSearchService.clicked.connect(lambda: appFunctions.displayServices(self))

        appFunctions.displayServices(self)

        self.ui.addServiceBtn.clicked.connect(lambda: appFunctions.inputServices(self))

        self.ui.updateServicesBtn.clicked.connect(lambda: appFunctions.updateServices(self))
        self.ui.servicesTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedServicesUpdate(self))

        self.ui.deleteServiceBtn.clicked.connect(lambda: appFunctions.deleteServices(self))
        self.ui.servicesTableWidget.itemSelectionChanged.connect(lambda: appFunctions.whenClickedServicesDelete(self))
    ####################### SERVICES ##################################

        

    ####################### OTHERS ##################################

    ####################### OTHERS ##################################
       
        
        
        
       
        
        

        self.show() 

        

       


        """
        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ssis_v2.db'))
        appFunctions.main (dbFolder)

        

        appFunctions.displayCourse3(self, appFunctions.getAllUsers(dbFolder))

        self.ui.inputCourse.clicked.connect(lambda: appFunctions.inputCourse(self, dbFolder))

        appFunctions.displayCourse1(self, appFunctions.getAllUsers1(dbFolder))

        appFunctions.displayCourse2(self, appFunctions.getAllUsers1(dbFolder))

        self.ui.addInfo.clicked.connect(lambda: appFunctions.inputCourse1(self, dbFolder))

        self.ui.csearchBtn.clicked.connect(lambda: appFunctions.searchData(self, dbFolder))
        
        self.ui.ssearchBtn.clicked.connect(lambda: appFunctions.searchData1(self, dbFolder))
        
        self.ui.deleteStudentButton.clicked.connect(lambda: appFunctions.deleteStudent(self))

        self.ui.deleteCourseButton.clicked.connect(lambda: appFunctions.deleteCourse(self))

        self.ui.tableWidget_4.itemSelectionChanged.connect(lambda: appFunctions.whenClickedCode(self))

        self.ui.tableWidget_3.itemSelectionChanged.connect(lambda: appFunctions.whenClickedId(self))

        self.ui.editStudentButton.clicked.connect(lambda: appFunctions.updateStudent(self))

        self.ui.updateStudentButton.clicked.connect(lambda: appFunctions.updateStudentData(self))

        self.ui.editCourseButton.clicked.connect(lambda: appFunctions.updateCourses(self))

        self.ui.updateCourseButton.clicked.connect(lambda: appFunctions.updateCourseData(self))

        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
