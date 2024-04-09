from django.urls import path
from user.views import SignupAPIView

urlpatterns = [
    # path('login/', SignupAPIView.as_view(), name='login'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    ]