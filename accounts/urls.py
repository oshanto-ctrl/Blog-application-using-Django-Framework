from django.urls import path
from .views import SignUpView

urlpatterns = [
    # Sign up view urls (accounts/signup/)
    path('signup/', SignUpView.as_view(), name='signup'),
]



