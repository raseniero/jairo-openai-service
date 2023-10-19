from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import Sum, F

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
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]    

    objects = UserManager()

class Seller(User):
    profile_picture = models.CharField(max_length=100, null=False)
    modified = models.DateTimeField(auto_now=True)

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not hasattr(self, 'cart'):
            Cart.objects.create(buyer_id=self)
        
         
    
class Company(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, blank=True)
    logo = models.CharField(max_length=100, null=False)                               
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    seller_id = models.ForeignKey('Seller', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
     
class Hyperlink(models.Model):
    name = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url}'

class Access_Code(models.Model):
    code = models.CharField(max_length=100, null=False)
    activated = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    hyperlink_id = models.ForeignKey('Hyperlink', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code}'
    
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=1, max_digits=10)
    image = models.CharField(max_length=100, null=False)
    seller_id = models.ForeignKey('Seller', on_delete=models.CASCADE)
    hyperlink_id = models.ForeignKey('Hyperlink', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

# BUYER PERSPECTIVE MODELS
class Cart(models.Model):
    summation = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    buyer_id = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def update_summation(self):
        # Calculate the total summation for all associated cart items
        total_summation = self.items.aggregate(total=Sum(F('quantity') * F('price')))['total']
        self.summation = total_summation
        self.save()

class Cart_Item(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name='items', null=True)

    def save(self, *args, **kwargs):
        # Calculate the summation
        self.summation = self.price * self.quantity

        if not self.cart_id:
            existing_cart = Cart.objects.first()

            if existing_cart:
                self.cart_id = existing_cart
            else:
                new_cart = Cart.objects.create()  #initialize
                self.cart_id = new_cart  # assign

        super().save(*args, **kwargs)  

        # Update the associated cart's summation
        self.cart_id.update_summation()

    def delete(self, *args, **kwargs):
        try:
            has_cart = self.cart_id is not None

            super().delete(*args, **kwargs)  # Delete the cart item

            if has_cart and self.cart_id.items.count() == 0:
                self.cart_id.delete()  # Delete the associated cart if it has no items:

            self.cart_id.update_summation()
        except Exception as error:
            print("Cart has been deleted!")

class Placed_Product(models.Model): 
    product_name = models.CharField(max_length=255, null=False)
    purchased_price = models.DecimalField(decimal_places=1, max_digits=10)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(decimal_places=1, max_digits=10)
    buyer_id = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
class Purchased_Order(models.Model):
    list_of_placed_products = models.ForeignKey('Placed_Product', on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=1, max_digits=10)
    status = models.CharField(max_length=100, null=False)
    buyer_id = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    seller_id = models.ForeignKey('Seller', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.list_of_placed_products}'







     

   





    
