import csv

class Item:
    pay_rate = 0.8 # The payrate after 20% discount
    all_items = []
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validations to the recieved argument
        assert price >= 0, f"Price {price} not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} not greater than or equal to zero!"

        # Assign to self objece
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all_items.append(self)
    def calculate_total_price(self,):
        return self.price * self.quantity
    
    @property
    # Property Decorator
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instanciate_from_csv(cls):
        with open('store.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items:
            #print(item)
            Item(
                name = item.get('name'),
                price = float   (item.get('price')),
                quantity = int(item.get('quantity'))
           )
    @staticmethod
    def is_interger(num):
        # we will count out the floats that are point zero
        # For example 5.0, 8.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: 
            return False

  

    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"  