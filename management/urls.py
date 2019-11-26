from django.urls import path,include
from . import views
from django.conf.urls import url
urlpatterns=[
    path('welcome/',view=views.Welcome.as_view()),
    path('checkin/',view=views.CheckIn.as_view()),
    path('checkout/',view=views.CheckOut.as_view()),
]