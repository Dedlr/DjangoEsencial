from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views



urlpatterns = [

    path('admin/',admin.site.urls),

    path('hello-world/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.sorted,name='sort'),
    path('hi/<str:name>/<int:age>',local_views.say_hi,name='hi'),

    path('',posts_views.list_posts,name='feed'),
    path('posts/new/',posts_views.create_posts,name='create_posts'),


    path('account/login',users_views.login_view,name='login'),
    path('account/logout',users_views.logout_view,name='logout'),
    path('account/signup',users_views.signup_view,name='signup'),
    path('account/me/profile/',users_views.update_profile,name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
