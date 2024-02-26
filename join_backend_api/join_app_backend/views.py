from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class LoginView(APIView):
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data,)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
    def get(self, request):
        user = User.objects.all().order_by('-date_joined')
        serializers = UserSerializer(user, many=True)
        return JsonResponse(serializers.data, safe=False)
