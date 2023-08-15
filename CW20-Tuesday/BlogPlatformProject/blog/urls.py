from django.urls import path
from .views import home, post_list, category_details, category_list, PostDetailView, CommentUpdateView

app_name='blog'

urlpatterns = [
    path('', home, name="home"),
    path('post/', post_list, name="post_list"),
    # path('post/<int:pk>/', post_details, name="post_details"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_details"),
    path('categories/', category_list, name="category_list"),
    path('categories/<int:pk>/', category_details, name="category_details"),
    # path('comment_update/<int:pk>',comment_update,name='comment_update'),
    path('comment_update/<int:pk>',CommentUpdateView.as_view(),name='comment_update'),
]