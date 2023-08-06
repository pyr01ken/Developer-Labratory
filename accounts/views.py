from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializer import UserRegisterSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from .utils import send_email


class UsersListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserDetailView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateAccountView(APIView):
    def get(self, request, email_active_code):
        user = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(100)
                user.save()
                return Response({'detail': 'user activate successfully.'}, status=status.HTTP_200_OK)
            return Response({'detail': 'user activated has error.'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = None
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            pass

        if not user:
            user = authenticate(email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def psot(self, request):
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user_email = serializer.validated_data['email']
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('Forgot Password', user_email, {'user': user}, 'emails/forgot_password.html')
                return Response({'detail': 'we send an email to you for forgot your password.'},
                                status=status.HTTP_200_OK)
            return Response({'not found': 'this email is not has an account.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            active_code = serializer.validated_data['active_code']
            user = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return Response({'not found': 'user not found.'}, status=status.HTTP_404_NOT_FOUND)

            user.set_password(serializer.validated_data['password'])
            user.email_active_code = get_random_string(100)
            # user.is_active = True
            user.save()
            return Response({'successfully': 'user password changed.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
