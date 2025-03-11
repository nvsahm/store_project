from django.db import models # import Djangos built-in database models module

class Store(models.Model): # define a model named 'Store' that inherits from Djangos base Model class
    store_name = models.CharField(max_length=100) # text field for the store's name, limited to 100 characters
    address = models.CharField(max_length=200) # text field for the store's address, limited to 200 characters
    opening_hours = models.CharField(max_length=100) # text field for the store opening hours, limited to 100 characters

    def __str__(self): # defines how the object is represented as a string
        return self.store_name # returns the store's name when printed or displayed in the Django admin panel

