from rest_framework import serializers
from .models import Seller, Company, Hyperlink


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


    





