from abc import ABC
from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import User
from .utils import get_client_ip, send_email


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # todo: fix get client ip bug
        # request = self.context.get('request')
        # client_ip = None
        # if request:
        #     client_ip = get_client_ip(request)

        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        role = validated_data['role']
        password = validated_data['password']

        username = email.split('@')[0]

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            role=role,
            # ip=client_ip,
            email_active_code=get_random_string(100),
            is_active=False,
        )
        user.set_password(password)
        user.save()
        send_email('Activate the account', user.email, {'user', user}, 'emails/activate_account.html')
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    active_code = serializers.CharField(max_length=100)
    password = serializers.CharField()
