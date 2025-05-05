from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404, redirect
from user_auth_app.api.utils import send_activation_email, generate_activation_link


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                is_active=False
            )
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            activation_link = f"http://127.0.0.1:8000/api/activate/{uid}/{token}/"
            mail_subject = "Confirm your e-mail address"

            send_activation_email(user, activation_link, email, mail_subject)
            return Response({
                "message": "Please check your mailbox and confirm your e-mail address.",
                "token": token,
                "user_id": user.id,
                "email": user.email,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uid, token):
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = get_object_or_404(User, pk=uid)
            if token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return redirect(f"http://localhost:4200/login?success=account_activated")
            else:
                return redirect(f"http://localhost:4200/login?error=invalid_token")
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return redirect(f"http://localhost:4200/login?error=invalid_link")


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = User.objects.get(email=email)
            if not user.is_active:
                return Response({"detail": "Please confirm your e-mail address first."}, status=status.HTTP_403_FORBIDDEN)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"message": "Please enter an e-mail address."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            current_site = get_current_site(request).domain
            reset_link = f"http://localhost:4200/reset-password/{uid}/{token}/"
            mail_subject = "Reset password"
            message = render_to_string("user_auth_app/password_reset_email.html", {
                "user": user,
                "reset_link": reset_link
            })
            send_mail(
                subject=mail_subject,
                message="",
                from_email="no-reply@videoflix.com",
                recipient_list=[email],
                html_message=message,
                fail_silently=False,
            )
        except User.DoesNotExist:
            pass
        return Response({"message": "A password reset email has been sent to the provided email address."}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uid, token):
        try:
            uid_decoded = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=uid_decoded)
            if token_generator.check_token(user, token):
                new_password = request.data.get('password')
                if not new_password:
                    return Response({"message": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password successfully reset. You can log in now."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid or expired link."}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"message": "Invalid link."}, status=status.HTTP_400_BAD_REQUEST)
