from django.urls import path,include
from .views import *
urlpatterns = [
   path('register',register_user,name='register_user'),
   path('login',user_login,name='user_login'),
   path('reminder',remind,name='reminder')
]