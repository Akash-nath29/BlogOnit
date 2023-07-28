from django.urls import path
from .views import Home, PostView,WritePost, UpdatePost, DeletePost, AddCategory, CategoryView, LikeView

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('post/<int:pk>', PostView.as_view(), name="PostView"),
    path('writePost/', WritePost.as_view(), name="AddPost"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="UpdatePost"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="DeletePost"),
    path('addCategory/', AddCategory.as_view(), name="AddCategory"),
    path('category/<str:cats>/', CategoryView, name="Category"),
    path('like/<int:pk>', LikeView, name="like_post"),
]
