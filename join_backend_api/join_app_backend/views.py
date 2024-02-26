from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from .serializer import UserSerializer
import json 
from django.http import HttpResponse


class LoginView(ObtainAuthToken):
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request' : request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
          
    def get(self, request):
        user = User.objects.all()
        serializers = UserSerializer(user, many=True)
        return JsonResponse(serializers.data, safe=False)


class SignupView(View):
    
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if not username:
            return HttpResponse('Missing username')
        try:
            if User.objects.filter(username=username).exists():
                return HttpResponse('User allready exist')
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return HttpResponse('User succesfully created')
        except Exception as e:
            return HttpResponse(str(e))