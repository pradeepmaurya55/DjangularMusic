from rest_framework import serializers
from .models import User


class UserRegistratonSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email','name','password','password2','avatar'] 
        extra_kwargs={
            'password':{'write_only' : True}
        }

    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name','avatar']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    old_password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields = ['password','password2','old_password']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        old_password =attrs.get('old_password')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user=self.context.get('user')
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old Password is wrong")
        user.set_password(password)
        user.save()
        return attrs 
