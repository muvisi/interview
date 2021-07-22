from form1A.views import Form1AViewset
from django.urls import path

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('RegisterForm1A',Form1AViewset)

urlpatterns = [
    
   

]
urlpatterns += router.urls
