from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View
from .serializer import *
import json 
from django.http import HttpResponse
from .models import  *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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

class SignupView(View):
    
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already exists')
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already exists')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key})
        except Exception as e:
            return HttpResponse(str(e))

class UsersView(APIView):
    authentication_classes  = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
     user = User.objects.all()
     serializers = UserSerializer(user, many=True)
     return JsonResponse(serializers.data, safe=False)


class ContactsView(APIView):
    authentication_classes  = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        contacts = ContactModel.objects.all().filter(author=request.user.id)
        serializer = ContactSerializer(contacts, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
     data = json.loads(request.body)
     serializer = ContactSerializer(data=data)
     if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, status=201)  
     return JsonResponse(serializer.errors, status=400)
 
  
class UpdateContactView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ContactModel.objects.get(pk=pk)
        except ContactModel.DoesNotExist:
            return None

    def patch(self, request, pk):
        contact = self.get_object(pk)
        if contact is None:
            return JsonResponse({"error": "Contact not found"}, status=404)

        if contact.author != request.user:
            return JsonResponse({"error": "You do not have permission to perform this action."}, status=403)

        data = json.loads(request.body)
        serializer = ContactSerializer(contact, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    
class DeleteContactView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ContactModel.objects.get(pk=pk)
        except ContactModel.DoesNotExist:
            return None

    def delete(self, request, pk):  
        contact = self.get_object(pk)
        
        if contact is not None:
            if contact.author != request.user:
                return JsonResponse({"error": "You do not have permission to perform this action."}, status=403)
            
            contact.delete()
            return HttpResponse("Deleted!")
        else:
            return HttpResponse("Task not found", status=404)
        
        
class TaskView(APIView):
    authentication_classes  = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
            
    def get(self, request):
        task = TaskModel.objects.all().filter(author=request.user.id)
        serializer = TaskSerializer(task, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=201)  
        return JsonResponse(serializer.errors, status=400)
    
    
class UpdateTaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            return None

    def patch(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return JsonResponse({"error": "Task not found"}, status=404)

        if task.author != request.user:
            return JsonResponse({"error": "You do not have permission to perform this action."}, status=403)

        data = json.loads(request.body)
        serializer = TaskSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    
class DeleteTaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            return None

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is not None:
            if task.author != request.user:
                return JsonResponse({"error": "You do not have permission to perform this action."}, status=403)
            
            task.delete()
            return HttpResponse("Deleted!")
        else:
            return HttpResponse("Task not found", status=404)
        
        
class SubtaskView(APIView):
 
    def get(self, request):
        subtask = SubtaskModel.objects.all()
        serializer = SubtaskSerializer(subtask, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = SubtaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    