#!/usr/bin/env python3

class Coffee:
    coffee_sizes = ["Small", "Medium", "Large"] #Permitted entries for size.

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property #Getter method
    def size(self):
        return self._size
    
    @property
    def price(self):
        return self._price
    
    @size.setter
    def size(self, size_value):
        if size_value not in Coffee.coffee_sizes: #The setter method performs validation logic to see whether the size entry is valid.
            print("size must be Small, Medium, or Large")
        else:
            self._size = size_value
    
    @price.setter
    def price(self, price_value):
        self._price = price_value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self._price += 1


