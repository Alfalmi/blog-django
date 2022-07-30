from django.urls import re_path
from . import views

urlpatterns = [
    re_path('posts/$', views.PostView.as_view(), name='posts'),
    re_path('post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post'),
    re_path('write/$', views.WriteView.as_view(success_url="/posts/"), name='write')

]
