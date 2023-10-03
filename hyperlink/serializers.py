from rest_framework import serializers
from .models import Seller, Buyer, Company, Hyperlink, Access_Code, Product, Cart, Placed_Product, Purchased_Order

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        # fields = '__all__'
        fields = ['id','email','first_name','last_name','password','phone_number','profile_picture','created_at','modified_at']

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id','email','first_name','last_name','phone_number','address','created_at']        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class HyperlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hyperlink
        fields = ['id','url', 'description', 'created_at', 'modified_at','company']

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_Code
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class PlacedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placed_Product
        fields = '__all__'

class PurchasedOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Purchased_Order
        fields = '__all__'






