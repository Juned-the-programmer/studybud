from django.urls import path
from . import views

urlpatterns = [
    path('room_detail/<str:pk>',views.room_detail,name="room_detail"),
    path('addroom/',views.addroom,name="addroom"),
    path('update-room/<str:pk>',views.update_room,name="update-room"),
    path('delete-room/<str:pk>',views.delete_room,name="delete-room"),
    path('user-profile/<str:pk>',views.user_profile,name="user-profile"),
    path('delete-message/<str:pk>',views.delete_message,name="delete-message"),
    path('current_user_profile/',views.current_user_profile,name="current_user_profile"),
]
