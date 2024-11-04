from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # Call to super function to have acces to all attribute/ methods
        super().__init__(
            name, price, quantity
        )
        # Run validations to the recieved argument
        assert broken_phones >= 0, f"Broken_phones {broken_phones} not greater than or equal to zero!"


        # Assign to self object
        self.broken_phones = broken_phones
   