from django.urls import path
from . import views

from django.contrib import admin
admin.site.site_header="login to pavani administration"
admin.site.site_title="welcome to pavani's Dashboard"
admin.site.index_title="welcome to this portal"

urlpatterns = [
            path('home/', views.home, name='home'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
            path('projects/', views.projects, name='projects'),
    path('login/', views.login, name='login'),
#     path('registration/', views.registration, name='registration'),
        path('home_page/', views.home_page, name='home_page'),
        path('content/', views.content, name='content'),
        path('posts/', views.posts, name='posts'),
path('index/', views.index, name='index'),
    path('check_text/', views.check_text, name='check_text'),
        path('page/', views.page, name='page'),
                path('posts_data/', views.posts_data, name='posts_data'),
                # path('new/', views.new, name='new'),
# path('new/<int:post_id>/', new, name='new'),
                path('reference/', views.reference, name='reference'),
                path('register/', views.register, name='register'),


]