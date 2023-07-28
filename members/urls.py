from django.urls import path
from .views import UserRegistry, UserEdit, ShowUserProfile, EditUserProfile

urlpatterns = [
    path('register/', UserRegistry.as_view(), name="Register"),
    path('edit_profile/', UserEdit.as_view(), name="EditProfile"),
    path('<int:pk>/profile', ShowUserProfile.as_view(), name="ShowProfile"),
    path('<int:pk>/edit_profile_page', EditUserProfile.as_view(), name="EditProfile"),
]
