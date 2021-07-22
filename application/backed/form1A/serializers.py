
from rest_framework import serializers
from .models import RegisterForm1A  
class Form1Aserializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterForm1A
        fields=('id','firstname','secondname','lastname','age','stream')
      