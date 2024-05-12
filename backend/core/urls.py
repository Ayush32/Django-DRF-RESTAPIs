from django.urls import path
from .views import UserDetail, UserList

urlpatterns = [
    # get all users - GET
    path('users/',UserDetail.as_view()),
    path('users/<int:id>',UserDetail.as_view())
]
  