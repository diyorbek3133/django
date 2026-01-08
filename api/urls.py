from django.urls import path
from .views import LugatListView

urlpatterns = [
    path('', LugatListView.as_view()),
    # path("users/",RegisterUser.as_view())
    # path("words/<int:pk>/",LugatListView.as_view())
]