Store Management System
This is a simple Object-Oriented Python project designed to demonstrate basic principles of OOP by creating a store management system. The project includes functionality for managing items in inventory and handling products with specific characteristics, such as broken items.

Project Structure
The project includes three main files:

Item.py: Contains the Item class, which represents the core of the inventory system.
Phone.py: Contains the Phone class, which inherits from the Item class and adds an attribute for managing broken phones.
main.py: A sample file to demonstrate how to use the Item and Phone classes.
Key Features
Item Class (Item.py)
Attributes:

name: Name of the item, with validation to ensure it meets certain criteria.
price: Price of the item, with an assertion to ensure it is non-negative.
quantity: Quantity of the item in stock, which is also validated.
pay_rate: A class variable to apply a discount on all items, defaulting to 80% (20% off).
all_items: A class-level list to keep track of all item instances created.
Methods:

calculate_total_price(): Calculates the total price by multiplying the item price by quantity.
apply_discount(): Applies the discount rate specified in pay_rate to the item price.
instanciate_from_csv(): A class method that reads item data from store.csv to create instances automatically.
is_integer(): A static method to check if a number is an integer (includes float numbers with .0).
Property Decorators:

@property name: Getter for the item name, ensuring encapsulation.
@name.setter: Allows controlled setting of the name attribute.
Phone Class (Phone.py)
Inherits from Item and adds a specific attribute:
broken_phones: Number of broken phones in stock, validated to be non-negative.
Sample Code (main.py)
Demonstrates basic usage of the Item and Phone classes.
Shows how to create an Item instance, set its name, and access attributes.
How to Run
Clone the repository or download the files.

Ensure you have a store.csv file in the same directory with data for the instanciate_from_csv() method to work.

Run the main script to see the output.

bash
Copy code
python main.py
Example Usage
python
Copy code
from item import Item
from phone import Phone

# Create an Item instance
item1 = Item("Laptop", 1500, 10)
item1.apply_discount()
print(item1.calculate_total_price())

# Create a Phone instance
phone1 = Phone("iPhone", 1000, 5, 1)
print(phone1.calculate_total_price())
Requirements
Python 3.6+
CSV file store.csv formatted with columns: name, price, quantity
License
This project is licenced

Acknowledgments
Built as part of a tutorial on Object-Oriented Programming (OOP) in Python.
