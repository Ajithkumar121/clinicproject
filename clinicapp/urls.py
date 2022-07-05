from .import views
from django.urls import path

app_name='clinicapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('logout',views.logout,name="logout"),
    path('details',views.details,name="details"),
    path('book',views.book,name="book"),
]
