from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.homepage, name='homepage'),
]

# path က django က function ဖြစ်ပါတယ်.
# 'home' က link name 
# views.homepage က views.py က လာတာ 
# name က keyword အနေနဲ့ သုံးတာ 