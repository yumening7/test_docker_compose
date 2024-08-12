from django.urls import path
from .views import signup, signin, me

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('me/', me, name='me'),
]