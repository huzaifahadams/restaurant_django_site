from django.urls.conf import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index-2'),
    path('about', views.about, name='about'),
    path('blog-single', views.blog_single, name='blog-single'),
    path('blog', views.blog, name='blog'),
    path('chef', views.chef, name='chef'),
    path('contact', views.contact, name='contact'),
    path('index', views.index2, name='index'),
    path('menu', views.menu, name='menu'),
    path('reservation', views.reservation, name='reservation'),
    path('login' , views.login, name= 'login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name= 'register')


]
