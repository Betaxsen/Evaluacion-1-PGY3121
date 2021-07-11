from django.urls import path
from .views import home, principal, elemento

urlpatterns = [
    path('', home, name="home"),
    path('principal', principal, name="principal"),
    path('elemento', elemento, name='elemento'),  
]
