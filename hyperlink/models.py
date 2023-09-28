from django.db import models


class Seller(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.name}'
    
class Company(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    hyperlink = models.ForeignKey('Hyperlink', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    
class Hyperlink(models.Model):
    url = models.CharField(max_length=255, null=False)
    list_of_buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    list_of_products = models.ForeignKey('Product', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    list_of_code = models.ForeignKey('Access_Code', on_delete=models.CASCADE) # query

    def __str__(self):
        return f'{self.url}'
    
class Access_Code(models.Model):
    code = models.CharField(max_length=100, null=False)
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code}'

class Buyer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    purchased_orders = models.ForeignKey('Purchased_Order', on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
    
class Cart(models.Model):
    list_of_products = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField


class Placed_Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    purchased_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity =  models.IntegerField()

    def __str__(self):
        return f'{self.name}' 

class Purchased_Order(models.Model): 
     total_price = models.DecimalField(max_digits=10, decimal_places=2)
     status = models.IntegerField()
     list_of_placed_products = models.ForeignKey('Placed_Product', on_delete=models.CASCADE)


     

   





    
