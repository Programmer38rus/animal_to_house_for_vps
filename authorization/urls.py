from django.contrib.auth.views import  (
  LoginView as login,
  LogoutView as logout,
)
from authorization.views import login, RegisterView, register, profile
from django.urls import path

app_name = 'authorization'


urlpatterns = [
  path('login/', login, name='login'),
  path('logout/', logout.as_view(), name='logout'),
  # path('register/', RegisterView.as_view(), name='registration'),
  path('register/', register, name='registration'),
  path('profile/', profile, name='profile'),
]