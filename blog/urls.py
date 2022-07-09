from . import views
from django.urls import path,include
from django.contrib import admin


from blog.views import post_admin,BlogDetailView,about_us,contact,policy


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('register/', views.registerPage, name='register'),
    path('register/', views.register, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name= 'logout'),
    path('blog/<int:_id>', BlogDetailView, name='post_detail'),
    path('admin_login',post_admin,name='admin_login'),
    path('about_us', about_us, name='about_us'),
    path('policy', policy, name='policy'),
    path('contact', contact , name='contact'),
    
    
]

