from django.urls import path
from .views import input, register, user_login,log_out,add_word,get_users,delete_word
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('input/', input, name="home"),          
    path('user/register/', register, name="register"), 
    path('', user_login, name="login"),
    path("logout/",log_out,name="logout"),
    path("add-word/",add_word),
    path("users",get_users),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("delete-word/<int:id>/", delete_word, name="delete_word"),

]
