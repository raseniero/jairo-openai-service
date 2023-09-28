from rest_framework import serializers
from .models import Seller, Company, Hyperlink, Access_Code, Buyer, Product, Cart, Placed_Product, Purchased_Order


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'company']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = '__all__'

class HyperLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hyperlink 
        fields = '__all__'


class AccessCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_Code
        fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart 
        fields = '__all__'

class PlacedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placed_Product 
        fields = '__all__'

class PurchasedOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased_Order 
        fields = '__all__'
        



