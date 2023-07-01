import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QHeaderView, QDialog, QVBoxLayout, QMessageBox, QInputDialog
from PySide6.QtCore import Qt
from datetime import date



mydb = mysql.connector.connect (

    host="localhost",
    user ="new",
    password="bippityboppity69",
    database="test"

)

mycursor = mydb.cursor ()


class appFunctions():
    def __init__(self, arg):
        super(appFunctions, self).__init__()
        self.arg = arg


    def inputCustomer(self):
        
            customerName = self.ui.customerName.text()
            customerPhoneNum = self.ui.customerPhoneNum.text()
            customerAddress = self.ui.customerAddress.text()

            insert_customers_data_sql = "INSERT INTO customer (name, phoneNum, address) VALUES (%s, %s, %s)"

            try:

                # Insert the new customer data
                mycursor.execute(insert_customers_data_sql, (customerName, customerPhoneNum, customerAddress))
                mydb.commit()
                QMessageBox.information(self, "Success", "Customer inserted successfully.")
                self.ui.customerName.setText("")
                self.ui.customerPhoneNum.setText("")
                self.ui.customerAddress.setText("")
                appFunctions.displayCustomer(self)
            except Error as e:
                print(e)
    
    def displayCustomer(self):
        query = "SELECT * FROM customer;"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.customersTableWidget.clearContents()
        self.ui.customersTableWidget.setRowCount(0)
        self.ui.customersTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.customersTableWidget.rowCount()
            self.ui.customersTableWidget.insertRow(rowPos)
            self.ui.customersTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.customersTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.customersTableWidget.setItem(rowPos, 2, QTableWidgetItem(str(row[2])))
            self.ui.customersTableWidget.setItem(rowPos, 3, QTableWidgetItem(row[3]))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.customersTableWidget.columnCount()):
                item = self.ui.customersTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        customerIDs = [row[1] for row in rows]
        self.ui.customerComboBox.clear()
        self.ui.customerComboBox.addItems(customerIDs)

        self.ui.customersTableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeToContents)

    def displayCustomerDashboard(self):
        query = "SELECT * FROM customer;"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.customerTableWidgetDashboard.clearContents()
        self.ui.customerTableWidgetDashboard.setRowCount(0)
        self.ui.customerTableWidgetDashboard.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.customerTableWidgetDashboard.rowCount()
            self.ui.customerTableWidgetDashboard.insertRow(rowPos)
            self.ui.customerTableWidgetDashboard.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.customerTableWidgetDashboard.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.customerTableWidgetDashboard.setItem(rowPos, 2, QTableWidgetItem(str(row[2])))
            self.ui.customerTableWidgetDashboard.setItem(rowPos, 3, QTableWidgetItem(row[3]))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.customerTableWidgetDashboard.columnCount()):
                item = self.ui.customerTableWidgetDashboard.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    
        self.ui.customerTableWidgetDashboard.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeToContents)

    def whenClickedCustomerUpdate(self):
        selected_indexes = self.ui.customersTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            customerID_item = self.ui.customersTableWidget.item(row, 0)
            customerName_item = self.ui.customersTableWidget.item(row, 1)
            customerPhoneNum_item = self.ui.customersTableWidget.item(row, 2)
            customerAddress_item = self.ui.customersTableWidget.item(row, 3)

            if customerID_item and customerName_item and customerPhoneNum_item and customerAddress_item:
                customerID = int(customerID_item.text())
                customerName = customerName_item.text()
                customerPhoneNum = customerPhoneNum_item.text()
                customerAddress = customerAddress_item.text()

                # Set the values to the corresponding line edits
                self.ui.customerIDUpdate.setText(str(customerID))
                self.ui.customerNameUpdate.setText(customerName)
                self.ui.customerPhoneNumUpdate.setText(customerPhoneNum)
                self.ui.customerAddressUpdate.setText(customerAddress)
                self.ui.customerIDUpdate.setReadOnly(True)

    def searchCustomer(self):
        query = "SELECT * FROM customer WHERE customerID LIKE %s OR name LIKE %s OR phoneNum LIKE %s OR address LIKE %s"
        search_text = '%' + self.ui.customerSearch.text() + '%'  # Add wildcards to the search text
        mycursor.execute(query, (search_text, search_text, search_text, search_text))

        # Fetch all matching rows from the query result
        rows = mycursor.fetchall()

        table_widget = self.ui.customersTableWidget
        self.ui.customersTableWidget.clearContents()
        self.ui.customersTableWidget.setRowCount(0)
        self.ui.customersTableWidget.verticalHeader().setVisible(False)
        
        for row in rows:
            rowPos = table_widget.rowCount()
            table_widget.insertRow(rowPos)
            table_widget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            table_widget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            table_widget.setItem(rowPos, 2, QTableWidgetItem(str(row[2])))
            table_widget.setItem(rowPos, 3, QTableWidgetItem(row[3]))

            # Set item flags to make cells non-editable
            for col in range(table_widget.columnCount()):
                item = table_widget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    
    def deleteCustomer(self):
        # Get the course code from the line edit widget
        delete_customer = self.ui.deleteCustomerLineEdit.text()

        # Print the course code for debugging
        # print("Course Code:", course_code)
        

        delete_customer_sql = "DELETE FROM customer WHERE customerID = %s"

        try:

                mycursor.execute(delete_customer_sql, (delete_customer,))
                mydb.commit()
                
                QMessageBox.information(None, "Success", "Customer deleted successfully.")
          
                appFunctions.displayCustomer(self)
           
        except Error as e:
            print(e)

    def whenClickedCustomer(self):
        selected_indexes = self.ui.customersTableWidget.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()
            
            # Retrieve the data from the selected cell
            item = self.ui.customersTableWidget.item(row, 0)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.deleteCustomerLineEdit.setText(value)

    def updateCustomer(self):
        customerID = int(self.ui.customerIDUpdate.text())
        customerName = self.ui.customerNameUpdate.text()
        customerPhoneNum = self.ui.customerPhoneNumUpdate.text()
        customerAddress = self.ui.customerAddressUpdate.text()

        update_query = "UPDATE customer SET name = %s, phoneNum = %s, address = %s WHERE customerID = %s"
        values = (customerName, customerPhoneNum, customerAddress, customerID)

        try:
            mycursor.execute(update_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Customer updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayCustomer(self)
        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)
    
    def whenClickedCustomerUpdate(self):
        selected_indexes = self.ui.customersTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            customerID_item = self.ui.customersTableWidget.item(row, 0)
            customerName_item = self.ui.customersTableWidget.item(row, 1)
            customerPhoneNum_item = self.ui.customersTableWidget.item(row, 2)
            customerAddress_item = self.ui.customersTableWidget.item(row, 3)

            if customerID_item and customerName_item and customerPhoneNum_item and customerAddress_item:
                customerID = int(customerID_item.text())
                customerName = customerName_item.text()
                customerPhoneNum = customerPhoneNum_item.text()
                customerAddress = customerAddress_item.text()

                # Set the values to the corresponding line edits
                self.ui.customerIDUpdate.setText(str(customerID))
                self.ui.customerNameUpdate.setText(customerName)
                self.ui.customerPhoneNumUpdate.setText(customerPhoneNum)
                self.ui.customerAddressUpdate.setText(customerAddress)
                self.ui.customerIDUpdate.setReadOnly(True)

    ######################### CUSTOMERS ############################
    

    def updateCustOrder(self):
        custName = self.ui.customerComboBox.currentText()
        custIDquery = "SELECT customerID FROM customer WHERE name = %s;"
        mycursor.execute(custIDquery, (custName,))
        result = mycursor.fetchone()  # Fetch the first row from the query result

        if result:
            custID = result[0]  # Extract the customer ID from the result
            self.ui.cusIDinOrders.setText(str(custID))  # Set the customer ID in the QLineEdit
        else:
            self.ui.cusIDinOrders.setText("")  # Clear the QLineEdit if no customer ID was found

    def updatePackOrder(self):
        packName = self.ui.packComboBox.currentText()
        packIDquery = "SELECT * FROM package WHERE name = %s;"
        mycursor.execute(packIDquery, (packName,))
        result = mycursor.fetchone()  # Fetch the first row from the query result

        if result:
            packID = result[0]  # Extract the customer ID from the result
            packPrice = result[2]
            self.ui.packIDinOrders.setText(str(packID))  # Set the customer ID in the QLineEdit
            self.ui.packPriceInOrder.setText(str(packPrice))
        else:
            self.ui.packIDinOrders.setText("")  
            self.ui.packPriceInOrder.setText("")
    
    def displayOrders(self):
        query = "SELECT customer.name, customer.customerID, package.name, package.packID, package.price, orders.orderDate, pays.date, orders.dlvryDate FROM pays INNER JOIN customer ON pays.customerID=customer.customerID INNER JOIN orders ON customer.customerID=orders.customerID INNER JOIN package ON orders.packID=package.packID"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.ordersTableWidget.clearContents()
        self.ui.ordersTableWidget.setRowCount(0)
        self.ui.ordersTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.ordersTableWidget.rowCount()
            self.ui.ordersTableWidget.insertRow(rowPos)
            self.ui.ordersTableWidget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.ordersTableWidget.setItem(rowPos, 1, QTableWidgetItem(str(row[1])))
            self.ui.ordersTableWidget.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            self.ui.ordersTableWidget.setItem(rowPos, 3, QTableWidgetItem(str(row[3])))
            self.ui.ordersTableWidget.setItem(rowPos, 4, QTableWidgetItem(str(row[4])))
            self.ui.ordersTableWidget.setItem(rowPos, 5, QTableWidgetItem(str(row[5])))
            self.ui.ordersTableWidget.setItem(rowPos, 6, QTableWidgetItem(str(row[6])))
            self.ui.ordersTableWidget.setItem(rowPos, 7, QTableWidgetItem(str(row[7])))
            
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.ordersTableWidget.columnCount()):
                item = self.ui.ordersTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    
        self.ui.ordersTableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeToContents)

    def displayOrdersDashboard(self):
        query = "SELECT customer.name, customer.customerID, package.name, package.packID, package.price, orders.orderDate, pays.date, orders.dlvryDate FROM pays INNER JOIN customer ON pays.customerID=customer.customerID INNER JOIN orders ON customer.customerID=orders.customerID INNER JOIN package ON orders.packID=package.packID"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.ordersTableWidgetDashboard.clearContents()
        self.ui.ordersTableWidgetDashboard.setRowCount(0)
        self.ui.ordersTableWidgetDashboard.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.ordersTableWidgetDashboard.rowCount()
            self.ui.ordersTableWidgetDashboard.insertRow(rowPos)
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 1, QTableWidgetItem(str(row[1])))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 3, QTableWidgetItem(str(row[3])))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 4, QTableWidgetItem(str(row[4])))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 5, QTableWidgetItem(str(row[5])))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 6, QTableWidgetItem(str(row[6])))
            self.ui.ordersTableWidgetDashboard.setItem(rowPos, 7, QTableWidgetItem(str(row[7])))
            
            
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.ordersTableWidgetDashboard.columnCount()):
                item = self.ui.ordersTableWidgetDashboard.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

            self.ui.ordersTableWidgetDashboard.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)

    def addOrder(self):
        custID = self.ui.cusIDinOrders.text()
        packID = self.ui.packIDinOrders.text()
        ordquery = "INSERT INTO orders(customerID,packID) VALUES (%s, %s);"
        mycursor.execute(ordquery, (custID, packID))
        payquery = "INSERT INTO pays(customerID,packID) VALUES (%s, %s);"
        mycursor.execute(payquery, (custID, packID))
        mydb.commit()
        QMessageBox.information(self, "Success", "Order added successfully.")

        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)

    #COME BACK HERE
    def searchOrder(self):
        query = "SELECT customer.name, customer.customerID, package.name, package.packID, package.price, orders.orderDate, orders.dlvryDate FROM customer " \
        "INNER JOIN orders ON customer.customerID=orders.customerID " \
        "INNER JOIN package ON orders.packID=package.packID " \
        "WHERE customer.name LIKE %s OR customer.customerID LIKE %s OR package.name LIKE %s OR package.packID LIKE %s"


        search_text = '%' + self.ui.lineEdit_1.text() + '%'  # Add wildcards to the search text
        mycursor.execute(query, (search_text, search_text, search_text, search_text))

        # Fetch all matching rows from the query result
        rows = mycursor.fetchall()

        table_widget = self.ui.ordersTableWidget
        self.ui.ordersTableWidget.clearContents()
        self.ui.ordersTableWidget.setRowCount(0)
        self.ui.ordersTableWidget.verticalHeader().setVisible(False)
        
        for row in rows:
            rowPos = table_widget.rowCount()
            table_widget.insertRow(rowPos)
            table_widget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            table_widget.setItem(rowPos, 1, QTableWidgetItem(str(row[1])))
            table_widget.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            table_widget.setItem(rowPos, 3, QTableWidgetItem(str(row[3])))
            table_widget.setItem(rowPos, 4, QTableWidgetItem(str(row[4])))
            table_widget.setItem(rowPos, 5, QTableWidgetItem(str(row[5])))
            table_widget.setItem(rowPos, 7, QTableWidgetItem(str(row[6])))


            # Set item flags to make cells non-editable
            for col in range(table_widget.columnCount()):
                item = table_widget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def deleteOrder(self):
        customerID = int(self.ui.deleteOrderNameCus.text())
        packageID = int(self.ui.deleteOrderNamePack.text())
        

        order_query = "DELETE FROM orders WHERE customerID = %s AND packID = %s;"
        pay_query = "DELETE FROM pays WHERE customerID = %s AND packID = %s;"
        values = (customerID, packageID)

        try:
            mycursor.execute(order_query, values)
            mycursor.execute(pay_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Order deleted successfully.")
        except Error as e:
            print(e)

        appFunctions.displayCustomer(self)
        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)
    
    def whenClickedOrderDelete(self):
        selected_indexes = self.ui.ordersTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            customerIDitem = self.ui.ordersTableWidget.item(row, 1)
            packIDitem = self.ui.ordersTableWidget.item(row, 3)

            if customerIDitem and packIDitem:
                customerID = int(customerIDitem.text())
                packID = int(packIDitem.text())

                # Set the values to the corresponding line edits
                self.ui.deleteOrderNameCus.setText(str(customerID))
                self.ui.deleteOrderNamePack.setText(str(packID))
                
                self.ui.deleteOrderNameCus.setReadOnly(True)
                self.ui.deleteOrderNamePack.setReadOnly(True)

    def updateOrderDel(self):
        customerID = int(self.ui.updateCusIDinOrders.text())
        packID = int(self.ui.updatePackIDinOrders.text())
        
        currDate = date.today()
        ord_query = "UPDATE orders SET dlvryDate = %s WHERE customerID = %s AND packID = %s"
        values = (currDate, customerID, packID)

        try:
            mycursor.execute(ord_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)

    def updateOrderPay(self):
        customerID = int(self.ui.updateCusIDinOrders.text())
        packID = int(self.ui.updatePackIDinOrders.text())
        
        currDate = date.today()
        pay_query = "UPDATE pays SET date = %s WHERE customerID = %s AND packID = %s"
        values = (currDate, customerID, packID)

        try:
            mycursor.execute(pay_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)

    def updateOrderPayReset(self):
        customerID = int(self.ui.updateCusIDinOrders.text())
        packID = int(self.ui.updatePackIDinOrders.text())
        
        pay_query = "UPDATE pays SET date = NULL WHERE customerID = %s AND packID = %s"
        values = (customerID, packID)

        try:
            mycursor.execute(pay_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)

    def updateOrderOrdReset(self):
        customerID = int(self.ui.updateCusIDinOrders.text())
        packID = int(self.ui.updatePackIDinOrders.text())
        
        pay_query = "UPDATE orders SET dlvryDate = NULL WHERE customerID = %s AND packID = %s"
        values = (customerID, packID)

        try:
            mycursor.execute(pay_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)

    def whenClickedOrderUpdate(self):
        selected_indexes = self.ui.ordersTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            customerName_item = self.ui.ordersTableWidget.item(row, 0)
            customerID_item = self.ui.ordersTableWidget.item(row, 1)
            packageName_item = self.ui.ordersTableWidget.item(row, 2)
            packageID_item = self.ui.ordersTableWidget.item(row, 3)
            price_item = self.ui.ordersTableWidget.item(row, 4)
            date_item = self.ui.ordersTableWidget.item(row, 5)
           

            if customerName_item and customerID_item and packageName_item and packageID_item and price_item and date_item:
                customerName = customerName_item.text()
                customerID = int(customerID_item.text())
                packageName = packageName_item.text()
                packageID = int(packageID_item.text())
                price = int(price_item.text())
                date = date_item.text()

                # Set the values to the corresponding line edits
                self.ui.updateCusInOrders.setText(customerName)
                self.ui.updateCusIDinOrders.setText(str(customerID))
                self.ui.updatePackInOrders.setText(packageName)
                self.ui.updatePackIDinOrders.setText(str(packageID))
                self.ui.updatePackPriceInOrder.setText(str(price))
                self.ui.updatePackDateInOrder.setText(date)
                

    
    ######################### ORDERS ############################

    def displayDishes(self):
        query = "SELECT * FROM dish;"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.dishesTableWidget.clearContents()
        self.ui.dishesTableWidget.setRowCount(0)
        self.ui.dishesTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.dishesTableWidget.rowCount()
            self.ui.dishesTableWidget.insertRow(rowPos)
            self.ui.dishesTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.dishesTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.dishesTableWidget.columnCount()):
                item = self.ui.dishesTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.ui.dishesTableWidget.horizontalHeader().setSectionResizeMode(
        QHeaderView.ResizeToContents)

        dishName = [row[1] for row in rows]
        self.ui.dish3Name1.clear()
        self.ui.dish3Name1.addItems(dishName)
        self.ui.dish3Name2.clear()
        self.ui.dish3Name2.addItems(dishName)
        self.ui.dish3Name3.clear()
        self.ui.dish3Name3.addItems(dishName)
        self.ui.dish4Name1.clear()
        self.ui.dish4Name1.addItems(dishName)
        self.ui.dish4Name2.clear()
        self.ui.dish4Name2.addItems(dishName)
        self.ui.dish4Name3.clear()
        self.ui.dish4Name3.addItems(dishName)
        self.ui.dish4Name4.clear()
        self.ui.dish4Name4.addItems(dishName)
        self.ui.dish5Name1.clear()
        self.ui.dish5Name1.addItems(dishName)
        self.ui.dish5Name2.clear()
        self.ui.dish5Name2.addItems(dishName)
        self.ui.dish5Name3.clear()
        self.ui.dish5Name3.addItems(dishName)
        self.ui.dish5Name4.clear()
        self.ui.dish5Name4.addItems(dishName)
        self.ui.dish5Name5.clear()
        self.ui.dish5Name5.addItems(dishName)

    def searchDishes(self):
        query = "SELECT * FROM dish WHERE name LIKE %s;"
        search_value = '%' + self.ui.lineEdit_3.text() + '%'
        mycursor.execute(query, (search_value,))
        rows = mycursor.fetchall()

        self.ui.dishesTableWidget.clearContents()
        self.ui.dishesTableWidget.setRowCount(0)
        self.ui.dishesTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.dishesTableWidget.rowCount()
            self.ui.dishesTableWidget.insertRow(rowPos)
            self.ui.dishesTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.dishesTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.dishesTableWidget.columnCount()):
                item = self.ui.dishesTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def inputDishes(self): 
        dishesName = self.ui.dishesName.text()
        insert_dish_data_sql = "INSERT INTO dish (name) VALUES (%s)"

        try:

            # Insert the new customer data
            mycursor.execute(insert_dish_data_sql, (dishesName,))
            mydb.commit()
            QMessageBox.information(self, "Success", "Dishes inserted successfully.")
            self.ui.dishesName.setText("")
         
            appFunctions.displayDishes(self)
        except Error as e:
            print(e)


    def updateDishes(self):
        dishesID = int(self.ui.updateDishID.text())
        dishesName = self.ui.updateDishName.text()
       

        update_query = "UPDATE dish SET name = %s WHERE dishID = %s"
        values = (dishesName,  dishesID)

        try:
            mycursor.execute(update_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Dish updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayDishes(self)
      

    def whenClickedDishesUpdate(self):
        selected_indexes = self.ui.dishesTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            dishesID_item = self.ui.dishesTableWidget.item(row, 0)
            dishesName_item = self.ui.dishesTableWidget.item(row, 1)
          

            if  dishesID_item and dishesName_item:
                dishesID = int( dishesID_item.text())
                dishesName = dishesName_item.text()
           

                # Set the values to the corresponding line edits
                self.ui.updateDishID.setText(str(dishesID))
                self.ui.updateDishName.setText(dishesName)
                self.ui.updateDishID.setReadOnly(True)

    
    def deleteDishes(self):
        # Get the course code from the line edit widget
        delete_dish = self.ui.deleteDishName.text()

        # Print the course code for debugging
        # print("Course Code:", course_code)
        

        delete_dish_sql = "DELETE FROM dish WHERE dishID = %s"

        try:

                mycursor.execute(delete_dish_sql, (delete_dish,))
                mydb.commit()
                
                QMessageBox.information(None, "Success", "Dish deleted successfully.")
          
                appFunctions.displayDishes(self)
           
        except Error as e:
            print(e)

    def whenClickedDishesDelete(self):
        selected_indexes = self.ui.dishesTableWidget.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()
            
            # Retrieve the data from the selected cell
            item = self.ui.dishesTableWidget.item(row, 0)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.deleteDishName.setText(value)

    ######################### DISHES ############################
    
    def inputServices(self):
        serviceName = self.ui.AddServiceName.text()

        insert_service_data_sql = "INSERT INTO extra_service (name) VALUES (%s)"
        fetchquery = "SELECT packID FROM package"
        
        try:
            # Insert the new service data
            mycursor.execute(insert_service_data_sql, (serviceName,))
            mydb.commit()
            QMessageBox.information(self, "Success", "Service inserted successfully.")
            self.ui.AddServiceName.setText("")

            # Get the service ID of the inserted service
            servquery = "SELECT serviceID FROM extra_service WHERE name = %s"
            mycursor.execute(servquery, (serviceName,))
            service = mycursor.fetchone()

            # Insert the service into all packages
            mycursor.execute(fetchquery)
            rows = mycursor.fetchall()
            for row in rows:
                packquery = "INSERT INTO includes_service (packID, serviceID) VALUES (%s, %s)"
                mycursor.execute(packquery, (row[0], service[0]))
                mydb.commit()
            
            appFunctions.displayServices(self)
        except Error as e:
            print(e)



    def updateServices(self):
        servicesID = int(self.ui.updateServiceID.text())
        servicesName = self.ui.updateServiceName.text()
       

        update_query = "UPDATE extra_service SET name = %s WHERE serviceID = %s"
        values = (servicesName,  servicesID)

        try:
            mycursor.execute(update_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Service updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayServices(self)
      

    def whenClickedServicesUpdate(self):
        selected_indexes = self.ui.servicesTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            serviceID_item = self.ui.servicesTableWidget.item(row, 0)
            serviceName_Item = self.ui.servicesTableWidget.item(row, 1)
          

            if  serviceID_item and serviceName_Item:
                serviceID = int( serviceID_item.text())
                servicesName = serviceName_Item.text()
           

                # Set the values to the corresponding line edits
                self.ui.updateServiceID.setText(str(serviceID))
                self.ui.updateServiceName.setText(servicesName)
                self.ui.updateServiceID.setReadOnly(True)

    
    def deleteServices(self):
        # Get the course code from the line edit widget
        delete_service = self.ui.deleteServiceName.text()

        # Print the course code for debugging
        # print("Course Code:", course_code)
        

        delete_service_sql = "DELETE FROM extra_service WHERE serviceID = %s"

        try:

                mycursor.execute(delete_service_sql, (delete_service,))
                mydb.commit()
                
                QMessageBox.information(None, "Success", "Service deleted successfully.")
          
                appFunctions.displayServices(self)
           
        except Error as e:
            print(e)

    def whenClickedServicesDelete(self):
        selected_indexes = self.ui.servicesTableWidget.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()
            
            # Retrieve the data from the selected cell
            item = self.ui.servicesTableWidget.item(row, 0)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.deleteServiceName.setText(value)

    def displayServices(self):
        query = "SELECT * FROM extra_service;"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.servicesTableWidget.clearContents()
        self.ui.servicesTableWidget.setRowCount(0)
        self.ui.servicesTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.servicesTableWidget.rowCount()
            self.ui.servicesTableWidget.insertRow(rowPos)
            self.ui.servicesTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.servicesTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.servicesTableWidget.columnCount()):
                item = self.ui.servicesTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            
        self.ui.servicesTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)

    def searchServies(self):
        query = "SELECT * FROM extra_service WHERE name LIKE %s"
        search_value = '%' + self.ui.lineEdit_4.text() + '%'
        mycursor.execute(query, (search_value,))
        rows = mycursor.fetchall()

        self.ui.servicesTableWidget.clearContents()
        self.ui.servicesTableWidget.setRowCount(0)
        self.ui.servicesTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.servicesTableWidget.rowCount()
            self.ui.servicesTableWidget.insertRow(rowPos)
            self.ui.servicesTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.servicesTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.servicesTableWidget.columnCount()):
                item = self.ui.servicesTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)


    ######################### SERVICES ############################
    
    def inputPackage(self):
        
            packName = self.ui.addPackageName.text()
            packPrice = self.ui.addPackagePrice.text()
            packPax = self.ui.addPackagePax.text()

            insert_pack_data_sql = "INSERT INTO package (name, price, num_pax) VALUES (%s, %s, %s)"

            try:

                # Insert the new customer data
                mycursor.execute(insert_pack_data_sql, (packName, packPrice, packPax))
                mydb.commit()
                QMessageBox.information(self, "Success", "Package inserted successfully.")
                self.ui.addPackageName.setText("")
                self.ui.addPackagePrice.setText("")
                self.ui.addPackagePax.setText("")
                appFunctions.displayPackage(self)
                appFunctions.displayPackageDish(self)
            except Error as e:
                print(e)

    def searchPackages(self):
        query = "SELECT * FROM package WHERE name LIKE %s OR price LIKE %s OR num_pax LIKE %s;"
        search_value = '%' + self.ui.lineEdit_5.text() + '%'
        mycursor.execute(query, (search_value,search_value,search_value))
        rows = mycursor.fetchall()

        self.ui.packagesTableWidget.clearContents()
        self.ui.packagesTableWidget.setRowCount(0)
        self.ui.packagesTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.packagesTableWidget.rowCount()
            self.ui.packagesTableWidget.insertRow(rowPos)
            self.ui.packagesTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.packagesTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.packagesTableWidget.setItem(rowPos, 2, QTableWidgetItem(str(row[2])))
            self.ui.packagesTableWidget.setItem(rowPos, 3, QTableWidgetItem(str(row[3])))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.packagesTableWidget.columnCount()):
                item = self.ui.packagesTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)


    
    def displayPackage(self):
        query = "SELECT * FROM package;"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.packagesTableWidget.clearContents()
        self.ui.packagesTableWidget.setRowCount(0)
        self.ui.packagesTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.packagesTableWidget.rowCount()
            self.ui.packagesTableWidget.insertRow(rowPos)
            self.ui.packagesTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.packagesTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.packagesTableWidget.setItem(rowPos, 2, QTableWidgetItem(str(row[2])))
            self.ui.packagesTableWidget.setItem(rowPos, 3, QTableWidgetItem(str(row[3])))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.packagesTableWidget.columnCount()):
                item = self.ui.packagesTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            
            key = row[0]
            comboBox = QComboBox()
            self.ui.packagesTableWidget.setCellWidget(rowPos, 4, comboBox)
            dishquery = "SELECT includes_dish.packID, dish.name FROM includes_dish INNER JOIN dish ON includes_dish.dishID=dish.dishID WHERE packID = '%s';"
            mycursor.execute(dishquery, (key,))
            dishIDs = mycursor.fetchall()
            for dish in dishIDs:
                comboBox.addItem(dish[1])

        packIDs = [row[1] for row in rows]
        self.ui.packComboBox.clear()
        self.ui.packComboBox.addItems(packIDs)

        self.ui.packagesTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        

    def displayPackageDish(self):
        query = "SELECT * FROM package;"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        self.ui.addCoupleDishTableWidget.clearContents()
        self.ui.addCoupleDishTableWidget.setRowCount(0)
        self.ui.addCoupleDishTableWidget.verticalHeader().setVisible(False)
        for row in rows:
            rowPos = self.ui.addCoupleDishTableWidget.rowCount()
            self.ui.addCoupleDishTableWidget.insertRow(rowPos)
            self.ui.addCoupleDishTableWidget.setItem(rowPos, 0, QTableWidgetItem(str(row[0])))
            self.ui.addCoupleDishTableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.addCoupleDishTableWidget.setItem(rowPos, 2, QTableWidgetItem(str(row[2])))
            self.ui.addCoupleDishTableWidget.setItem(rowPos, 3, QTableWidgetItem(str(row[3])))
                
            # Set item flags to make cells non-editable
            for col in range(self.ui.addCoupleDishTableWidget.columnCount()):
                item = self.ui.addCoupleDishTableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            
            key = row[0]
            comboBox = QComboBox()
            self.ui.addCoupleDishTableWidget.setCellWidget(rowPos, 4, comboBox)
            dishquery = "SELECT includes_dish.packID, dish.name FROM includes_dish INNER JOIN dish ON includes_dish.dishID=dish.dishID WHERE packID = '%s';"
            mycursor.execute(dishquery, (key,))
            dishIDs = mycursor.fetchall()
            for dish in dishIDs:
                comboBox.addItem(dish[1])


        self.ui.addCoupleDishTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        
    def whenClickedPackageDish(self):
        selected_indexes = self.ui.addCoupleDishTableWidget.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()
            
            # Retrieve the data from the selected cell
            item = self.ui.addCoupleDishTableWidget.item(row, column)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.dish3PackageName.setText(value)
                self.ui.dish4PackageName.setText(value)
                self.ui.dish5PackageName.setText(value)

    def updatePackage(self):
        packID = int(self.ui.updatePackageID.text())
        packName = self.ui.updatePackageName.text()
        packPrice = int(self.ui.updatePackagePrice.text())
        packPax = int(self.ui.updatePackagePax.text())

        update_query = "UPDATE package SET name = %s, price = %s, num_pax = %s WHERE packID = %s"
        values = (packName, packPrice, packPax, packID)

        try:
            mycursor.execute(update_query, values)
            mydb.commit()
            QMessageBox.information(self, "Success", "Package updated successfully.")
        except Error as e:
            print(e)

        appFunctions.displayPackage(self)
        appFunctions.displayOrders(self)
        appFunctions.displayOrdersDashboard(self)
    
    def whenClickedPackageUpdate(self):
        selected_indexes = self.ui.packagesTableWidget.selectedIndexes()

        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()

            packID_item = self.ui.packagesTableWidget.item(row, 0)
            packName_item = self.ui.packagesTableWidget.item(row, 1)
            packPrice_item = self.ui.packagesTableWidget.item(row, 2)
            packPax_item = self.ui.packagesTableWidget.item(row, 3)

            if packID_item and packName_item and packPrice_item and packPax_item:
                packID = int(packID_item.text())
                packName = packName_item.text()
                packPrice = packPrice_item.text()
                packPax = packPax_item.text()

                # Set the values to the corresponding line edits
                self.ui.updatePackageID.setText(str(packID))
                self.ui.updatePackageName.setText(packName)
                self.ui.updatePackagePrice.setText(packPrice)
                self.ui.updatePackagePax.setText(packPax)
                self.ui.updatePackageID.setReadOnly(True)
    
    def addDish3(self):
            packID = str(self.ui.dish3PackageName.text())
            d1n = self.ui.dish3Name1.currentText()
            d2n = self.ui.dish3Name2.currentText()
            d3n = self.ui.dish3Name3.currentText()

            dquery = "SELECT dishID FROM dish WHERE name = %s;"

            dquery = "SELECT dishID FROM dish WHERE name = '" + d1n + "';"
            mycursor.execute(dquery)
            d1 = mycursor.fetchone()

            dquery = "SELECT dishID FROM dish WHERE name = '" + d2n + "';"
            mycursor.execute(dquery)
            d2 = mycursor.fetchone()

            dquery = "SELECT dishID FROM dish WHERE name = '" + d3n + "';"
            mycursor.execute(dquery)
            d3 = mycursor.fetchone()
            clear = "DELETE FROM includes_dish WHERE packID = %s;"
            insert = "INSERT INTO includes_dish (packID, dishID) VALUES (%s,%s);"
            
            mycursor.execute(clear, (packID,))
            mydb.commit()
            try:

                # Insert dishes into package
                mycursor.execute(insert, (packID, d1[0]))
                mycursor.execute(insert, (packID, d2[0]))
                mycursor.execute(insert, (packID, d3[0]))
                mydb.commit()
                QMessageBox.information(self, "Success", "Dishes added successfully.")
                self.ui.addPackageName.setText("")
                self.ui.addPackagePrice.setText("")
                self.ui.addPackagePax.setText("")
                appFunctions.displayPackage(self)
                appFunctions.displayPackageDish(self)
            except Error as e:
                print(e)

    def addDish4(self):
        packID = str(self.ui.dish4PackageName.text())
        d1n = self.ui.dish4Name1.currentText()
        d2n = self.ui.dish4Name2.currentText()
        d3n = self.ui.dish4Name3.currentText()
        d4n = self.ui.dish4Name4.currentText()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d1n + "';"
        mycursor.execute(dquery)
        d1 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d2n + "';"
        mycursor.execute(dquery)
        d2 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d3n + "';"
        mycursor.execute(dquery)
        d3 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d4n + "';"
        mycursor.execute(dquery)
        d4 = mycursor.fetchone()
        
        
        clear = "DELETE FROM includes_dish WHERE packID = %s;"
        insert = "INSERT INTO includes_dish (packID, dishID) VALUES (%s,%s);"
        
        mycursor.execute(clear, (packID,))
        mydb.commit()
        try:

            # Insert dishes into package
            mycursor.execute(insert, (packID, d1[0]))
            mycursor.execute(insert, (packID, d2[0]))
            mycursor.execute(insert, (packID, d3[0]))
            mycursor.execute(insert, (packID, d4[0]))
            mydb.commit()
            QMessageBox.information(self, "Success", "Dishes added successfully.")
            self.ui.addPackageName.setText("")
            self.ui.addPackagePrice.setText("")
            self.ui.addPackagePax.setText("")
            appFunctions.displayPackage(self)
            appFunctions.displayPackageDish(self)
        except Error as e:
            print(e)

    def addDish5(self):
    
        packID = str(self.ui.dish5PackageName.text())
        d1n = self.ui.dish5Name1.currentText()
        d2n = self.ui.dish5Name2.currentText()
        d3n = self.ui.dish5Name3.currentText()
        d4n = self.ui.dish5Name4.currentText()
        d5n = self.ui.dish5Name5.currentText()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d1n + "';"
        mycursor.execute(dquery)
        d1 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d2n + "';"
        mycursor.execute(dquery)
        d2 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d3n + "';"
        mycursor.execute(dquery)
        d3 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d4n + "';"
        mycursor.execute(dquery)
        d4 = mycursor.fetchone()

        dquery = "SELECT dishID FROM dish WHERE name = '" + d5n + "';"
        mycursor.execute(dquery)
        d5 = mycursor.fetchone()
        
        
        clear = "DELETE FROM includes_dish WHERE packID = %s;"
        insert = "INSERT INTO includes_dish (packID, dishID) VALUES (%s,%s);"
        
        mycursor.execute(clear, (packID,))
        mydb.commit()
        try:

            # Insert dishes into package
            mycursor.execute(insert, (packID, d1[0]))
            mycursor.execute(insert, (packID, d2[0]))
            mycursor.execute(insert, (packID, d3[0]))
            mycursor.execute(insert, (packID, d4[0]))
            mycursor.execute(insert, (packID, d5[0]))
            mydb.commit()
            QMessageBox.information(self, "Success", "Dishes added successfully.")
            self.ui.addPackageName.setText("")
            self.ui.addPackagePrice.setText("")
            self.ui.addPackagePax.setText("")
            appFunctions.displayPackage(self)
            appFunctions.displayPackageDish(self)
        except Error as e:
            print(e)

    def deletePackage(self):
        # Get the course code from the line edit widget
        delete_pack = self.ui.deletePackageName.text()
        """delete_orders = "UPDATE orders SET packID = NULL WHERE packID = %s;"
        delete_pays =   "UPDATE pays SET packID = NULL WHERE packID = %s;"""
        delete_pack_sql = "DELETE FROM package WHERE packID = %s"

        try:
                """mycursor.execute(delete_orders, (delete_pack,))
                mycursor.execute(delete_pays, (delete_pack,))"""
                mycursor.execute(delete_pack_sql, (delete_pack,))
                mydb.commit()
                
                QMessageBox.information(None, "Success", "Package deleted successfully.")
          
                appFunctions.displayPackage(self)
                appFunctions.displayPackageDish(self)
                appFunctions.displayOrders(self)
                appFunctions.displayOrdersDashboard(self)
           
        except Error as e:
            print(e)

    def whenClickedPackDelete(self):
        selected_indexes = self.ui.packagesTableWidget.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            
            # Retrieve the data from the selected cell
            item = self.ui.packagesTableWidget.item(row, 0)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.deletePackageName.setText(value)

        
    ######################### PACKAGES ############################