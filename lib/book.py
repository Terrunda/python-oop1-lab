#!/usr/bin/env python3

class Book:
        def __init__(self, title, page_count: int):
                self.title = title
                self.page_count = page_count

                if (type(self.page_count) != int):
                        print("page_count must be an integer")
                        return
            
        def turn_page(self):
                print("Flipping the page...wow, you read fast.")
    

