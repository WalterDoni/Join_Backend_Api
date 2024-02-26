from django.contrib import admin
from django.urls import path, include
from join_app_backend.views import LoginView, SignupView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view())
]

