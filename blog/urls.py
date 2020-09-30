# May this url doesn't exist, so create manually 'urls.py'

from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [

    path('', views.all_blogs, name='all_blogs'), 	# '' is the home for blog app
    path('<int:blog_id>/', views.detail, name='detail'),
]