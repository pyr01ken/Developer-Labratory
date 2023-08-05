from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import User
from .utils import get_client_ip, send_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data, request):
            first_name = validated_data.get('first_name')
            last_name = validated_data.get('last_name')
            email = validated_data.get('email')
            role = validated_data.get('role')
            password = validated_data.get('password')

            username = email.split('@')[0]
            ip = get_client_ip(request)

            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                role=role,
                ip=ip,
                email_active_code=get_random_string(100),
                is_active=False,
            )
            user.set_password(password)
            user.save()
            # send_email('Activate the account', user.email, {'user', user}, 'emails/activate_account.html')
            return user

