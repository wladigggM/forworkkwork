from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import RegisterView, LoginUserView, PerformerProfileView, CustomerDashboard

app_name = 'users'

urlpatterns = [
    path('registration/', RegisterView.as_view(success_url=reverse_lazy('users:login')), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('performer/', PerformerProfileView.as_view(), name='performer'),
    path('customer/', CustomerDashboard.as_view(), name='customer'),
]
