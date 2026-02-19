#!/usr/bin/env python3

class Coffee:
    coffee_sizes = ["Small", "Medium", "Large"] #Permitted entries for size.

    def __init__(self, size, price):
        self.size = size
        self.price = price

        if size not in Coffee.coffee_sizes:
            print("size must be Small, Medium, or Large")
            return

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1


