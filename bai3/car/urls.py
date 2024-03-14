from django.urls import path

from . import views

urlpatterns = [
    # path('register', UserRegisterView.as_view(), name='register'),
    # path('login', UserLoginView.as_view(), name='login'),
    path('api/cars', views.ListCreateCarView.as_view()),
    path('api/cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]
