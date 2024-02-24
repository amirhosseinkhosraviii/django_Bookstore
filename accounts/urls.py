from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('singup/', views.SingUpView.as_view(), name='signup'),

]

