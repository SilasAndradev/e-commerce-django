from django.urls import path
from .views import (
    LoginPage,
    RegisterUser,
    LogoutUser,
    ViewClientOrders
)
urlpatterns = [
    path('login/', LoginPage, name='login'),
    path('register/', RegisterUser, name='register'),
    path('logout/', LogoutUser, name='logout'),
    path('my-orders/', ViewClientOrders, name='my-orders'),
]