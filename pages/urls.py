from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('signup/',views.signup,name="signup"),
    path('setting/',views.setting,name="setting"),
    path('logout/',views.logout,name="logout")
]
