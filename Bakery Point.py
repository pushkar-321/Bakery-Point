products = {
	1 : {1 : "Bread", 2 : 2.99, 3 : 10},
	2 : {1 : "Milk", 2 : 3.99, 3 : 10},
	3 : {1 : "Eggs", 2 : 4.99, 3 : 10},
}

record = {
	1 : {1 : "Pushkar", 2 : 1, 3 : 10, 4 : 30},
	2 : {1 : "Rohan", 2 : 2, 3 : 20, 4 : 40},
	3 : {1 : "Rohit", 2 : 3, 3 : 30, 4 : 50},
}

def order_products():
	print("Welcome to the store!")
	print("Here are our products")
	for i in products:
		print(products[i][1], "price = ", products[i][2], "and serial no.", i)
	print("What would you like to buy?")
	choice = int(input("Enter the product serial no.: "))
	choice2 = int(input("And enter in how much quantity: "))
	if choice in products:
		if products[choice][3] >= choice2:
			print("You have chosen", products[choice][1])
			print("The price is", products[choice][2]*choice2, "and in", choice2, "quantity")
			print("Thank you for shopping with us!")
			products[choice][3] -= choice2
		elif products[choice][3] < choice2:
			print("Sorry, we don't have enough stock")
		else:
			print("Sorry, we don't have that product in our inventory.")

def add_products():
	product_name = input("Enter the name of the products: ")
	product_price = float(input("Enter the price of the product: "))
	product_units = int(input("Enter the number of units: "))
	products[len(products) + 1] = {1 : product_name, 2 : product_price, 3 : product_units}
	print("Product added successfully!")

def remove_products():
	choice = int(input("Enter the serial no. of the product you want to remove: "))
	if choice in products:
		del products[choice]
	else:
		print("Enter a vald serial no.")

def display_products():
	choice = int(input("Enter the serial no. of the product you want to display: "))
	if choice in products:
		print("Product name:", products[choice][1])
		print("Product price:", products[choice][2])
		print("Product units:", products[choice][3])
	else:
		print("Enter a valid serial no.")

def display_all_products():
	print("Here are all the products")
	for i in products:
		print(products[i][1], "its price = ", products[i][2], "and there are", products[i][3], "units")

def add_record():
	name = input("Enter the name of the person: ")
	what_product = int(input("Enter the serial no. of the product: "))
	units = int(input("Enter the number of units: "))
	price = units*products[what_product][2]
	record[len(record) + 1] = {1 : name, 2: what_product, 3 : units, 4 : price}
	print("Record added successfully!")


def remove_record():
	choice = int(input("Enter the serial no. of the record you want to remove: "))
	if choice in record:
		del record[choice]
	else:
		print("Enter a vald serial no.")

def display_record():
	choice = int(input("Enter the serial no. of the record you want to display: "))
	if choice in record:
		print("Name:", record[choice][1])
		print("Product:", products[record[choice][2]][1])
		print("Units:", record[choice][3])
		print("Price:", record[choice][4])
	else:
		print("Enter a valid serial no.")

def display_all_record():
	print("Here are all the records")
	for i in record:
		print(record[i][1], "bought", products[record[i][2]][1], "for", record[i][3], "units and the total price is", record[i][4])

def update_record():
	choice = int(input("Enter the serial no. of the record you want to update: "))
	if choice in record:
		choice2 = int(input("Enter what you want to update: 1. Name, 2. Product, 3. Units: "))
		if choice2 == 1:
			name = input("Enter the new name: ")
			record[choice][choice2] = name
		elif choice2 == 2:
			product = int(input("Enter the new product serial no.: "))
			record[choice][choice2] = product
		elif choice2 == 3:
			units = int(input("Enter the new number of units: "))
			record[choice][choice2] = units
		else:
			print("Enter a valid choice")

choice = int(input("Enter are you a customer or an employee: 1. Customer, 2. Employee: "))
while True:
	if choice == 1:
		choice2 = int(input("Enter what you want to do: 1. Order products, 2. Display products, 3. Display all products: 4. Exit: "))
		if choice2 == 1:
			order_products()
		elif choice2 == 2:
			display_products()
		elif choice2 == 3:
			display_all_products()
		elif choice2 == 4:
			print("Thank you for using our system!")
			break
		else:
			print("Enter a valid choice")
	elif choice == 2:
		choice2 = int(input("Enter what you want to do: 1. Add products, 2. Remove products, 3. Display products, 4. Display all products, 5. Add record, 6. Remove record, 7. Display record, 8. Display all record, 9. Update record, 10. Exit: "))
		if choice2 == 1:
			add_products()
		elif choice2 == 2:
			remove_products()
		elif choice2 == 3:
			display_products()
		elif choice2 == 4:
			display_all_products()
		elif choice2 == 5:
			add_record()
		elif choice2 == 6:
			remove_record()
		elif choice2 == 7:
			display_record()
		elif choice2 == 8:
			display_all_record()
		elif choice2 == 9:
			update_record()
		elif choice2 == 10:
			print("Thank you for using our system!")
			break
		else:
			print("Enter a valid choice")
	else:
		print("Enter a valid choice")