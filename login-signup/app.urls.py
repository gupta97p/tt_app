from django.urls import path, include
from users.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
     path('', include(router.urls))
]
