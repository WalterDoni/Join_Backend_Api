from django.contrib import admin
from django.urls import path, include
from join_app_backend.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', UpdateContactView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', UpdateTaskView.as_view()),
    path('tasks/subtasks/', SubtaskView.as_view())
]

