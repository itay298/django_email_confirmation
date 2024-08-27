from django.urls import path
from accounts.views import Register, UserLogin, confirm_email

app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name="signup"),
    path('login/', UserLogin.as_view(), name="login"),
    path('confirm_email/<int:id>/', confirm_email, name="email"),
]