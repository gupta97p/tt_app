from rest_framework import serializers
from .models import user_reg

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =user_reg
        fields=['username','email']
