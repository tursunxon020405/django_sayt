from django.urls import path
from .views import SignUp,user_logout

urlpatterns=[
    path('signup',SignUp.as_view(),name='signup'),
    path('logout',user_logout,name='logout'),
]