from rest_framework import serializers, validators
from .models import Seller, Buyer, Company, Hyperlink, Access_Code, Product, Cart, Placed_Product, Purchased_Order
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return user, token

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        
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

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("email", "first_name", "last_name", "password", "phone_number", "profile_picture")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        Seller.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        seller = Seller.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"]
        )
        return seller






