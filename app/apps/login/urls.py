from django.urls import path
from .views import LoginFormView, LogoutAuthView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('', LogoutAuthView.as_view(), name='logout')
]
