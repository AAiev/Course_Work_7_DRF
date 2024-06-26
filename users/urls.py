from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDeleteAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('', UserListAPIView.as_view(), name='user-list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete')
]
