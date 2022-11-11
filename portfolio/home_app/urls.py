from django.urls import path


#import views
from home_app import views

app_name='home_app'

urlpatterns = [
    path("",views.Index.as_view(),name='home'),
    path('message/',views.SenderMessage.as_view(),name='message')
]
