from django.urls import path
from login_app import views

app_name='login_app'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogOut.as_view(),name='logout') ,
]
