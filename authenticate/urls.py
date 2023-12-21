from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registered_users/', views.registered_users_view, name='registered_users'),
    path('update_user/<user_id>/', views.update_user, name='update_user'),
    path('remove_user/<user_id>', views.remove_user, name='remove_user'),
    path ('logout_user/', views.logout_user, name='logout_user')
]