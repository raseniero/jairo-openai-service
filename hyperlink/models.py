from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, phone_number, password, first_name, last_name):
        if not email:
            raise ValueError("Email is required.")
    
        username = email.split('@')[0] #example jedz@gmail.com -> jedz

        user = self.model(
            username = username, 
            email=email, 
            phone_number=phone_number, 
            first_name=first_name, 
            last_name=last_name, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password, first_name, last_name):
        user = self.create_user(
            email, 
            phone_number, 
            password, 
            first_name, 
            last_name, 
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]    

    objects = UserManager()

class Seller(User):
    profile_picture = models.CharField(max_length=100, null=False)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set is_staff and is_superuser to True for Seller instances
        self.is_staff = True
        self.is_superuser = True
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

class Buyer (User):
    address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"
    
class Company(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, blank=True)
    logo = models.CharField(max_length=100, null=False)                               
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
     
class Hyperlink(models.Model):
    name = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url}'

class Access_Code(models.Model):
    code = models.CharField(max_length=100, null=False)
    activated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    hyperlink = models.ForeignKey('Hyperlink', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code}'
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=1, max_digits=10)
    image = models.CharField(max_length=100, null=False)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    hyperlink = models.ForeignKey('Hyperlink', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

#
class Cart(models.Model): 
    product_name = models.ForeignKey('Product', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(decimal_places=1, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.list_of_products}'
    
class Placed_Product(models.Model): 
    product_name = models.CharField(max_length=255, null=False)
    purchased_price = models.DecimalField(decimal_places=1, max_digits=10)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(decimal_places=1, max_digits=10)
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
class Purchased_Order(models.Model):
    list_of_placed_products = models.ForeignKey('Placed_Product', on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=1, max_digits=10)
    status = models.CharField(max_length=100, null=False)
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.list_of_placed_products}'







     

   





    
