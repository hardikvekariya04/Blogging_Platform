from rest_framework import serializers
from account.models import User
# from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from account.utils import Util

# User registartion serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
      model = User
      fields=['name', 'email', 'password', 'password2']
      extra_kwargs={
        'password':{'write_only':True}
      }

    # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
      password = attrs.get('password')
      password2 = attrs.get('password2')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      return attrs

    def create(self, validate_data):
      return User.objects.create_user(**validate_data)

# User login serializer
class UserLoginSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    class Meta:
      model = User
      fields = ['name', 'password']

# User profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ['id', 'name', 'email']

# User change password serializer
class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
      fields = ['password', 'password2']

    def validate(self, attrs):
      password = attrs.get('password')
      password2 = attrs.get('password2')
      user = self.context.get('user')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      user.set_password(password)
      user.save()
      return attrs