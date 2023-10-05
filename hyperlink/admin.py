from django.contrib import admin
from . models import User, Seller, Buyer, Company

#admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Company)