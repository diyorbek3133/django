from django.urls import path
from .views import input, register, user_login,log_out,add_word,get_users

urlpatterns = [
    path('input/', input, name="home"),          
    path('user/register/', register, name="register"), 
    path('', user_login, name="login"),
    path("logout/",log_out,name="logout"),
    path("add-word/",add_word),
    path("users",get_users)

]
