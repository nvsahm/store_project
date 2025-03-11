from django.db import models 

class Store(models.Model): 
    store_name = models.CharField(max_length=100) # text field for the store's name, limited to 100 characters
    address = models.CharField(max_length=200) # text field for the store's address, limited to 200 characters
    opening_hours = models.CharField(max_length=100) # text field for the store opening hours, limited to 100 characters

    def __str__(self): 
        return self.store_name 

